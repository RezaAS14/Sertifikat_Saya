from __future__ import annotations
import sys
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS

ROOT = Path(__file__).resolve().parent
IMAGE_DIR = ROOT / "Sertifikat_Apresiasi"

def get_image_metadata(img_path: Path) -> dict:
    """Extract metadata from image."""
    try:
        img = Image.open(img_path)
        exif = img.getexif()
        metadata = {}
        if exif:
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = str(value)[:200]
        # Also get basic info
        metadata['format'] = img.format
        metadata['size'] = img.size
        return metadata
    except Exception as exc:
        return {"error": str(exc)}

def main() -> None:
    for img_path in sorted(IMAGE_DIR.glob("*.png")) + sorted(IMAGE_DIR.glob("*.jpg")):
        print(f"\n==== {img_path.name}")
        meta = get_image_metadata(img_path)
        for k, v in meta.items():
            print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
