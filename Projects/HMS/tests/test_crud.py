def test_create_and_get_patient(client):
    # create
    r = client.post("/api/patients", json={"name": "Alice", "age": 30, "disease": "Flu"})
    assert r.status_code == 201
    js = r.get_json()
    assert js["name"] == "Alice"
    assert js["age"] == 30

    # get
    pid = js["id"]
    r2 = client.get(f"/api/patients/{pid}")
    assert r2.status_code == 200
    js2 = r2.get_json()
    assert js2["id"] == pid
    assert js2["name"] == "Alice"

    # update
    r3 = client.put(f"/api/patients/{pid}", json={"age": 31})
    assert r3.status_code == 200
    assert r3.get_json()["age"] == 31

    # delete
    r4 = client.delete(f"/api/patients/{pid}")
    assert r4.status_code == 204
    # then 404
    r5 = client.get(f"/api/patients/{pid}")
    assert r5.status_code == 404
