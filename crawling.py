import requests
from bs4 import BeautifulSoup
import base64
import urllib3
import os

# Mengabaikan peringatan SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Loop untuk setiap mahasiswa
for i in range(1, 130):  # Mengambil 3 digit terakhir nomor NIM
    # Nama file gambar
    filename = f"KARTU UTS MAHASISWA INFORMATIKA/112410{i:03d}.png"
    
    # Cek jika file sudah ada
    if os.path.exists(filename):
        print(f"Gambar untuk NIM 112410{i:03d} sudah ada, melewati pengambilan gambar.")
        continue  # Loncat ke iterasi berikutnya jika gambar sudah ada

    # URL halaman
    url = f'https://sisfo.unisla.ac.id/kartu-ujian/index.php?nk=202411112410{i:03d}'
    
    # Ambil konten halaman
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Temukan tag <img> dengan id tertentu
    img_tag = soup.find('img', {'id': 'output'})
    
    if img_tag:
        # Ambil data base64
        img_data = img_tag['src']
        
        # Hapus prefix data:image/png;base64,
        img_base64 = img_data.split(",")[1]
        
        # Dekode dan simpan sebagai file gambar
        with open(filename, "wb") as f:
            f.write(base64.b64decode(img_base64))
        print(f"Gambar berhasil disimpan sebagai '{filename}'")
    else:
        print(f"Gambar tidak ditemukan di halaman untuk NIM 112410{i:03d}.")

# Dokumentasi:
# Script ini bertujuan untuk mengunduh dan menyimpan gambar kartu UTS mahasiswa dari situs web tertentu.
# 
# Penjelasan tiap bagian:
# 1. `import requests, BeautifulSoup, base64, urllib3, os`: Mengimpor modul yang dibutuhkan untuk HTTP request, parsing HTML, decoding base64, dan operasi file.
# 2. `urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)`: Menonaktifkan peringatan SSL yang muncul karena verifikasi sertifikat dinonaktifkan.
# 3. `for i in range(1, 130)`: Loop untuk iterasi NIM mahasiswa, dimulai dari 1 hingga 129.
# 4. `filename = f"KARTU UTS MAHASISWA INFORMATIKA/112410{i:03d}.png"`: Membuat nama file gambar berdasarkan NIM mahasiswa.
# 5. `if os.path.exists(filename)`: Mengecek apakah file gambar sudah ada. Jika ada, script akan melewati pengambilan gambar untuk NIM tersebut.
# 6. `url = f'https://sisfo.unisla.ac.id/kartu-ujian/index.php?nk=202411112410{i:03d}'`: Membentuk URL untuk halaman kartu ujian mahasiswa.
# 7. `response = requests.get(url, verify=False)`: Mengambil konten halaman dengan mengabaikan verifikasi SSL.
# 8. `soup.find('img', {'id': 'output'})`: Mencari elemen gambar dengan atribut id 'output' di dalam halaman HTML.
# 9. `img_base64 = img_data.split(",")[1]`: Membersihkan data base64 dari prefix yang tidak diperlukan.
# 10. `with open(filename, "wb") as f`: Membuka file dalam mode biner untuk menulis data gambar yang sudah didekode.
# 11. `base64.b64decode(img_base64)`: Mendekode data base64 menjadi format biner.
# 12. Menyimpan file gambar ke dalam direktori yang ditentukan dan mencetak pesan konfirmasi.
# 13. Jika tag gambar tidak ditemukan, mencetak pesan bahwa gambar tidak ditemukan untuk NIM tersebut.
