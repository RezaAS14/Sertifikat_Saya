import PyPDF2
import os

files = [
    'Sertifikat_Apresiasi/20250709083655AhmadRezaAuliaSiregar.pdf',
    'Sertifikat_Apresiasi/432544605dc6fb61320d064fb2ce0715-3.pdf',
    'Sertifikat_Apresiasi/Ahmad Reza Aulia Siregar_sign.pdf'
]

for filepath in files:
    print(f"\n{'='*60}")
    print(f"FILE: {os.path.basename(filepath)}")
    print('='*60)
    try:
        with open(filepath, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            print(f"Total pages: {len(reader.pages)}")
            
            all_text = ""
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                all_text += text
                if text.strip():
                    print(f"\n--- Page {i+1} ---")
                    print(text[:500])
            
            # Coba ekstrak metadata
            if reader.metadata:
                print("\n--- METADATA ---")
                for key, value in reader.metadata.items():
                    print(f"{key}: {value}")
            
            if not all_text.strip():
                print("\n[WARNING] No text found - possibly image-based PDF")
                
    except Exception as e:
        print(f"Error: {e}")
