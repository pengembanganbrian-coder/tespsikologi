import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data soal & kunci
try:
    from pertanyaan import SOAL_DISC
    import scoring
except Exception as e:
    st.error(f"Gagal memuat file: {e}. Pastikan scoring.py dan pertanyaan.py sudah di-upload ke GitHub.")
    st.stop()

st.set_page_config(page_title="Tes DISC DJBC", layout="wide")

st.title("Sistem Analisis DISC Digital")

# Sidebar
with st.sidebar:
    st.header("Identitas")
    nama = st.text_input("Nama Lengkap")
    nip = st.text_input("NIP")

# Form 24 Kotak
jawaban = []
cols = st.columns(3)
for i, kotak in enumerate(SOAL_DISC):
    with cols[i % 3]:
        with st.container(border=True):
            st.write(f"**KOTAK {i+1}**")
            c1, c2, c3 = st.columns([1, 1, 4])
            m = c1.radio(f"M{i}", [0, 1, 2, 3], key=f"m{i}", label_visibility="collapsed")
            l = c2.radio(f"L{i}", [0, 1, 2, 3], key=f"l{i}", label_visibility="collapsed")
            for t in kotak: c3.text(t)
            jawaban.append({'M': m, 'L': l})

if st.button("HITUNG SKOR & GRAFIK", type="primary"):
    if not nama:
        st.error("Nama tidak boleh kosong!")
    else:
        # Hitung Raw Score
        res_m = {"D":0, "I":0, "S":0, "C":0}
        for idx, val in enumerate(jawaban):
            kotak_id = idx + 1
            char = scoring.MAPPING_MOST[kotak_id][val['M']]
            if char in res_m: res_m[char] += 1
        
        st.success(f"Berhasil! Hasil untuk {nama}:")
        
        # Gambar Grafik Garis (Matplotlib)
        fig, ax = plt.subplots(figsize=(8, 4))
        kat = ['D', 'I', 'S', 'C']
        nilai = [res_m[k] for k in kat]
        
        ax.plot(kat, nilai, marker='o', linestyle='-', color='blue', linewidth=2)
        ax.set_ylim(0, 24)
        ax.grid(True, alpha=0.3)
        ax.set_title("Grafik 1 (Most)")
        
        st.pyplot(fig)
