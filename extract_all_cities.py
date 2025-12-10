import PyPDF2
import os
import glob

# Get all PDF files from Sertifikat_Apresiasi
pdf_files = glob.glob('Sertifikat_Apresiasi/*.pdf')
pdf_files.extend(glob.glob('Sertifikat_Bootcamp/*.pdf'))
pdf_files.extend(glob.glob('Sertifikat_Coding/*.pdf'))

results = {}

for filepath in sorted(pdf_files):
    filename = os.path.basename(filepath)
    print(f"\n{'='*70}")
    print(f"FILE: {filename}")
    print('='*70)
    
    try:
        with open(filepath, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            
            all_text = ""
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                all_text += text + "\n"
            
            if all_text.strip():
                # Print first 1500 characters to see institution info
                print(all_text[:1500])
                results[filename] = all_text[:1500]
            else:
                print("[WARNING] No text found - image-based PDF")
                results[filename] = "[IMAGE-BASED PDF]"
                
    except Exception as e:
        print(f"Error: {e}")
        results[filename] = f"[ERROR: {e}]"

print("\n\n" + "="*70)
print("SUMMARY - Files processed:", len(results))
print("="*70)
