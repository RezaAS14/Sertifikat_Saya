import PyPDF2
from pdf2image import convert_from_path
from PIL import Image
import io

files = [
    'Sertifikat_Apresiasi/Sertifikat Bug Hunt Ahmad Reza Aulia Siregar_tte.pdf',
    'Sertifikat_Apresiasi/SERTIFIKAT-APRESIASI-BUG-HUNTER-9.Ahmad-Reza.pdf',
    'Sertifikat_Apresiasi/432544605dc6fb61320d064fb2ce0715-3.pdf'
]

print("Mengkonversi PDF ke gambar untuk analisis visual...")
print("=" * 80)

for filepath in files:
    print(f"\nFILE: {filepath}")
    print("-" * 80)
    
    try:
        # Convert PDF to images
        images = convert_from_path(filepath, dpi=200, first_page=1, last_page=1)
        
        if images:
            img = images[0]
            print(f"✓ PDF berhasil dikonversi ke gambar")
            print(f"  Ukuran: {img.size}")
            print(f"  Mode: {img.mode}")
            
            # Save as temporary PNG for manual inspection
            output_name = filepath.replace('/', '_').replace('.pdf', '_preview.png')
            img.save(output_name)
            print(f"  Preview disimpan: {output_name}")
            
            # Coba deteksi teks dengan analisis warna
            pixels = img.load()
            width, height = img.size
            
            # Sample beberapa pixel untuk deteksi
            print(f"  Analisis: Image-based certificate, memerlukan OCR atau manual reading")
            
    except Exception as e:
        print(f"ERROR: {e}")

print("\n" + "=" * 80)
print("Silakan cek file preview yang sudah disimpan untuk melihat isi sertifikat")
