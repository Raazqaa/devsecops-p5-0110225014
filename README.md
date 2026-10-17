# DevSecOps Console - Tugas 5

## 1. Nama Aplikasi & Fungsi
**DevSecOps Console** adalah aplikasi web sederhana berbasis FastAPI yang berfungsi sebagai antarmuka pemantauan dan pencatatan audit log keamanan (*Security Activity Log & Audit Monitor*). Aplikasi ini menyediakan fitur CRUD (Create, Read, Update, Delete) catatan keamanan secara *in-memory*.

## 2. Bahasa & Framework
- **Bahasa Pemrograman:** Python 3.12
- **Framework Backend:** FastAPI & Uvicorn
- **Frontend:** HTML5 & Tailwind CSS
- **Testing:** Pytest & HTTPX
- **SAST Tool:** Bandit

## 3. Cara Menjalankan Aplikasi

### Lintas Dependensi:
```bash
pip install -r requirements.txt

A. Jalankan Unit Test:
python -m pytest src/test_app.py -v

B. Jalankan Web Application:
cd src
python -m uvicorn app:app --reload