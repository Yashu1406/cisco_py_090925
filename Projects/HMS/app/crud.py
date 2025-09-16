from sqlalchemy.exc import SQLAlchemyError
from app.models import Patient
from app.db import SessionLocal

class CRUDException(Exception):
    pass

def create_patient(name: str, age: int, disease: str) -> Patient:
    session = SessionLocal()
    try:
        patient = Patient(name=name, age=age, disease=disease)
        session.add(patient)
        session.commit()
        session.refresh(patient)
        return patient
    except SQLAlchemyError as e:
        session.rollback()
        raise CRUDException(f"DB error: {e}")
    finally:
        session.close()

def get_patient(patient_id: int) -> Patient | None:
    session = SessionLocal()
    try:
        return session.get(Patient, patient_id)
    finally:
        session.close()

def get_all_patients() -> list[Patient]:
    session = SessionLocal()
    try:
        return session.query(Patient).all()
    finally:
        session.close()

def update_patient(patient_id: int, name: str, age: int, disease: str) -> Patient | None:
    session = SessionLocal()
    try:
        patient = session.get(Patient, patient_id)
        if not patient:
            return None
        patient.name = name
        patient.age = age
        patient.disease = disease
        session.commit()
        session.refresh(patient)
        return patient
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()

def delete_patient(patient_id: int) -> bool:
    session = SessionLocal()
    try:
        patient = session.get(Patient, patient_id)
        if not patient:
            return False
        session.delete(patient)
        session.commit()
        return True
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()