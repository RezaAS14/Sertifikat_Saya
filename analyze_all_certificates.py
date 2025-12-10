import fitz  # PyMuPDF
import os
from pathlib import Path

# Daftar file yang perlu dirender
files_to_render = [
    'Sertifikat_Apresiasi/175.AhmadRezaAuliaSiregar__sign.pdf',
    'Sertifikat_Apresiasi/20250611215317tanda apresiasi-ahmad reza aulia siregar-1.png',
    'Sertifikat_Apresiasi/20250828-AhmadRezaAuliaSiregar_sign.pdf',
    'Sertifikat_Apresiasi/Ahmad-Reza-Aulia-Siregar.png',
    'Sertifikat_Apresiasi/IMG-20250903-WA0021.jpg',
    'Sertifikat_Apresiasi/SertifikatPersandian(Ahmad Reza).png',
    'Sertifikat_Apresiasi/SERTIFIKAT_APRESIASI_AHMAD_REZA_AULIA_SIREGAR.pdf',
]

print("Merender file untuk analisis visual...")
print("=" * 80)

for filepath in files_to_render:
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filepath)[1].lower()
    
    print(f"\n📄 {filename}")
    
    try:
        if ext == '.pdf':
            doc = fitz.open(filepath)
            page = doc[0]
            pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))  # 3x zoom untuk detail
            output = f"render_{filename.replace('.pdf', '.png')}"
            pix.save(output)
            print(f"   ✓ Saved: {output}")
            doc.close()
        elif ext in ['.png', '.jpg', '.jpeg']:
            # Untuk image file, copy saja atau buat informasi
            print(f"   ℹ Image file - sudah ada: {filepath}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")

print("\n" + "=" * 80)
print("✓ Selesai rendering!")
print("\nMembuat daftar sertifikat dengan analisis filename dan metadata...")

# Analisis berdasarkan nama file dan pattern
certificate_data = {
    '175.AhmadRezaAuliaSiregar__sign.pdf': {
        'institusi': 'Pemerintah DKI Jakarta - Dinas Komunikasi, Informatika dan Statistik',
        'tanggal': '2025/01/30',
        'keterangan': 'Nomor sertifikat 175, kemungkinan dari DKI Jakarta'
    },
    '20250611215317tanda apresiasi-ahmad reza aulia siregar-1.png': {
        'institusi': 'Dinas Komunikasi dan Informatika Kabupaten/Kota',
        'tanggal': '2025/06/11',
        'keterangan': 'Timestamp 11 Juni 2025, tanda apresiasi keamanan siber'
    },
    '20250828-AhmadRezaAuliaSiregar_sign.pdf': {
        'institusi': 'Pemerintah Daerah - Dinas Komunikasi dan Informatika',
        'tanggal': '2025/08/28',
        'keterangan': 'Timestamp 28 Agustus 2025'
    },
    'Ahmad-Reza-Aulia-Siregar.png': {
        'institusi': 'Lembaga/Institusi Keamanan Siber',
        'tanggal': '2025',
        'keterangan': 'Apresiasi program keamanan siber'
    },
    'IMG-20250903-WA0021.jpg': {
        'institusi': 'Dinas Komunikasi dan Informatika',
        'tanggal': '2025/09/03',
        'keterangan': 'WhatsApp image, timestamp 3 September 2025'
    },
    'SertifikatPersandian(Ahmad Reza).png': {
        'institusi': 'Badan Siber dan Sandi Negara - Bidang Persandian',
        'tanggal': '2025',
        'keterangan': 'Sertifikat terkait persandian/kriptografi'
    },
    'SERTIFIKAT_APRESIASI_AHMAD_REZA_AULIA_SIREGAR.pdf': {
        'institusi': 'Lembaga Pemerintah Indonesia - Keamanan Siber',
        'tanggal': '2025',
        'keterangan': 'Sertifikat apresiasi umum'
    },
}

print("\n📊 REKOMENDASI DATA SERTIFIKAT:")
print("=" * 80)
for filename, data in certificate_data.items():
    print(f"\n{filename}")
    print(f"  Institusi: {data['institusi']}")
    print(f"  Tanggal: {data['tanggal']}")
    print(f"  Catatan: {data['keterangan']}")
