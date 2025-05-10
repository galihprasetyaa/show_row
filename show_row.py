import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gabung Baris dari Nilai Kolom", layout="wide")
st.title("🔗 Gabungkan Baris Berdasarkan Nilai dalam Kolom")

# Upload dua file CSV
col1, col2 = st.columns(2)
with col1:
    file1 = st.file_uploader("📁 Unggah CSV Pertama", type=["csv"], key="csv1")
with col2:
    file2 = st.file_uploader("📁 Unggah CSV Kedua", type=["csv"], key="csv2")

if file1 and file2:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    st.subheader("📋 Pratinjau Data")
    st.write("CSV 1")
    st.dataframe(df1.head())
    st.write("CSV 2")
    st.dataframe(df2.head())

    st.markdown("### 🎯 Pilih Kolom sebagai Kunci Pemilihan Baris")

    # Pilih kolom dari masing-masing file
    col_key1 = st.selectbox("Pilih kolom kunci dari CSV 1", df1.columns, key="col_key1")
    col_key2 = st.selectbox("Pilih kolom kunci dari CSV 2", df2.columns, key="col_key2")

    if col_key1 and col_key2:
        st.markdown("### 🧩 Pilih Nilai dari Kolom untuk Diambil Barisnya")

        # Pilih nilai dari kolom tersebut
        values1 = st.multiselect(f"Pilih nilai dari kolom '{col_key1}' (CSV 1)", df1[col_key1].dropna().unique(), key="val1")
        values2 = st.multiselect(f"Pilih nilai dari kolom '{col_key2}' (CSV 2)", df2[col_key2].dropna().unique(), key="val2")

        if st.button("Gabungkan Baris Berdasarkan Nilai"):
            selected_df1 = df1[df1[col_key1].isin(values1)]
            selected_df2 = df2[df2[col_key2].isin(values2)]

            combined_df = pd.concat([selected_df1, selected_df2], ignore_index=True)

            st.success(f"{len(combined_df)} baris berhasil digabung berdasarkan nilai kolom.")
            st.dataframe(combined_df)

            # Tombol download
            csv = combined_df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Unduh Tabel Gabungan", csv, "gabungan_baris_dari_kolom.csv", "text/csv")
else:
    st.info("Unggah dua file CSV terlebih dahulu.")
