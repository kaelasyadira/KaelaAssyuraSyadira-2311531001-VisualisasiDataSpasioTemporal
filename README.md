# Dashboard Spasio-Temporal IMK Indonesia

Dashboard visualisasi interaktif untuk menganalisis pola industri mikro dan kecil (IMK) di Indonesia berdasarkan data BPS tahun 2013–2024, dilengkapi dengan analisis klusterisasi K-Means dan visualisasi spasial berbasis peta.

---

## Fitur Utama

- **Tentang Dataset** — Metadata, sampel data, dan peta animasi perubahan cluster IMK per tahun
- **Analisis Temporal** — Tren nasional, distribusi per pulau, dan top 10 provinsi berdasarkan indikator pilihan
- **Perbandingan Provinsi** — Perbandingan tren dua provinsi secara dinamis
- **Analisis Machine Learning** — Visualisasi hasil K-Means clustering (distribusi cluster, scatter plot, profil statistik)
- **Visualisasi Spasial** — Peta persebaran cluster dan heatmap intensitas per provinsi

---

## Teknologi yang Digunakan

| Library | Kegunaan |
|---|---|
| `streamlit` | Framework aplikasi web interaktif |
| `pandas` | Manipulasi dan agregasi data |
| `numpy` | Komputasi numerik |
| `plotly` | Grafik interaktif (line, bar, pie, scatter, mapbox) |
| `folium` | Peta interaktif berbasis Leaflet |
| `streamlit-folium` | Integrasi Folium ke dalam Streamlit |

---

## Struktur File

```
├── app.py               # File utama aplikasi Streamlit
├── data_imk.csv         # Dataset IMK Indonesia (BPS, 2013–2024)
├── requirements.txt     # Daftar dependensi Python
└── README.md            # Dokumentasi proyek
```

---

## Cara Menjalankan Aplikasi

### 1. Clone atau unduh repositori ini

```bash
git clone <url-repositori>
cd <nama-folder>
```

### 2. Install dependensi

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
streamlit run app.py
```

### 4. Buka di browser

Aplikasi akan otomatis terbuka di browser pada alamat:
```
http://localhost:8501
```

> **Pastikan file `data_imk.csv` berada di folder yang sama dengan `app.py` sebelum menjalankan aplikasi.**

---

## Sumber Data

Dataset yang digunakan bersumber dari **Badan Pusat Statistik (BPS) Republik Indonesia**, mencakup data Industri Mikro dan Kecil (IMK) seluruh provinsi di Indonesia pada rentang tahun **2013–2024**.

Indikator yang tersedia:
- Jumlah Perusahaan IMK
- Jumlah Tenaga Kerja
- Nilai Output (dalam satuan juta rupiah)

---

## Informasi Pengembang

| | |
|---|---|
| **Nama** | Kaela Assyura Syadira |
| **NIM** | 2311531001 |
| **Program Studi** | Informatika, Universitas Andalas |
| **Tahun** | 2026 |
