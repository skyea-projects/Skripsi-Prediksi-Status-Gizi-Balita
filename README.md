# Prediksi Status Gizi Balita dengan Streamlit

Aplikasi Streamlit ini bertujuan untuk memprediksi **status gizi balita** berdasarkan data **usia**, **berat badan**, dan **tinggi badan**. Prediksi dilakukan menggunakan model **Logistic Regression** yang telah dioptimasi, dan data input akan melalui proses normalisasi sebelum diproses oleh model.

## Fitur Aplikasi

1. **Input Data Manual**: 
   - Pengguna dapat memasukkan data balita berupa:
     - **Usia (bulan)**
     - **Berat badan (kg)**
     - **Tinggi badan (cm)**
   - Setelah data dimasukkan, aplikasi akan memberikan prediksi status gizi balita.

2. **Prediksi Status Gizi**:
   - Model akan mengklasifikasikan status gizi balita ke dalam salah satu kategori berikut:
     - Gizi Buruk
     - Gizi Kurang
     - Normal
     - Beresiko Gizi Lebih
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
   - Anda juga bisa mengakses aplikasi ini secara online melalui Streamlit Sharing. Klik [di sini](https://share.streamlit.io/username/repository-name/main/app.py) untuk mencoba.

## Struktur File

