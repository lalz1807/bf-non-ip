# bf-non-ip

# Simple Brute Force Tool (Non-IP Based)

Tool ini digunakan untuk melakukan brute force login pada aplikasi web atau API tanpa menggunakan metode berbasis IP.

## Fitur
- Mencoba kombinasi username dan password dari file teks.
- Tidak menggunakan IP tracking atau blocking.
- Mudah dikonfigurasi untuk berbagai form login.

## Cara Menggunakan

1. Siapkan file `usernames.txt` dan `passwords.txt` yang berisi daftar username dan password yang ingin diuji, satu per baris.

2. Sesuaikan variabel di bagian bawah script `bf.py`:
   - `target_url`: URL endpoint login.
   - `user_field`: Nama field username pada form login.
   - `pass_field`: Nama field password pada form login.
   - `success_text`: Teks yang muncul di halaman jika login berhasil (digunakan untuk mendeteksi keberhasilan).

3. Pastikan Anda sudah menginstall dependencies:
   - pip install requests
  
4. Jalankan script dengan Python 3:
   - python3 bf.py

5. Script akan mencoba semua kombinasi username dan password dan menampilkan hasilnya.

## Catatan
- Pastikan Anda memiliki izin eksplisit untuk melakukan pengujian ini.
- Gunakan tool ini secara etis dan bertanggung jawab.
