import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- PENGECEKAN FILE ---
try:
    from pertanyaan import SOAL_DISC
    from scoring import MAPPING_MOST, MAPPING_LEAST
except ImportError:
    st.error("❌ File 'pertanyaan.py' atau 'scoring.py' tidak ditemukan di GitHub kamu!")
    st.stop()

st.set_page_config(page_title="Tes DISC Online", layout="wide")

st.title("Lembar Kerja Tes DISC")

# Identitas
with st.sidebar:
    st.header("Profil Peserta")
    nama = st.text_input("Nama Lengkap")
    nip = st.text_input("NIP")

# Form Soal (24 Kotak)
jawaban_user = []
cols = st.columns(3)

for i, options in enumerate(SOAL_DISC):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**KOTAK {i+1}**")
            c1, c2, c3 = st.columns([1, 1, 5])
            m = c1.radio(f"M{i}", [0,1,2,3], key=f"m{i}", label_visibility="collapsed")
            l = c2.radio(f"L{i}", [0,1,2,3], key=f"l{i}", label_visibility="collapsed")
            for idx, txt in enumerate(options):
                c3.text(txt)
            jawaban_user.append({"M": m, "L": l})

st.divider()

if st.button("PROSES & LIHAT GRAFIK", type="primary"):
    if not nama:
        st.warning("Silakan isi nama terlebih dahulu.")
    else:
        # Perhitungan Skor Mentah
        most_score = {"D":0, "I":0, "S":0, "C":0}
        least_score = {"D":0, "I":0, "S":0, "C":0}
        
        for i, ans in enumerate(jawaban_user):
            kotak = i + 1
            # Ambil karakter berdasarkan kunci dari scoring.py
            char_m = MAPPING_MOST[kotak][ans['M']]
            char_l = MAPPING_LEAST[kotak][ans['L']]
            
            if char_m in most_score: most_score[char_m] += 1
            if char_l in least_score: least_score[char_l] += 1
            
        st.success(f"Analisis Selesai untuk: {nama}")
        
        # Tampilan Grafik
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.write("### Grafik 1 (Most)")
            st.line_chart(pd.DataFrame(most_score.items(), columns=['X', 'Y']).set_index('X'))
            
        with col_right:
            st.write("### Grafik 2 (Least)")
            st.line_chart(pd.DataFrame(least_score.items(), columns=['X', 'Y']).set_index('X'))
