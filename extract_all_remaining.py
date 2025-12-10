from __future__ import annotations
import sys
from pathlib import Path

try:
    import PyPDF2
    from PIL import Image
    import easyocr
except ImportError as e:
    print(f"Missing: {e}")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
APRESIASI_DIR = ROOT / "Sertifikat_Apresiasi"

# Initialize OCR reader
reader = easyocr.Reader(['id', 'en'], gpu=False)

def extract_pdf_text(pdf_path: Path) -> str:
    """Extract text from PDF."""
    try:
        with pdf_path.open("rb") as f:
            reader_pdf = PyPDF2.PdfReader(f)
            if not reader_pdf.pages:
                return ""
            text_parts = []
            for page in reader_pdf.pages[:3]:  # First 3 pages
                text = page.extract_text() or ""
                text_parts.append(text)
            return "\n".join(text_parts)
    except Exception as e:
        return f"ERROR: {e}"

def extract_image_text(img_path: Path) -> str:
    """Extract text from image using EasyOCR."""
    try:
        result = reader.readtext(str(img_path), detail=0)
        return '\n'.join(result) if result else ""
    except Exception as e:
        return f"ERROR: {e}"

# Target files to extract
TARGETS = [
    "20250611215317tanda apresiasi-ahmad reza aulia siregar-1.png",
    "20250828-AhmadRezaAuliaSiregar_sign.pdf",
    "432544605dc6fb61320d064fb2ce0715-3.pdf",
    "Ahmad Reza Aulia Siregar_sign.pdf",
    "Ahmad-Reza-Aulia-Siregar.png",
    "IMG-20250903-WA0021.jpg",
    "SERTIFIKAT_APRESIASI_AHMAD_REZA_AULIA_SIREGAR.pdf",
]

def main() -> None:
    for fname in TARGETS:
        fpath = APRESIASI_DIR / fname
        if not fpath.exists():
            print(f"❌ {fname}: FILE NOT FOUND\n")
            continue
        
        print(f"\n{'='*80}")
        print(f"FILE: {fname}")
        print('='*80)
        
        if fpath.suffix.lower() in ['.pdf']:
            text = extract_pdf_text(fpath)
        elif fpath.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            text = extract_image_text(fpath)
        else:
            text = "UNKNOWN FORMAT"
        
        if text.startswith("ERROR") or not text:
            print("[NO TEXT EXTRACTED]")
        else:
            # Print first 1000 chars
            snippet = text[:1000]
            print(snippet)
            if len(text) > 1000:
                print("\n... [TEXT TRUNCATED]")

if __name__ == "__main__":
    main()
