from __future__ import annotations
import sys
from pathlib import Path

try:
    from PIL import Image
    import pytesseract
except ImportError:
    sys.stderr.write("Required: pip install pytesseract pillow\n")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
IMAGE_DIR = ROOT / "Sertifikat_Apresiasi"


def extract_image_text(image_path: Path) -> str:
    """Extract text from PNG/JPG using OCR."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang="ind+eng")
        return text.strip() if text else ""
    except Exception as exc:  # noqa: BLE001
        return f"<error> {exc}"


def main() -> None:
    for img_path in sorted(IMAGE_DIR.glob("*.png")) + sorted(IMAGE_DIR.glob("*.jpg")):
        print("====", img_path.name)
        text = extract_image_text(img_path)
        if not text:
            print("(no text extracted)\n")
        else:
            snippet = text[:800]
            print(snippet)
            if len(text) > 800:
                print("... [truncated]\n")
            else:
                print()


if __name__ == "__main__":
    main()
