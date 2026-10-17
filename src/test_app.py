import pytest
from fastapi.testclient import TestClient
from app import app, notes_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_notes():
    notes_db.clear()

def test_dashboard_endpoint():
    response = client.get("/")
    assert response.status_code == 200

def test_create_note_endpoint():
    response = client.post("/notes?note=Security Note Test")
    assert response.status_code == 200
    assert response.json()["data"]["content"] == "Security Note Test"

def test_update_note_endpoint():
    # Buat note dulu
    client.post("/notes?note=Catatan Awal")
    # Edit note id 1
    response = client.put("/notes/1?note=Catatan Diperbarui")
    assert response.status_code == 200
    assert response.json()["data"]["content"] == "Catatan Diperbarui"

def test_delete_note_endpoint():
    # Buat note dulu
    client.post("/notes?note=Catatan Hapus")
    # Hapus note id 1
    response = client.delete("/notes/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Catatan berhasil dihapus"