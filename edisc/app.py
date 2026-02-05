import streamlit as st
from pertanyaan import SOAL_DISC

st.set_page_config(page_title="Tes DISC Online", layout="wide")

# Header dan Identitas
st.title("Lembar Kerja Tes DISC")
st.info("Instruksi: Pilih satu 'M' (Paling Mirip) dan satu 'L' (Paling Tidak Mirip) untuk setiap kotak.")

with st.sidebar:
    st.header("Data Peserta")
    nama = st.text_input("Nama Lengkap")
    nip = st.text_input("NIP / ID")
    jabatan = st.text_input("Jabatan")

# Tempat menyimpan pilihan user
data_jawaban = []

# Tampilan Grid Soal (3 Kolom)
cols = st.columns(3)

for i, options in enumerate(SOAL_DISC):
    # Bagi kotak soal ke 3 kolom agar rapi
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**KOTAK {i+1}**")
            
            # Header kecil
            h_col1, h_col2, h_col3 = st.columns([1, 1, 4])
            h_col1.write("**M**")
            h_col2.write("**L**")
            h_col3.write("**Pernyataan**")
            
            # Pilihan User
            m_val = h_col1.radio(f"M{i}", [0,1,2,3], key=f"m{i}", label_visibility="collapsed")
            l_val = h_col2.radio(f"L{i}", [0,1,2,3], key=f"l{i}", label_visibility="collapsed")
            
            # Teks Pernyataan
            for idx, text in enumerate(options):
                h_col3.text(text)
            
            # Validasi
            if m_val == l_val:
                st.error("M & L tidak boleh sama!")
            
            data_jawaban.append({"kotak": i+1, "most": options[m_val], "least": options[l_val]})

st.divider()

if st.button("KIRIM JAWABAN", type="primary"):
    if not nama:
        st.warning("Mohon isi Nama Lengkap terlebih dahulu.")
    else:
        st.balloons()
        st.success(f"Terima kasih {nama}, jawaban Anda berhasil direkam!")
        # Di sini nantinya kita masukkan rumus hitung D, I, S, C
        st.write("Data Anda:", data_jawaban)
