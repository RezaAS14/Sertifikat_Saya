from __future__ import annotations
import sys
from pathlib import Path

try:
    import easyocr
except ImportError:
    sys.stderr.write("EasyOCR not installed\n")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
IMAGE_DIR = ROOT / "Sertifikat_Apresiasi"

# Initialize reader once
reader = easyocr.Reader(['id', 'en'], gpu=False)

def extract_text_easyocr(img_path: Path) -> str:
    """Extract text dari gambar menggunakan EasyOCR."""
    try:
        result = reader.readtext(str(img_path), detail=0)
        text = '\n'.join(result)
        return text.strip() if text else ""
    except Exception as exc:
        return f"<error> {exc}"

def main() -> None:
    images = [
        "20250611215317tanda apresiasi-ahmad reza aulia siregar-1.png",
        "Ahmad-Reza-Aulia-Siregar.png",
        "SertifikatPersandian(Ahmad Reza).png",
        "IMG-20250903-WA0021.jpg"
    ]
    
    for img_name in images:
        img_path = IMAGE_DIR / img_name
        if not img_path.exists():
            print(f"❌ {img_name}: NOT FOUND\n")
            continue
            
        print(f"📄 {img_name}")
        text = extract_text_easyocr(img_path)
        
        if not text or text.startswith("<error"):
            print(f"  ⚠️ {text}\n")
        else:
            # Print first 600 chars
            snippet = text[:600]
            print(snippet)
            if len(text) > 600:
                print("... [truncated]\n")
            else:
                print()

if __name__ == "__main__":
    main()
