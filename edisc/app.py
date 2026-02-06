import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pertanyaan import SOAL_DISC
import scoring

st.set_page_config(page_title="DISC DJBC 2026", layout="wide")

# Tambahkan CSS agar tampilan lebih bersih
st.markdown("""
    <style>
    .stRadio [role=radiogroup]{flex-direction:row;}
    .st-expander {border: 1px solid #e6e6e6; margin-bottom: 10px;}
    </style>
    """, unsafe_allow_html=True)

st.title("Sistem Analisis DISC - DJBC 2026")

# Identitas
with st.sidebar:
    st.header("Profil Peserta")
    nama = st.text_input("Nama Lengkap")
    nip = st.text_input("NIP")
    st.divider()
    st.info("Pastikan setiap kotak diisi 1 Most dan 1 Least.")

# Form Soal
jawaban = []
cols = st.columns(3)

for i, kotak in enumerate(SOAL_DISC):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**KOTAK {i+1}**")
            c1, c2, c3 = st.columns([1, 1, 5])
            c1.caption("M")
            c2.caption("L")
            
            m_res = c1.radio(f"M{i}", [0,1,2,3], key=f"m_{i}", label_visibility="collapsed")
            l_res = c2.radio(f"L{i}", [0,1,2,3], key=f"l_{i}", label_visibility="collapsed")
            
            for idx, teks in enumerate(kotak):
                c3.text(teks)
            
            if m_res == l_res:
                st.error("M & L tidak boleh sama!")
            
            jawaban.append({"M": m_res, "L": l_res})

st.divider()

if st.button("HITUNG HASIL & TAMPILKAN GRAFIK", type="primary"):
    if not nama:
        st.warning("Mohon isi Nama Lengkap di sidebar kiri.")
    else:
        # Hitung Raw Score
        res_m = {"D":0, "I":0, "S":0, "C":0}
        res_l = {"D":0, "I":0, "S":0, "C":0}
        
        for idx, val in enumerate(jawaban):
            k = idx + 1
            # Ambil mapping dari scoring.py
            char_m = scoring.MAPPING_MOST[k][val['M']]
            char_l = scoring.MAPPING_LEAST[k][val['L']]
            
            if char_m in res_m: res_m[char_m] += 1
            if char_l in res_l: res_l[char_l] += 1

        # Tampilkan Grafik
        st.success(f"Analisis DISC untuk: {nama}")
        
        # Grafik Sederhana menggunakan Matplotlib
        fig, ax = plt.subplots(figsize=(10, 5))
        cats = ['D', 'I', 'S', 'C']
        vals = [res_m[c] for c in cats]
        
        ax.plot(cats, vals, marker='o', linestyle='-', color='#1f77b4', linewidth=3)
        ax.set_ylim(0, 24)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_title("Grafik 1 (MOST)")
        
        st.pyplot(fig)
        
        # Tampilkan Skor Mentah
        st.write("Skor Mentah (Most):", res_m)
