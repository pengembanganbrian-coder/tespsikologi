import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pertanyaan import SOAL_DISC
from scoring import MAPPING_MOST, MAPPING_LEAST

st.set_page_config(page_title="Tes DISC Online", layout="wide")

st.title("Sistem Analisis DISC Digital")

# --- Identitas ---
with st.sidebar:
    st.header("Profil Peserta")
    nama = st.text_input("Nama")
    jabatan = st.text_input("Jabatan")

# --- Tampilan Soal ---
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

if st.button("PROSES HASIL TES", type="primary"):
    # 1. Hitung Raw Score
    raw_most = {"D": 0, "I": 0, "S": 0, "C": 0}
    raw_least = {"D": 0, "I": 0, "S": 0, "C": 0}

    for i, ans in enumerate(jawaban_user):
        kotak_num = i + 1
        m_char = MAPPING_MOST[kotak_num][ans['M']]
        l_char = MAPPING_LEAST[kotak_num][ans['L']]
        
        if m_char in raw_most: raw_most[m_char] += 1
        if l_char in raw_least: raw_least[l_char] += 1

    # 2. Hitung Change Score
    raw_change = {k: raw_most[k] - raw_least[k] for k in raw_most}

    # 3. Tampilkan Hasil
    st.success(f"Analisis Selesai untuk {nama}")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.write("**Grafik 1 (Most)**")
        st.line_chart(pd.DataFrame(raw_most.items(), columns=['X', 'Y']).set_index('X'))

    with col_b:
        st.write("**Grafik 2 (Least)**")
        st.line_chart(pd.DataFrame(raw_least.items(), columns=['X', 'Y']).set_index('X'))

    with col_c:
        st.write("**Grafik 3 (Change)**")
        st.line_chart(pd.DataFrame(raw_change.items(), columns=['X', 'Y']).set_index('X'))

    st.info("Catatan: Skor di atas adalah skor mentah. Gunakan Tabel Norma untuk interpretasi mendalam.")
