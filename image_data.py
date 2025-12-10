from __future__ import annotations
import json
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGE_DIR = ROOT / "Sertifikat_Apresiasi"

# Hardcoded extracted data (manual/previous OCR attempts)
IMAGE_DATA = {
    "20250611215317tanda apresiasi-ahmad reza aulia siregar-1.png": {
        "issuer": "Cek berkas langsung (gambar)",
        "date": "-"
    },
    "Ahmad-Reza-Aulia-Siregar.png": {
        "issuer": "Cek berkas langsung (gambar)",
        "date": "-"
    },
    "SertifikatPersandian(Ahmad Reza).png": {
        "issuer": "Badan Siber dan Sandi Negara (persandian)",
        "date": "-"
    },
    "IMG-20250903-WA0021.jpg": {
        "issuer": "Cek berkas langsung (foto)",
        "date": "-"
    }
}

def main() -> None:
    for img_file, data in IMAGE_DATA.items():
        img_path = IMAGE_DIR / img_file
        if img_path.exists():
            print(f"{img_file}:")
            print(f"  Penerbit: {data['issuer']}")
            print(f"  Tanggal: {data['date']}")
        else:
            print(f"{img_file}: NOT FOUND")

if __name__ == "__main__":
    main()
