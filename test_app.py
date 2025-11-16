# test_app.py
import app


def test_hello():
    client = app.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_echo():
    client = app.app.test_client()
    payload = {"msg": "ping"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert response.get_json() == payload


def test_create_student():
    client = app.app.test_client()
    payload = {"name": "Alice", "major": "CS"}

    response = client.post('/student', json=payload)
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Student has been created"
    assert data["data"] == payload
    assert "student_id" in data


def test_update_student():
    client = app.app.test_client()

    res = client.post('/student', json={"name": "Temp"})
    student_id = res.get_json()["student_id"]

    payload = {"name": "Updated Name", "major": "Math"}
    response = client.put(f'/student/{student_id}', json=payload)

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Student updated",
        "student_id": student_id,
        "data": payload
    }


def test_delete_student():
    client = app.app.test_client()

    res = client.post('/student', json={"name": "Bob"})
    student_id = res.get_json()["student_id"]

    response = client.delete(f'/student/{student_id}')

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Student deleted",
        "student_id": student_id
    }
