import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# PREPARE DATAFRAME

def buat_hitung_perBulan_df(df):
    hitung_perBulan = df.resample(rule='M', on='tanggal').agg({
    "Penyewa_NonMember":"sum",
    "Penyewa_Member":"sum",
    "Total_Penyewa":"sum"
    })
    hitung_perBulan.index = hitung_perBulan.index.strftime('%b-%y')
    hitung_perBulan = hitung_perBulan.reset_index()
    hitung_perBulan.rename(columns={
        "tanggal": "bulanTahun",
        "Penyewa_NonMember":"nonMember",
        "Penyewa_Member":"Member",
        "Total_Penyewa":"Semua"
    }, inplace=True)
    return hitung_perBulan

def buat_hitung_perjam_df(df):
    hitung_perjam = df.groupby(by="jam").agg({
    "Penyewa_NonMember":"sum",
    "Penyewa_Member":"sum",
    "Total_Penyewa":"sum"
    }).reset_index()
    return hitung_perjam

def buat_hitung_permusim_df(df):
    hitung_permusim = df.groupby(by="musim").agg({
        "Total_Penyewa":"sum"
    }).reset_index()
    return hitung_permusim

def buat_hitung_perhari_df(df):
    hitung_perhari = df.groupby(by="hari").agg({
    "Penyewa_NonMember":"sum",
    "Penyewa_Member":"sum",
    "Total_Penyewa":"sum"
    }).reset_index()
    hitung_perhari['hari'] = pd.Categorical(hitung_perhari['hari'],
                                            categories=['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu'])
    hitung_perhari = hitung_perhari.sort_values('hari').reset_index()
    hitung_perhari = hitung_perhari.drop('index', axis=1)
    return hitung_perhari

def buat_hitung_percuaca_df(df):
    hitung_percuaca = df.groupby(by="cuaca").agg({
        "Total_Penyewa":"sum"
    }).reset_index()
    return hitung_percuaca

# PREPARE FILTER
jam_df=pd.read_csv('https://raw.githubusercontent.com/davidirfan/TugasProyekDicodingAnalisisData/main/dashboard/new_jam.csv')

# ubah tipe data
jam_df['musim'] = jam_df.musim.astype('category')
jam_df['tahun'] = jam_df.tahun.astype('category')
jam_df['bulan'] = jam_df.bulan.astype('category')
jam_df['hari_libur'] = jam_df.hari_libur.astype('category')
jam_df['hari'] = jam_df.hari.astype('category')
jam_df['hari_kerja'] = jam_df.hari_kerja.astype('category')
jam_df['cuaca'] = jam_df.cuaca.astype('category')
jam_df['tanggal'] = pd.to_datetime(jam_df['tanggal'])


min_date = jam_df["tanggal"].min()
max_date = jam_df["tanggal"].max()

# DASHBOARD SETUP

st.set_page_config(page_title="Dashboard Data Rental Sepeda", page_icon=":bicycle:", layout="wide")
st.header('Dashboard Data Jumlah Penyewa Sepeda Tahun 2011-2012')

