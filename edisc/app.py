import streamlit as st
import pandas as pd

# =========================
# IMPORT DATA & SCORING
# =========================
try:
    from pertanyaan import SOAL_DISC
    from skoring import MAPPING_MOST, MAPPING_LEAST
except ImportError as e:
    st.error("❌ File pendukung tidak ditemukan.")
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
# VALIDASI DATA SOAL
# =========================
if len(SOAL_DISC) != 24:
    st.error("❌ Jumlah kotak DISC harus 24.")
    st.stop()

# =========================
# FORM SOAL DISC
# =========================
st.subheader("Instruksi")
st.write(
    "Pada setiap kotak, pilih **SATU pernyataan PALING sesuai (M)** "
    "dan **SATU pernyataan PALING TIDAK sesuai (L)** dengan diri Anda."
)

jawaban_user = []
cols = st.columns(3)

for i, options in enumerate(SOAL_DISC):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"### Kotak {i+1}")

            col_m, col_l, col_text = st.columns([1, 1, 6])

            m = col_m.radio(
                "M",
                [0, 1, 2, 3],
                key=f"M_{i}",
                label_visibility="collapsed"
            )

            l = col_l.radio(
                "L",
                [0, 1, 2, 3],
                key=f"L_{i}",
                label_visibility="collapsed"
            )

            for idx, txt in enumerate(options):
                col_text.write(f"{idx+1}. {txt}")

            jawaban_user.append({"M": m, "L": l})

st.divider()

# =========================
# PROSES HASIL
# =========================
if st.button("📊 PROSES & LIHAT HASIL", type="primary"):

    if not nama:
        st.warning("⚠️ Nama peserta wajib diisi.")
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

        if char_m in most_score:
            most_score[char_m] += 1

        if char_l in least_score:
            least_score[char_l] += 1

    st.success(f"✅ Analisis selesai untuk **{nama}**")

    # =========================
    # TAMPILAN HASIL
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
    st.subheader("Ringkasan Skor")
    df_ringkasan = pd.DataFrame({
        "MOST": most_score,
        "LEAST": least_score
    })
    st.dataframe(df_ringkasan)
