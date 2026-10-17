import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from utils import validate_string

app = FastAPI(title="DevSecOps Dashboard", description="A simple Security and Monitoring Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
notes_db = []

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    template_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>DevSecOps Dashboard</h1><p>Template index.html belum ditemukan.</p>")

@app.get("/notes")
async def get_notes():
    return {"data": notes_db}

@app.post("/notes")
async def create_note(note: str):
    try:
        note_data = validate_string(note)
        new_note = {
            "id": len(notes_db) + 1 if not notes_db else max(n["id"] for n in notes_db) + 1,
            "content": note_data,
            "created_at": datetime.now().isoformat()
        }
        notes_db.append(new_note)
        return {"message": "Catatan berhasil ditambahkan", "data": new_note}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Gagal menambah catatan: {str(e)}")

# Endpoint Edit Note
@app.put("/notes/{note_id}")
async def update_note(note_id: int, note: str):
    try:
        note_data = validate_string(note)
        for item in notes_db:
            if item["id"] == note_id:
                item["content"] = note_data
                item["updated_at"] = datetime.now().isoformat()
                return {"message": "Catatan berhasil diperbarui", "data": item}
        raise HTTPException(status_code=404, detail="Catatan tidak ditemukan")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Gagal memperbarui catatan: {str(e)}")

# Endpoint Hapus Note
@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    global notes_db
    for index, item in enumerate(notes_db):
        if item["id"] == note_id:
            deleted_item = notes_db.pop(index)
            return {"message": "Catatan berhasil dihapus", "data": deleted_item}
    raise HTTPException(status_code=404, detail="Catatan tidak ditemukan")