# SETUP SIDEBAR
with st.sidebar:
    # DISPLAY GAMBAR LOGO
    st.image("https://raw.githubusercontent.com/davidirfan/TugasProyekDicodingAnalisisData/main/dashboard/sepedahan.png")
    # DISPLAY RANGE FILTER
    start_date, end_date = st.date_input(
        label='Pilih Rentang Tanggal',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
st.sidebar.header("Kunjungi Profilku & Hubungiku disini")
st.sidebar.markdown(
    "David Irfan Jasir"
    )
#SIDEBAR COLUMN
kolom11, kolom12 = st.sidebar.columns(2)
with kolom11:
    st.markdown("[![LinkedIn](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/david-irfan-jasir/)")
with kolom12:
    st.markdown("[![Github](https://pngimg.com/uploads/github/github_PNG40.png)](https://github.com/davidirfan)")

# DATAFRAME DISESUAIKAN DENGAN RANGE FILTER
main_df = jam_df[(jam_df["tanggal"] >= str(start_date)) & 
                (jam_df["tanggal"] <= str(end_date))]

# INPUT DATAFRAME SESUAI RANGE FILTER
perBulan = buat_hitung_perBulan_df(main_df)
perjam = buat_hitung_perjam_df(main_df)
permusim = buat_hitung_permusim_df(main_df)
perhari = buat_hitung_perhari_df(main_df)
percuaca = buat_hitung_percuaca_df(main_df)

st.subheader('Jumlah Perental pada waktu tertentu')
# BARIS PERTAMA VISUAL DATA
kolom21, kolom22 = st.columns(2)
# BARIS PERTAMA KOLOM PERTAMA VISUAL DATA
with kolom21:
    semua_perental = main_df['Total_Penyewa'].sum()

    nonMember = main_df['Penyewa_NonMember'].sum()
    persen_nonMember = nonMember/semua_perental

    Member = main_df['Penyewa_Member'].sum()
    persen_Member = Member/semua_perental

    st.metric("TOTAL PERENTAL", value=semua_perental)
    st.metric("TOTAL PERENTAL NON-MEMBER", value=nonMember)
    st.metric("TOTAL PERENTAL MEMBER", value=Member)
    
    labels = ['Perental Non-Member','Perental Member']
    nilai = [persen_nonMember, persen_Member]

    fig, ax = plt.subplots()
    ax.pie(
        nilai,
        labels = labels,
        autopct = '%1.1f%%'
           )
    ax.set_title('Persen Pengguna')

    st.pyplot(fig)
# BARIS PERTAMA KOLOM KEDUA VISUAL DATA
with kolom22:
    fig = px.line(perBulan,
              x='bulanTahun',
              y=['nonMember', 'Member', 'Semua'],
              color_discrete_sequence=["blue", "green", "red"],
              markers=True,
              title="Jumlah perental tiap bulan").update_layout(xaxis_title='', yaxis_title='Total Rides')

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
# BARIS KEDUA VISUAL DATA
kolom31, kolom32 = st.columns(2)
# BARIS KEDUA KOLOM PERTAMA VISUAL DATA
with kolom31:
    labels = percuaca['cuaca']
    nilai = percuaca['Total_Penyewa']

    fig, ax = plt.subplots()
    ax.pie(
        nilai,
        labels = labels,
        autopct = '%1.1f%%'
           )
    ax.set_title('Persen Cuaca')

    st.pyplot(fig)
# BARIS KEDUA KOLOM KEDUA VISUAL DATA
with kolom32:
    labels = permusim['musim']
    nilai = permusim['Total_Penyewa']

    fig, ax = plt.subplots()
    ax.pie(
        nilai,
        labels = labels,
        autopct = '%1.1f%%'
           )
    ax.set_title('Persen musim')

    st.pyplot(fig)

st.markdown("---")
# BARIS KEDUA VISUAL DATA
kolom41, kolom42 = st.columns(2)
# BARIS KETIGA KOLOM PERTAMA VISUAL DATA
with kolom41:
    fig = px.line(perjam,
              x='jam',
              y=['Penyewa_NonMember', 'Penyewa_Member', 'Total_Penyewa'],
              color_discrete_sequence=["blue", "green", "red"],
              markers=True,
              title="Jumlah perental pada setiap jam dalam sehari").update_layout(xaxis_title='', yaxis_title='Total Rides')

    st.plotly_chart(fig, use_container_width=True)
# BARIS KETIGA KOLOM KEDUA VISUAL DATA
with kolom42:
    fig = px.line(perhari,
              x='hari',
              y=['Penyewa_NonMember', 'Penyewa_Member', 'Total_Penyewa'],
              color_discrete_sequence=["blue", "green", "red"],
              markers=True,
              title="Jumlah perental pada setiap hari dalam seminggu").update_layout(xaxis_title='', yaxis_title='Total Rides')

    st.plotly_chart(fig, use_container_width=True)
