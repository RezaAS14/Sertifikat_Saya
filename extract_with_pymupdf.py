import fitz  # PyMuPDF
from PIL import Image
import io

files = {
    'Sertifikat Bug Hunt Ahmad Reza Aulia Siregar_tte.pdf': 'Sertifikat_Apresiasi/Sertifikat Bug Hunt Ahmad Reza Aulia Siregar_tte.pdf',
    'SERTIFIKAT-APRESIASI-BUG-HUNTER-9.Ahmad-Reza.pdf': 'Sertifikat_Apresiasi/SERTIFIKAT-APRESIASI-BUG-HUNTER-9.Ahmad-Reza.pdf',
    '432544605dc6fb61320d064fb2ce0715-3.pdf': 'Sertifikat_Apresiasi/432544605dc6fb61320d064fb2ce0715-3.pdf'
}

print("Ekstrak teks dan gambar dari PDF menggunakan PyMuPDF...")
print("=" * 80)

for filename, filepath in files.items():
    print(f"\n📄 FILE: {filename}")
    print("-" * 80)
    
    try:
        doc = fitz.open(filepath)
        page = doc[0]  # First page
        
        # Extract text dengan berbagai metode
        print("\n🔍 METODE 1 - Text Extraction (Normal):")
        text = page.get_text()
        if text.strip():
            print(text[:500])
        else:
            print("   [Tidak ada teks yang bisa diekstrak]")
        
        # Extract text blocks
        print("\n🔍 METODE 2 - Text Blocks:")
        blocks = page.get_text("blocks")
        if blocks:
            for block in blocks[:5]:  # Show first 5 blocks
                if len(block) >= 5:
                    print(f"   {block[4]}")
        else:
            print("   [Tidak ada text blocks]")
        
        # Extract text dengan dict untuk mendapat detail
        print("\n🔍 METODE 3 - Detailed Text (dict):")
        text_dict = page.get_text("dict")
        if text_dict and "blocks" in text_dict:
            for block in text_dict["blocks"][:3]:
                if "lines" in block:
                    for line in block["lines"]:
                        if "spans" in line:
                            for span in line["spans"]:
                                if "text" in span and span["text"].strip():
                                    print(f"   {span['text']}")
        
        # Extract images from PDF
        print("\n🖼️  METODE 4 - Images in PDF:")
        image_list = page.get_images()
        if image_list:
            print(f"   Ditemukan {len(image_list)} gambar dalam PDF")
            for img_index, img in enumerate(image_list[:2]):  # Process first 2 images
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                
                # Save image for manual inspection
                output_filename = f"extracted_{filename.replace('.pdf', '')}_{img_index}.png"
                with open(output_filename, "wb") as img_file:
                    img_file.write(image_bytes)
                print(f"   ✓ Gambar disimpan: {output_filename}")
        else:
            print("   [Tidak ada gambar terpisah, kemungkinan seluruh halaman adalah gambar]")
        
        # Render page as image
        print("\n🎨 METODE 5 - Render halaman sebagai gambar:")
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom
        output_img = f"rendered_{filename.replace('.pdf', '.png')}"
        pix.save(output_img)
        print(f"   ✓ Halaman di-render: {output_img}")
        print(f"   Ukuran: {pix.width}x{pix.height} pixels")
        
        doc.close()
        
    except Exception as e:
        print(f"   ❌ ERROR: {e}")

print("\n" + "=" * 80)
print("✓ Selesai! Cek file gambar yang sudah diekstrak")
print("  Untuk membaca isi sertifikat, buka file PNG yang sudah dibuat")
