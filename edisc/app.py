import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Memanggil data soal dan kunci
try:
    from pertanyaan import SOAL_DISC
    import scoring
except ImportError:
    st.error("Gagal memuat file pendukung. Pastikan 'pertanyaan.py' dan 'scoring.py' ada di GitHub.")
    st.stop()

st.set_page_config(page_title="DISC DJBC 2026", layout="wide")

st.title("Sistem Analisis DISC Digital")

# Sidebar Identitas
with st.sidebar:
    st.header("Identitas")
    nama = st.text_input("Nama Lengkap")
    nip = st.text_input("NIP")

# Form Input Soal
jawaban = []
cols = st.columns(3)
for i, kotak in enumerate(SOAL_DISC):
    with cols[i % 3]:
        with st.container(border=True):
            st.write(f"**KOTAK {i+1}**")
            c1, c2, c3 = st.columns([1, 1, 4])
            m = c1.radio(f"M{i}", [0, 1, 2, 3], key=f"m{i}", label_visibility="collapsed")
            l = c2.radio(f"L{i}", [0, 1, 2, 3], key=f"l{i}", label_visibility="collapsed")
            for txt in kotak:
                c3.text(txt)
            jawaban.append({'M': m, 'L': l})

# Tombol Proses
if st.button("HITUNG HASIL", type="primary"):
    if not nama:
        st.error("Mohon isi Nama Pegawai di sidebar.")
    else:
        # Proses Hitung Skor Mentah
        skor_m = {"D": 0, "I": 0, "S": 0, "C": 0}
        for idx, ans in enumerate(jawaban):
            kotak_num = idx + 1
            res = scoring.MAPPING_MOST[kotak_num][ans['M']]
            if res in skor_m: skor_m[res] += 1
        
        # Tampilan Grafik
        st.subheader(f"Hasil Analisis: {nama}")
        
        fig, ax = plt.subplots(figsize=(8, 4))
        kategori = ['D', 'I', 'S', 'C']
        nilai = [skor_m[k] for k in kategori]
        
        ax.plot(kategori, nilai, marker='o', color='blue', linewidth=2)
        ax.set_ylim(0, 24)
        ax.set_title("Grafik 1 (Most)")
        ax.grid(True, linestyle='--', alpha=0.6)
        
        st.pyplot(fig)
        st.success("Analisis berhasil ditampilkan!")
