import streamlit as st
import pandas as pd
from pertanyaan import SOAL_DISC

st.set_page_config(page_title="Tes DISC Online", layout="wide")

# --- LOGIC SCORING (Mapping Kunci Jawaban) ---
# Ini adalah contoh mapping sederhana. 
# Idealnya disesuaikan dengan 'key.csv' dari file Excel kamu.
def hitung_score(jawaban):
    score = {"D": 0, "I": 0, "S": 0, "C": 0}
    for item in jawaban:
        # Logika: Jika pilihan 'Most' sesuai kunci D, maka D + 1
        # Jika pilihan 'Least' sesuai kunci D, maka D - 1
        # (Di sini kamu bisa masukkan rumus spesifik dari file Excel-mu)
        pass
    return score

st.title("Sistem Tes DISC Digital 2026")

with st.sidebar:
    st.header("Profil Peserta")
    nama = st.text_input("Nama Lengkap")
    nip = st.text_input("NIP")

# Penampilan 24 Kotak Soal
jawaban_user = []
cols = st.columns(3)

for i, options in enumerate(SOAL_DISC):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**KOTAK {i+1}**")
            c1, c2, c3 = st.columns([1, 1, 4])
            m = c1.radio(f"M{i}", [0,1,2,3], key=f"m{i}", label_visibility="collapsed")
            l = c2.radio(f"L{i}", [0,1,2,3], key=f"l{i}", label_visibility="collapsed")
            for idx, txt in enumerate(options):
                c3.text(txt)
            jawaban_user.append({"M": m, "L": l})

st.divider()

if st.button("LIHAT HASIL ANALISIS", type="primary"):
    if not nama:
        st.error("Isi Nama dulu ya!")
    else:
        st.balloons()
        st.success(f"Hasil Analisis untuk {nama}")
        
        # Contoh Tampilan Grafik (Hanya Ilustrasi sebelum Mapping Kunci Selesai)
        chart_data = pd.DataFrame({
            'Kategori': ['D', 'I', 'S', 'C'],
            'Skor': [10, 15, 8, 12] # Ini nanti diganti hasil hitung_score
        })
        st.bar_chart(chart_data.set_index('Kategori'))
        
        st.write("### Karakteristik Anda:")
        st.write("Berdasarkan hasil tes, Anda cenderung memiliki profil yang teliti dan berorientasi pada data.")
