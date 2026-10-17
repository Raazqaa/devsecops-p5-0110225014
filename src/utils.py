import json
import yaml  # Ditambahkan agar parse_yaml & save_yaml tidak Error
from datetime import datetime
from typing import Any, Optional, Dict, List

def validate_string(value: str, min_length: int = 5) -> str:
    """Validasi string dengan minimal panjang"""
    if not value or len(value.strip()) < min_length:
        raise ValueError(f"Teks minimal harus {min_length} karakter")
    return value.strip()

def load_json(file_path: str) -> dict:
    """Membaca file JSON"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data: dict, file_path: str):
    """Menyimpan data ke file JSON"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def parse_yaml(file_path: str) -> dict:
    """Membaca file YAML"""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def save_yaml(data: dict, file_path: str):
    """Menyimpan data ke file YAML"""
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False)