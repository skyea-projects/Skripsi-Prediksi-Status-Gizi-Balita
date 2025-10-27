import streamlit as st
import joblib
import numpy as np

# Load model
model_l_bb_u = joblib.load("2model_bb_u_L.pkl")
model_l_tb_u = joblib.load("2model_tb_u_L.pkl")
model_l_bb_tb = joblib.load("2model_bb_tb_L.pkl")

model_p_bb_u = joblib.load("2model_bb_u_P.pkl")
model_p_tb_u = joblib.load("2model_tb_u_P.pkl")
model_p_bb_tb = joblib.load("2model_bb_tb_P.pkl")

# Load scaler
scaler = joblib.load("minmax_scaler.pkl")

# Label mapping
label_map = {
    'bb_u': {
        1: "Berat Badan Sangat Kurang",
        2: "Berat Badan Kurang",
        3: "Berat Badan Normal",
        4: "Risiko Gizi Lebih"
    },
    'tb_u': {
        1: "Sangat Pendek",
        2: "Pendek",
        3: "Normal",
        4: "Tinggi"
    },
    'bb_tb': {
        1: "Gizi Buruk",
        2: "Gizi Kurang",
        3: "Gizi Normal",
        4: "Beresiko Gizi Lebih",
        5: "Gizi Lebih",
        6: "Obesitas"
    }
}

# ------------------- #
#       Layout UI     #
# ------------------- #

st.set_page_config(page_title="Prediksi Gizi Balita", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Prediksi Status Gizi Balita</h1>", unsafe_allow_html=True)
st.markdown("---")

with st.expander("ℹ️ Tentang Aplikasi", expanded=True):
    st.write("""
        Aplikasi ini digunakan untuk memprediksi status gizi balita untuk usia 11-59 bulan berdasarkan input data antropometri seperti usia, berat badan, tinggi badan, 
        lingkar lengan atas (LiLA), dan lingkar kepala (LiPA). Model prediksi dibedakan berdasarkan jenis kelamin balita.
    """)

st.markdown("## Input Data Balita")

# Pilih Jenis Kelamin
jenis_kelamin = st.radio("Pilih Jenis Kelamin:", ("Laki-laki", "Perempuan"), horizontal=True)

# Input Form
col1, col2 = st.columns(2)
with col1:
    usia = st.number_input("Usia (bulan)", min_value=1, step=1)
    berat = st.number_input("Berat Badan (kg)", min_value=0.1, format="%.1f")
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=0.1, format="%.1f")
with col2:
    lila = st.number_input("Lingkar Lengan Atas (cm)", min_value=0.1, format="%.1f")
    lipa = st.number_input("Lingkar Kepala (cm)", min_value=0.1, format="%.1f")

st.markdown("")

if st.button("🔍 Prediksi Status Gizi"):
    input_data = np.array([[usia, berat, tinggi, lila, lipa]])
    input_scaled = scaler.transform(input_data)

    if jenis_kelamin == "Laki-laki":
        pred_bb_u = model_l_bb_u.predict(input_scaled)[0]
        pred_tb_u = model_l_tb_u.predict(input_scaled)[0]
        pred_bb_tb = model_l_bb_tb.predict(input_scaled)[0]
    else:
        pred_bb_u = model_p_bb_u.predict(input_scaled)[0]
        pred_tb_u = model_p_tb_u.predict(input_scaled)[0]
        pred_bb_tb = model_p_bb_tb.predict(input_scaled)[0]

    # Hasil
    st.success("✅ Prediksi berhasil!")
    st.markdown("## 📈 Hasil Prediksi Status Gizi:")
    
    st.info(f"**BB/U** : {label_map['bb_u'].get(pred_bb_u)}  ")
    st.info(f"**TB/U** : {label_map['tb_u'].get(pred_tb_u)}  ")
    st.info(f"**BB/TB** : {label_map['bb_tb'].get(pred_bb_tb)}  ")
else:
    st.markdown("👉 Masukkan data balita terlebih dahulu, lalu klik tombol **Prediksi Status Gizi** di atas.")
