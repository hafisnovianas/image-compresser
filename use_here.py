# ==============================================================================
# SOP DIMENSI & UKURAN FILE GAMBAR WEBSITE (STANDAR INDUSTRI)
# ==============================================================================

# 1. HERO IMAGE / SPANDUK UTAMA (FULL WIDTH)
#    - Fungsi       : Gambar latar belakang penuh atau ilustrasi raksasa di atas web.
#    - Max-Width    : 1920px (Tinggi menyesuaikan proporsi)
#    - Target File  : Max 200 KB - 250 KB
#    - Format       : WebP (Kualitas 80-85%)

# 2. GAMBAR KONTEN / ARTIKEL (HALF/CONTENT WIDTH)
#    - Fungsi       : Gambar artikel, ilustrasi "Tentang Kami" (setengah layar).
#    - Max-Width    : 1200px (Atau minimal 800px jika wadah kotaknya kecil)
#    - Target File  : Max 80 KB - 100 KB
#    - Format       : WebP (Kualitas 80-85%)

# 3. THUMBNAIL / GRID / KARTU (COL-3 / COL-4)
#    - Fungsi       : Foto siswa, katalog produk, galeri (berjejer 3-4 menyamping).
#    - Max-Width    : 600px 
#    - Target File  : Max 30 KB - 50 KB
#    - Format       : WebP (Kualitas 80%)

# 4. LOGO MITRA / AVATAR KECIL / IKON
#    - Fungsi       : Logo di footer, foto profil bundar, testimoni wajah.
#    - Max-Width    : 200px (Biasanya rasio 1:1 atau 200x200px)
#    - Target File  : Max 10 KB - 20 KB
#    - Format       : WebP untuk foto (SVG jika vektor warna solid)

# ==============================================================================
# CONTOH VARIABEL KONFIGURASI (Bisa dipakai langsung di fungsi resize)
# ==============================================================================
from image_compressor import ImgCompressor

CONFIG = {
    "hero": {"max_width": 1920, "quality": 85},
    "dokumen1": {"max_width": 1200, "quality": 80},
    "dokumen2": {"max_width": 900, "quality": 80},
    "thumbnail1": {"max_width": 600, "quality": 80},
    "thumbnail2": {"max_width": 400, "quality": 80},
    "ikon": {"max_width": 200, "quality": 80}
}

folder_path = r"E:\DIJUMPER WEB\PROJECT\260621 - dahepelani\source\logobrand - Diedit.png"
config_name = "ikon" # Pilih salah satu: "hero", "dokumen1", "dokumen2", "thumbnail1", "thumbnail2", "ikon"

compressor = ImgCompressor()
compressor.process(folder_path, max_ukuran=CONFIG[config_name]["max_width"], kualitas=CONFIG[config_name]["quality"])