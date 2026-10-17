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

## 4. Pipeline CI/CD (DevSecOps)
    Pipeline otomatisasi diimplementasikan menggunakan GitHub Actions (.github/workflows/devsecops.yml) dengan dua tahapan (job) utama:

    Build & Unit Test (build): Menginstall dependensi Python dan menjalankan automated unit testing menggunakan pytest.

    SAST Security Scan (sast-scan): Melakukan Pemindaian Keamanan Kode Statis (Static Application Security Testing) menggunakan Bandit untuk mendeteksi potensi kerentanan pada kode Python. Job ini berjalan secara sekuensial setelah job build berhasil (needs: build).