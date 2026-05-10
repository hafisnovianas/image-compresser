from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener

class ImgCompressor():
    def __init__(self):
        register_heif_opener() # Wajib: Daftarkan ekstensi HEIC agar bisa dibaca oleh Pillow

    def file(self, input_path, max_ukuran=1920, kualitas=80):
        path_absolut = Path(input_path).resolve()
        folder_sumber = path_absolut.parent
        
        nama_file_asli = path_absolut.stem        
        output_path = folder_sumber / f"{nama_file_asli}_kompres.webp"

        try:
            with Image.open(input_path) as img:
                # Pastikan format warna sesuai
                if img.mode not in ('RGB', 'RGBA'):
                    img = img.convert('RGBA')

                # Perkecil resolusi jika ukurannya terlalu besar
                lebar, tinggi = img.size
                if max(lebar, tinggi) > max_ukuran:
                    rasio = max_ukuran / max(lebar, tinggi)
                    ukuran_baru = (int(lebar * rasio), int(tinggi * rasio))
                    # Menggunakan LANCZOS untuk hasil resize terbaik
                    img = img.resize(ukuran_baru, Image.Resampling.LANCZOS)

                # Simpan gambar ke format WebP di folder yang sama
                img.save(output_path, 'webp', optimize=True, quality=kualitas)
                print(f"✅ Berhasil!")
                print(f"📁 File asli: {path_absolut}")
                print(f"📁 File baru: {output_path}")

        except FileNotFoundError:
            print(f"❌ Error: File '{input_path}' tidak ditemukan. Pastikan namanya/path-nya benar.")
        except Exception as e:
            print(f"❌ Terjadi kesalahan: {e}")

    def folder(self, folder_input, ukuran_target=600):
        folder_path = Path(folder_input)
        for file in folder_path.iterdir():
            if file.is_file() and file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.heic']:
                if "_kompres" not in file.stem:
                    self.file(str(file), max_ukuran=ukuran_target)