import PyPDF2
import sys

files = [
    'Sertifikat_Apresiasi/Sertifikat Bug Hunt Ahmad Reza Aulia Siregar_tte.pdf',
    'Sertifikat_Apresiasi/SERTIFIKAT-APRESIASI-BUG-HUNTER-9.Ahmad-Reza.pdf',
    'Sertifikat_Apresiasi/432544605dc6fb61320d064fb2ce0715-3.pdf'
]

for filepath in files:
    print("\n" + "="*80)
    print(f"FILE: {filepath}")
    print("="*80)
    
    try:
        with open(filepath, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            print(f"Total pages: {len(reader.pages)}\n")
            
            for page_num in range(len(reader.pages)):
                print(f"--- PAGE {page_num + 1} ---")
                text = reader.pages[page_num].extract_text()
                if text.strip():
                    print(text)
                else:
                    print("[No text extracted - possibly image-based PDF]")
                print()
                
            # Metadata
            if reader.metadata:
                print("--- METADATA ---")
                for key, value in reader.metadata.items():
                    print(f"{key}: {value}")
                    
    except Exception as e:
        print(f"ERROR: {e}")
