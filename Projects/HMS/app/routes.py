from flask import Blueprint, request, jsonify
from app.crud import create_patient, get_patient, get_all_patients, update_patient, delete_patient
from app.emailer import send_patient_creation_email
from app.exceptions import PatientNotFoundError

bp = Blueprint("api", __name__)

@bp.route("/patients", methods=["POST"])
def api_create_patient():
    data = request.json
    if not data or not all(k in data for k in ("name", "age", "disease")):
        return jsonify({"error": "Missing fields"}), 400
    patient = create_patient(data["name"], data["age"], data["disease"])
    send_patient_creation_email(patient)
    return jsonify({"id": patient.id, "name": patient.name, "age": patient.age, "disease": patient.disease}), 201

@bp.route("/patients/<int:patient_id>", methods=["GET"])
def api_get_patient(patient_id):
    patient = get_patient(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({"id": patient.id, "name": patient.name, "age": patient.age, "disease": patient.disease})

@bp.route("/patients", methods=["GET"])
def api_get_all_patients():
    patients = get_all_patients()
    result = [{"id": p.id, "name": p.name, "age": p.age, "disease": p.disease} for p in patients]
    return jsonify(result)

@bp.route("/patients/<int:patient_id>", methods=["PUT"])
def api_update_patient(patient_id):
    data = request.json
    patient = update_patient(patient_id, data.get("name"), data.get("age"), data.get("disease"))
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({"id": patient.id, "name": patient.name, "age": patient.age, "disease": patient.disease})

@bp.route("/patients/<int:patient_id>", methods=["DELETE"])
def api_delete_patient(patient_id):
    success = delete_patient(patient_id)
    if not success:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({"message": "Patient deleted"})