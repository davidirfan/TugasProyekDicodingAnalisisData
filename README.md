# Tugas Proyek Analisis Data dari DICODING

## Intro
Github Repository ini merupakan tugas proyek dari Kelas Dicoding - Analisis Data dengan Python. Proyek analisis data ini menggunakan dataset "Bike Sharing Dataset" yang tersedia di Kagle (dapat diakses di [sini](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)). Pengerjaan tugas proyek ini meliputi dua tahapan besar, yaitu analisis data dan pembuatan dashboard data.

## Analisis Data
Tahapan analisis data meliputi :
1. Menentukan pertanyaan analisis data.
2. Mengumpulkan data-data yang diperlukan.
3. Memeriksa data-data (Assessing Data).
4. Membersihkan data-data (Cleaning Data).
5. Menganalisis data berdasarkan pertanyaan-pertanyaan sebelumnya (Exploratory Data Analysis).
6. Membuat visualisasi data.
7. Merumuskan kesimpulan berdasarkan pernyataan dan analisis data.

Detail proses analisis data dapat diakses melalui file [notebook berikut](https://github.com/davidirfan/TugasProyekDicodingAnalisisData/blob/9221a69fb568ff08ccdfa19b263ead172825a109/NotebookAnalisisData.ipynb).

## Pembuatan Dashboard Data.
Dashboard data dibuat dengan menggunakan modul streamlit pada Python. Detail pembuatan dashboard data dapat diakses melalui file python berikut.
<br>
Dashboard data Streamlit dapat diakses melalui dua cara, yaitu melalui streamlit cloud dan akses lokal.

a. Akses streamlit cloud.
Akses dashboard data pada streamlit cloud dapat melalui link berikut.[Dashboard Data Rental Sepeda](https://dashboardrentalsepeda.streamlit.app/)

b. Akses lokal.
Akses dashboard data pada komputer lokal dapat dilakukan melalui langkah-langkah berikut.
1. Mengunduh semua file dalam repository ini sebagai satu file zip.
2. Ekstrak file yang sudah diunduh.
3. Pasang modul-modul library Python yang diperlukan sesuai yang terdapat pada file requirements.txt atau pasang langsung dengan menggunakan baris perintah berikut pada windows Command Prompt mode Administrator
```bash
pip install -r requirements.txt
```
4. Buka file dashboardRentalSepeda.py pada folder dashboard menggunakan code editor yang digunakan (seperti Visual Studio Code), lalu jalankan (Run) program dengan code editor tersebut hingga muncul baris perintah untuk membuka dahsboard. <br>
Command line berupa "streamlit run [lokasi file dashboard tersimpan di komputer lokal]".
![Contoh command line untuk membuka streamlit dashboad](https://raw.githubusercontent.com/davidirfan/TugasProyekDicodingAnalisisData/main/dashboard/address.PNG)
5. Buka dashboard dengan menyalin baris perintah tersebut dan dijalankan dengan aplikasi Command Prompt. Secara otomatis dashboard data akan terbuka melalui aplikasi web browser.
