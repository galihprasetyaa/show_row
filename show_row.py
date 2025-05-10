import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gabungkan Baris dari Dua CSV", layout="wide")
st.title("🔗 Gabungkan Baris yang Dipilih dari Dua CSV")

# Upload dua file CSV
col1, col2 = st.columns(2)
with col1:
    file1 = st.file_uploader("📁 Unggah CSV Pertama", type=["csv"], key="csv1")
with col2:
    file2 = st.file_uploader("📁 Unggah CSV Kedua", type=["csv"], key="csv2")

# Lanjut jika dua file sudah diunggah
if file1 and file2:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    st.subheader("📄 Pratinjau CSV 1")
    st.dataframe(df1)
    st.subheader("📄 Pratinjau CSV 2")
    st.dataframe(df2)

    st.markdown("### ✏️ Pilih Baris yang Ingin Digabung")

    # Pilih baris dari CSV 1
    selected_rows_1 = st.multiselect(
        "Pilih baris dari CSV 1 (berdasarkan index)", options=df1.index.tolist(), key="select1"
    )

    # Pilih baris dari CSV 2
    selected_rows_2 = st.multiselect(
        "Pilih baris dari CSV 2 (berdasarkan index)", options=df2.index.tolist(), key="select2"
    )

    if st.button("Gabungkan Baris yang Dipilih"):
        combined_df = pd.concat([df1.loc[selected_rows_1], df2.loc[selected_rows_2]], ignore_index=True)
        st.success(f"{len(combined_df)} baris berhasil digabung.")
        st.dataframe(combined_df)

        # Download hasil
        csv = combined_df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Unduh Tabel Gabungan", csv, "gabungan_baris.csv", "text/csv")
else:
    st.info("Silakan unggah dua file CSV terlebih dahulu.")
