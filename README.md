# Prediksi Status Gizi Balita dengan Streamlit

Aplikasi Streamlit ini bertujuan untuk memprediksi **Status Gizi Balita** berdasarkan data **Jenis Kelamin**, **Usia**, **Berat Badan**, **Tinggi Badan**, **Lingkar Lengan Atas**, dan **Lingkar Kepala**. Prediksi dilakukan menggunakan model **Algoritma Logistic Regression** yang telah dioptimasi, dan data input akan melalui proses normalisasi sebelum diproses oleh model.

## Fitur Aplikasi

1. **Input Data Manual**: 
   - Pengguna dapat memasukkan data balita berupa:
     -**Jenis Kelamin (Laki-laki/Perempuan)**
     - **Usia (bulan)**
     - **Berat Badan (kg)**
     - **Tinggi Badan (cm)**
     - **Lingkar Lengan Atas (cm)**
     - **Lingkar Kepala (cm)**
   - Setelah data dimasukkan, aplikasi akan memberikan hasil prediksi status gizi balita.

2. **Prediksi Status Gizi**:
   Model akan mengklasifikasikan status gizi balita ke dalam 3 kategori, yaitu sebagai berikut:
   - BB/U
     - Berat Badan Sangat Kurang
     - Berat Badan Kurang
     - Berat Badan Normal
     - Risiko Lebih
   - TB/U
     - Sangat Pendek
     - Pendek
     - Normal
     - Tinggi
   - BB/TB
     - Gizi Buruk
     - Gizi Kurang
     - Gizi Normal/Baik
     - Berisiko Gizi Lebih
     - Gizi Lebih
     - Obesitas

3. **Tampilan Interaktif**:
   - Desain responsif dengan antarmuka yang sederhana dan ramah pengguna.

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman utama.
- **Streamlit**: Framework untuk membangun aplikasi berbasis web.
- **scikit-learn**: Untuk model machine learning dan preprocessing data.
- **Pickle**: Untuk menyimpan dan memuat model Logistic Regression dan scaler.

## Cara Menggunakan Aplikasi

1. **Jalankan Aplikasi Secara Lokal**:
   - Clone repository ini:
     ```bash
     git clone https://github.com/username/repository-name.git
     cd repository-name
     ```
   - Pastikan semua dependensi terinstal:
     ```bash
     pip install -r requirements.txt
     ```
   - Jalankan aplikasi Streamlit:
     ```bash
     streamlit run app.py
     ```
   - Aplikasi akan terbuka di browser pada URL `http://localhost:8501`.

2. **Gunakan Aplikasi yang Telah Dideploy**:
   - Anda juga bisa mengakses aplikasi ini secara online melalui Streamlit Sharing. Klik [di sini](https://prediksi-status-gizi.streamlit.app/) untuk mencoba.

## Struktur File

## Input dan Output

- **Input**:
  - **Jenis Kelamin (L/P)**: Jenis kelamin balita Laki-laki atau Perempuan.
  - **Usia (bulan)**: Usia balita dalam satuan bulan.
  - **Berat badan (kg)**: Berat badan balita dalam satuan kilogram.
  - **Tinggi badan (cm)**: Tinggi badan balita dalam satuan sentimeter.
  - **Lingkar Lengan Atas (cm)**: Lingkar lengan atas balita dalam satuan sentimeter.
  - **Lingkar Kepala (cm)**: Lingkar kepala balita dalam satuan sentimeter.

- **Output**:
  Hasil prediksi terbagi menjadi 3 kategori Status gizi, yaitu:
   - BB/U
     - Berat Badan Sangat Kurang
     - Berat Badan Kurang
     - Berat Badan Normal
     - Risiko Lebih
   - TB/U
     - Sangat Pendek
     - Pendek
     - Normal
     - Tinggi
   - BB/TB
     - Gizi Buruk
     - Gizi Kurang
     - Gizi Normal/Baik
     - Berisiko Gizi Lebih
     - Gizi Lebih
     - Obesitas

## Contoh Tampilan

1. **Input Data**:
   - Pengguna memasukkan data berupa jenis kelamin, usia, berat badan, dan tinggi badan, lingkar lengan atas, dan lingkar kepala balita.
2. **Hasil Prediksi**:
   - Sistem menampilkan hasil prediksi status gizi berdasarkan input data.

## Catatan

- Model ini dirancang untuk membantu tenaga kesehatan dalam memprediksi status gizi balita. Hasil prediksi hanya sebagai referensi awal dan tidak menggantikan diagnosis profesional.
- Pastikan data yang dimasukkan akurat untuk hasil prediksi yang optimal.

## Kontribusi

Jika Anda memiliki saran atau ingin berkontribusi, silakan ajukan **pull request** atau buka **issue** di repository ini.

