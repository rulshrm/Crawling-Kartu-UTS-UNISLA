import requests
from bs4 import BeautifulSoup
import base64
import urllib3
import os

# Mengabaikan peringatan SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Loop untuk setiap mahasiswa
for i in range(1, 130): # Mengambil 3 digit terakhir nomor NIM
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
