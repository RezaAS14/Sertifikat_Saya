from __future__ import annotations
import sys
from pathlib import Path
from typing import Iterable

try:
    import PyPDF2  # type: ignore
except ImportError:
    sys.stderr.write("PyPDF2 not installed. Install with: pip install PyPDF2\n")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
PDF_DIRS: Iterable[Path] = [ROOT / "Sertifikat_Apresiasi", ROOT / "Sertifikat_Bootcamp", ROOT / "Sertifikat_Coding"]


def extract_first_page_text(pdf_path: Path) -> str:
    try:
        with pdf_path.open("rb") as f:
            reader = PyPDF2.PdfReader(f)
            if not reader.pages:
                return ""
            page0 = reader.pages[0]
            text = page0.extract_text() or ""
            # Normalize whitespace for readability
            return "\n".join(line.strip() for line in text.splitlines() if line.strip())
    except Exception as exc:  # noqa: BLE001
        return f"<error> {exc}"


def main() -> None:
    for folder in PDF_DIRS:
        if not folder.exists():
            continue
        for pdf_path in sorted(folder.glob("*.pdf")):
            text = extract_first_page_text(pdf_path)
            print("====", pdf_path.relative_to(ROOT))
            if not text:
                print("(no text extracted)\n")
            else:
                # Print only first 1200 chars to keep output concise
                snippet = text[:1200]
                print(snippet)
                if len(text) > 1200:
                    print("... [truncated]\n")
                else:
                    print()


if __name__ == "__main__":
    main()
