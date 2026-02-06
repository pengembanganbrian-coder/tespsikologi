import streamlit as st
import pandas as pd
import os, sys, traceback

st.set_page_config(page_title="Tes DISC Online", layout="wide")
st.title("🧠 Tes DISC Online (Diagnostic)")

# =========================
# DIAGNOSTIK FILE & PATH
# =========================
with st.expander("🔧 Diagnostics (buka kalau error)", expanded=True):
    st.write("Current dir:", os.getcwd())
    st.write("This file:", __file__)
    st.write("Files here:", os.listdir(os.path.dirname(__file__)))
    st.write("sys.path (top 5):", sys.path[:5])

# =========================
# IMPORT DATA & SCORING
# =========================
try:
    from pertanyaan import SOAL_DISC
    from skoring import MAPPING_MOST, MAPPING_LEAST
except Exception as e:
    st.error("❌ Gagal import modul. Ini detailnya:")
    st.code(traceback.format_exc())
    st.stop()

# =========================
# VALIDASI DATA SOAL & MAP
# =========================
def validate():
    # soal harus 24 kotak, tiap kotak 4 opsi
    if not isinstance(SOAL_DISC, (list, tuple)):
        return "SOAL_DISC bukan list/tuple."
    if len(SOAL_DISC) != 24:
        return f"SOAL_DISC harus 24 kotak, sekarang {len(SOAL_DISC)}."

    for idx, box in enumerate(SOAL_DISC, start=1):
        if not isinstance(box, (list, tuple)):
            return f"Kotak {idx} bukan list/tuple."
        if len(box) != 4:
            return f"Kotak {idx} harus 4 opsi, sekarang {len(box)}."

    # mapping harus punya key 1..24 dan index 0..3 dan hanya DISC
    valid_chars = {"D", "I", "S", "C"}

    for name, mp in [("MAPPING_MOST", MAPPING_MOST), ("MAPPING_LEAST", MAPPING_LEAST)]:
        if not isinstance(mp, dict):
            return f"{name} bukan dict."
        for k in range(1, 25):
            if k not in mp:
                return f"{name} tidak punya key kotak {k}."
            if not isinstance(mp[k], dict):
                return f"{name}[{k}] bukan dict."
            for opt in range(4):
                if opt not in mp[k]:
                    return f"{name}[{k}] tidak punya index opsi {opt}."
                v = mp[k][opt]
                if isinstance(v, str):
                    v = v.strip().upper()
                if v not in valid_chars:
                    return f"{name}[{k}][{opt}] bernilai '{mp[k][opt]}' (harus D/I/S/C)."
    return None

err = validate()
if err:
    st.error("❌ VALIDASI DATA GAGAL:")
    st.code(err)
    st.stop()

st.success("✅ Import & validasi sukses. App siap jalan.")

# =========================
# SIDEBAR IDENTITAS
# =========================
with st.sidebar:
    st.header("Profil Peserta")
    nama = st.text_input("Nama Lengkap")
    nip = st.text_input("NIP / ID Pegawai")

st.info("Pilih 1 MOST (M) dan 1 LEAST (L) untuk tiap kotak.")

# =========================
# FORM SOAL (RAPI)
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

            jawaban_user.append({"M": m, "L": l})

st.divider()

# =========================
# PROSES HASIL (AMAN)
# =========================
if st.button("📊 PROSES & LIHAT HASIL", type="primary"):
    if not nama:
        st.warning("⚠️ Nama wajib diisi.")
        st.stop()

    most_score = {"D": 0, "I": 0, "S": 0, "C": 0}
    least_score = {"D": 0, "I": 0, "S": 0, "C": 0}

    try:
        for i, ans in enumerate(jawaban_user):
            kotak = i + 1
            char_m = str(MAPPING_MOST[kotak][ans["M"]]).strip().upper()
            char_l = str(MAPPING_LEAST[kotak][ans["L"]]).strip().upper()

            most_score[char_m] += 1
            least_score[char_l] += 1

    except Exception:
        st.error("❌ Error saat hitung skor. Detail lengkap:")
        st.code(traceback.format_exc())
        st.stop()

    st.success(f"✅ Analisis selesai untuk **{nama}**")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("MOST")
        st.bar_chart(pd.DataFrame.from_dict(most_score, orient="index", columns=["Skor"]))
    with c2:
        st.subheader("LEAST")
        st.bar_chart(pd.DataFrame.from_dict(least_score, orient="index", columns=["Skor"]))

    st.subheader("Ringkasan")
    st.dataframe(pd.DataFrame({"MOST": most_score, "LEAST": least_score}))
