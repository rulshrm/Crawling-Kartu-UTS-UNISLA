<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>Crawler Data Kartu Peserta UTS UNISLA</h1>

<p>Crawler berbasis Python ini bertujuan untuk mengambil data kartu peserta Ujian Tengah Semester (UTS) bagi mahasiswa program studi Teknik Informatika di UNISLA. Alat ini mengotomatisasi proses pengambilan gambar kartu peserta, sehingga memudahkan dalam pengumpulan data secara efisien.</p>

<h2>Daftar Isi</h2>
<ul>
    <li><a href="#ikhtisar-proyek">Ikhtisar Proyek</a></li>
    <li><a href="#fitur">Fitur</a></li>
    <li><a href="#instalasi">Instalasi</a></li>
    <li><a href="#penggunaan">Penggunaan</a></li>
    <li><a href="#konfigurasi">Konfigurasi</a></li>
    <li><a href="#persyaratan">Persyaratan</a></li>
    <li><a href="#kontribusi">Kontribusi</a></li>
    <li><a href="#lisensi">Lisensi</a></li>
</ul>

<h2 id="ikhtisar-proyek">Ikhtisar Proyek</h2>
<p>Script <code>crawling.py</code> ini dirancang untuk mengumpulkan dan menyimpan gambar kartu peserta UTS bagi mahasiswa Teknik Informatika di UNISLA. Dengan menerapkan teknik web scraping, alat ini menyederhanakan proses pengumpulan data dan mengurangi pekerjaan manual.</p>

<h2 id="fitur">Fitur</h2>
<ul>
    <li><strong>Crawling data otomatis</strong>: Mengambil gambar kartu peserta berdasarkan NIM dengan cepat.</li>
    <li><strong>Penyimpanan Data</strong>: Menyimpan gambar yang diambil dalam folder bernama <code>KARTU UTS MAHASISWA INFORMATIKA</code> dalam format <code>.png</code>.</li>
    <li><strong>Pengecekan File</strong>: Menghindari pengambilan data ulang jika file gambar sudah ada.</li>
</ul>

<h2 id="instalasi">Instalasi</h2>
<p>Untuk memulai, klon repositori ini dan pastikan semua dependensi yang diperlukan telah terpasang:</p>
<pre><code>git clone https://github.com/username-anda/Crawling-Kartu-UTS-UNISLA.git
cd Crawling-Kartu-UTS-UNISLA
pip install -r requirements.txt
</code></pre>
<p><strong>Catatan</strong>: Pastikan Anda menggunakan Python versi 3.8 atau yang lebih baru.</p>

<h2 id="penggunaan">Penggunaan</h2>
<p>Jalankan script <code>crawling.py</code> untuk memulai proses pengumpulan data:</p>
<pre><code>python crawling.py
</code></pre>
<p>Script ini akan menjalankan crawler, yang mengumpulkan gambar kartu peserta yang diperlukan. Gambar akan disimpan dalam folder <code>KARTU UTS MAHASISWA INFORMATIKA</code>.</p>

<h2 id="konfigurasi">Konfigurasi</h2>
<p>Perbarui pengaturan konfigurasi (seperti URL atau jalur penyimpanan) secara langsung di file <code>crawling.py</code> atau buat file konfigurasi terpisah jika diperlukan.</p>

<h2 id="persyaratan">Persyaratan</h2>
<p>Proyek ini memerlukan pustaka berikut:</p>
<ul>
    <li><code>requests</code></li>
    <li><code>beautifulsoup4</code></li>
    <li><code>urllib3</code></li>
</ul>
<p>Untuk menginstal pustaka-pustaka tersebut, gunakan perintah:</p>
<pre><code>pip install requests beautifulsoup4 urllib3
</code></pre>

<h2 id="kontribusi">Kontribusi</h2>
<p>Kontribusi sangat dihargai! Silakan fork repositori ini dan ajukan pull request untuk perbaikan, penyempurnaan bug, atau penambahan fitur lainnya.</p>

<h2 id="lisensi">Lisensi</h2>
<p>Proyek ini dilisensikan di bawah Lisensi MIT - lihat file <a href="LICENSE">LICENSE</a> untuk informasi lebih lanjut.</p>

</body>
</html>
