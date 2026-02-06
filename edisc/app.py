import streamlit as st
import pandas as pd

# =========================
# IMPORT DATA & SCORING
# =========================
try:
    from pertanyaan import SOAL_DISC
    from skoring import MAPPING_MOST, MAPPING_LEAST
except ImportError as e:
    st.error("❌ File pertanyaan.py atau skoring.py tidak ditemukan.")
    st.code(str(e))
    st.stop()

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Tes DISC Online",
    layout="wide"
)

st.title("🧠 Tes DISC Online")

# =========================
# SIDEBAR – IDENTITAS
# =========================
with st.sidebar:
    st.header("Profil Peserta")
    nama = st.text_input("Nama Lengkap")
    nip = st.text_input("NIP / ID Pegawai")

# =========================
# VALIDASI DATA
# =========================
if len(SOAL_DISC) != 24:
    st.error("❌ Jumlah kotak DISC harus 24.")
    st.stop()

# =========================
# INSTRUKSI
# =========================
st.info(
    "Pada setiap **kotak**, pilih:\n"
    "- **1 pernyataan PALING SESUAI (M)** dengan diri Anda\n"
    "- **1 pernyataan PALING TIDAK SESUAI (L)** dengan diri Anda"
)

# =========================
# FORM SOAL DISC (RAPI)
# =========================
jawaban_user = []
cols = st.columns(3)

for i, options in enumerate(SOAL_DISC):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"### Kotak {i+1}")

            m = st.radio(
                "Paling Sesuai (M)",
                options=range(4),
                format_func=lambda x: options[x],
                key=f"M_{i}"
            )

            l = st.radio(
                "Paling Tidak Sesuai (L)",
                options=range(4),
                format_func=lambda x: options[x],
                key=f"L_{i}"
            )

            jawaban_user.append({
                "M": m,
                "L": l
            })

st.divider()

# =========================
# PROSES & HASIL
# =========================
if st.button("📊 PROSES & LIHAT HASIL", type="primary"):

    if not nama:
        st.warning("⚠️ Nama wajib diisi.")
        st.stop()

    most_score = {"D": 0, "I": 0, "S": 0, "C": 0}
    least_score = {"D": 0, "I": 0, "S": 0, "C": 0}

    for i, ans in enumerate(jawaban_user):
        kotak = i + 1

        try:
            char_m = MAPPING_MOST[kotak][ans["M"]]
            char_l = MAPPING_LEAST[kotak][ans["L"]]
        except KeyError:
            st.error(f"❌ Mapping error pada kotak {kotak}")
            st.stop()

        most_score[char_m] += 1
        least_score[char_l] += 1

    st.success(f"✅ Analisis selesai untuk **{nama}**")

    # =========================
    # GRAFIK HASIL
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Grafik MOST")
        df_most = pd.DataFrame.from_dict(
            most_score, orient="index", columns=["Skor"]
        )
        st.bar_chart(df_most)

    with col2:
        st.subheader("Grafik LEAST")
        df_least = pd.DataFrame.from_dict(
            least_score, orient="index", columns=["Skor"]
        )
        st.bar_chart(df_least)

    # =========================
    # TABEL RINGKASAN
    # =========================
    st.subheader("Ringkasan Skor DISC")
    df_summary = pd.DataFrame({
        "MOST": most_score,
        "LEAST": least_score
    })
    st.dataframe(df_summary)
