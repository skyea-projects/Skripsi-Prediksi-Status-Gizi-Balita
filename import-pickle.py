import streamlit as st
import pickle
import pandas as pd

# Memuat model dan scaler dari file pickle
with open("best_model.pkl", "rb") as f:
    best_model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Mapping label numerik ke nama status gizi
status_gizi_mapping = {
    1: "Gizi Buruk",
    2: "Gizi Kurang",
    3: "Normal",
    4: "Beresiko Gizi Lebih",
    5: "Gizi Lebih",
    6: "Obesitas",
}

# Judul aplikasi
st.title("Prediksi Status Gizi Balita")

# Input data oleh pengguna
usia = st.number_input("Input Usia dalam bulan (contoh: 24)", min_value=1, step=1)
berat = st.number_input(
    "Input Berat badan dalam kg (contoh: 12.5)", min_value=0.1, format="%.1f"
)
tinggi = st.number_input(
    "Input Tinggi badan dalam cm (contoh: 85.0)", min_value=0.1, format="%.1f"
)

# Tombol untuk melakukan prediksi
if st.button("Prediksi Status Gizi"):
    if usia > 0 and berat > 0 and tinggi > 0:
        # Buat DataFrame untuk data yang dimasukkan
        new_data = pd.DataFrame({"usia": [usia], "berat": [berat], "tinggi": [tinggi]})

        # Normalisasi data menggunakan scaler
        new_data_normalized = scaler.transform(new_data)

        # Prediksi menggunakan model
        predictions = best_model.predict(new_data_normalized)

        # Mapping hasil prediksi
        predicted_label = status_gizi_mapping.get(predictions[0], "Unknown")

        # Menampilkan hasil prediksi
        st.write(f"Prediksi status gizi: {predicted_label}")
    else:
        st.error("Semua input harus lebih besar dari 0!")
