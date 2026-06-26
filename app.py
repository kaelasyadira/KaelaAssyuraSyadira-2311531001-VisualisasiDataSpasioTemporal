import streamlit as st                              # Framework dashboard interaktif
import pandas as pd                                 # Manipulasi dan agregasi data tabular
import numpy as np                                  # Komputasi numerik 
import plotly.express as px                         # Grafik interaktif 
import folium                                       # Peta interaktif berbasis Leaflet.js
from streamlit_folium import st_folium              # Integrasi Folium ke Streamlit
from folium.plugins import HeatMap, HeatMapWithTime # Plugin heatmap pada peta Folium

# KONFIGURASI HALAMAN & CACHE DATA
st.set_page_config(
    page_title="Dashboard Spasio-Temporal IMK Indonesia",
    page_icon="🗺️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #1E1A1A;
}

.stApp {
    background-color: #F6EFE8;
}

[data-testid="stSidebar"] {
    background-color: #1E1A1A !important;
    border-right: 1px solid #443538 !important;
}

[data-testid="stSidebar"] * {
    color: #E3D6BF !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #F6EFE8 !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 1.1rem !important;
    letter-spacing: 0.3px;
    margin-top: 1rem !important;
    margin-bottom: 0.5rem !important;
}

[data-testid="stSidebar"] .stRadio [data-testid="stWidgetLabel"] {
    display: none !important;
}

[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 8px !important;
}

[data-testid="stSidebar"] .stRadio label {
    border-radius: 8px;
    padding: 6px 12px !important;
    transition: background 0.2s ease;
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    white-space: nowrap !important;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background-color: rgba(179, 114, 138, 0.15) !important;
    color: #B5728A !important;
}

[data-testid="stSidebar"] .stCaption,
[data-testid="stSidebar"] small {
    color: #9F9679 !important;
    font-size: 0.72rem !important;
}

[data-testid="stSidebar"] hr {
    border-color: #443538 !important;
}

h1 {
    font-family: 'Sora', sans-serif !important;
    font-size: 1.75rem !important;
    font-weight: 700 !important;
    color: #1E1A1A !important;
    margin-bottom: 0.15rem !important;
}

h2 {
    font-family: 'Sora', sans-serif !important;
    font-size: 1.15rem !important;
    font-weight: 600 !important;
    color: #2D2426 !important;
    margin-top: 1.5rem !important;
}

h3 {
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    color: #3D2830 !important;
}

p, .stMarkdown p {
    color: #5A4A4E;
    font-size: 0.92rem;
    line-height: 1.7;
}

[data-testid="metric-container"] {
    background: #EFE2D6 !important;
    border: 1px solid #E3D6BF !important;
    border-radius: 12px !important;
    padding: 1.1rem 1.25rem !important;
    transition: box-shadow 0.2s ease;
}

[data-testid="metric-container"]:hover {
    box-shadow: 0 4px 16px rgba(147, 59, 91, 0.12) !important;
}

[data-testid="metric-container"] label {
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.9px !important;
    color: #9F9679 !important;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'Sora', sans-serif !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    color: #933B5B !important;
}

.stSelectbox label,
.stRadio label span,
.stSlider label {
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    color: #7A5E64 !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

div[data-baseweb="select"] > div {
    background-color: #EFE2D6 !important;
    border: 1px solid #E3D6BF !important;
    border-radius: 8px !important;
    font-size: 0.88rem !important;
    color: #1E1A1A !important;
    box-shadow: none !important;
    transition: border-color 0.2s;
}

div[data-baseweb="select"] > div:hover {
    border-color: #B5728A !important;
}

.stDownloadButton button,
.stButton button {
    background-color: #933B5B !important;
    color: #F6EFE8 !important;
    border: none !important;
    border-radius: 8px !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.25rem !important;
    letter-spacing: 0.3px;
    transition: background 0.2s ease, transform 0.1s ease;
}

.stDownloadButton button:hover,
.stButton button:hover {
    background-color: #A03F63 !important;
    transform: translateY(-1px);
}

[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden;
    border: 1px solid #E3D6BF !important;
}

[data-testid="stDataFrame"] table {
    font-size: 0.83rem !important;
}

[data-testid="stDataFrame"] thead th {
    background-color: #EFE2D6 !important;
    color: #5A4A4E !important;
    font-weight: 600 !important;
    font-size: 0.76rem !important;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

.stPlotlyChart {
    background: #EFE2D6;
    border-radius: 12px;
    border: 1px solid #E3D6BF;
    padding: 0.5rem;
}

.page-header {
    border-left: 4px solid #933B5B;
    padding-left: 0.9rem;
    margin-bottom: 1.5rem;
    border-radius: 0;
}

.page-header h1 { margin-bottom: 0.2rem !important; }

.page-header p {
    font-size: 0.84rem;
    color: #9F9679;
    margin: 0;
}

iframe {
    border-radius: 12px !important;
    border: 1px solid #E3D6BF !important;
    overflow: hidden;
}

[data-testid="stHeader"] {
    display: none !important;
    height: 0 !important;
}

header[data-testid="stHeader"] {
    display: none !important;
}

#root > div:first-child > div > div > div > div > section > div {
    padding-top: 0 !important;
}

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    padding-left: 2.5rem !important;
    padding-right: 2.5rem !important;
    max-width: 1280px;
}
</style>
""", unsafe_allow_html=True)

# Fungsi Utilitas
def page_header(title: str, subtitle: str = ""):
    st.markdown(f"""
    <div class="page-header">
        <h1>{title}</h1>
        {"<p>" + subtitle + "</p>" if subtitle else ""}
    </div>
    """, unsafe_allow_html=True)


@st.cache_data
def load_data():
    df = pd.read_csv("data_imk.csv")
    return df

# untuk memuat data dan menampilkan pesan error jika file tidak ditemukan
try:
    df = load_data()
except FileNotFoundError:
    st.error("Gagal memuat data! Pastikan file 'data_imk.csv' sudah diletakkan di folder yang sama.")
    st.stop()

# SIDEBAR NAVIGATION
st.sidebar.title("🗺️ Dashboard")
st.sidebar.markdown("Silakan pilih halaman analisis:")

halaman = st.sidebar.radio(
    label="Pilih Menu Analisis:",
    options=[
        "📋 Tentang Dataset",
        "📈 Analisis Temporal",
        "👥 Perbandingan Provinsi",
        "🧮 Analisis Machine Learning",
        "🗺️ Visualisasi Spasial"
    ]
)

st.sidebar.write("---")
st.sidebar.caption("Sistem Visualisasi Klustering Data Spasio-Temporal IMK | Kaela | 2311531001 | 2026")

# KONFIGURASI PLOTLY (Template layout default untuk semua grafik Plotly)
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="#F6EFE8",
    font_family="Inter, sans-serif",
    font_color="#5A4A4E",
    title_font_family="Sora, sans-serif",
    title_font_color="#1E1A1A",
    title_font_size=14,
    margin=dict(t=50, l=16, r=16, b=16),
    xaxis=dict(showgrid=True, gridcolor="#E3D6BF", zeroline=False, linecolor="#E3D6BF"),
    yaxis=dict(showgrid=True, gridcolor="#E3D6BF", zeroline=False, linecolor="#E3D6BF"),
    legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="rgba(0,0,0,0)")
)

AMARANTH_SCALE = [[0, "#E3D6BF"], [0.5, "#B5728A"], [1, "#933B5B"]]
CLUSTER_COLORS = ["#933B5B", "#AABAAE", "#9F9679", "#B5728A"]
COMP_COLORS = ["#933B5B", "#AABAAE"]

# HALAMAN TENTANG DATASET ( menampilkan metadata, sampel data, peta animasi, dan tombol download dataset )
if halaman == "📋 Tentang Dataset":
    page_header(
        "Data IMK Indonesia",
        "Metadata dan struktur dataset Industri Mikro dan Kecil (IMK) Indonesia"
    )

    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric("Jumlah Data (Baris)", f"{len(df):,}")
    with col_m2:
        st.metric("Jumlah Provinsi", df["provinsi"].nunique())
    with col_m3:
        st.metric("Rentang Tahun", f"{df['tahun'].min()} – {df['tahun'].max()}")

    st.write("")
    st.subheader("🗺️ Perubahan Cluster IMK Indonesia (2013–2024)")

    # Nomralisasi ukuran plot berdasarkan nilai_output untuk visualisasi peta
    min_output = df["nilai_output"].min()
    max_output = df["nilai_output"].max()

    df["ukuran_plot"] = (
        ((df["nilai_output"] - min_output) /
        (max_output - min_output))
        * 10
    ) + 8

    # Peta animasi temporal yang setiap frame mewakili satu tahun (2013–2024)
    fig_map = px.scatter_mapbox(
        df,

        lat="latitude",
        lon="longitude",

        color="Kategori_Cluster",

        size="ukuran_plot",
        size_max=18,

        animation_frame="tahun",

        hover_name="provinsi",

        hover_data={
            "nilai_output": ":,.0f",
            "jumlah_perusahaan": True,
            "jumlah_tenaga_kerja": True,
            "latitude": False,
            "longitude": False,
            "ukuran_plot": False
        },

        zoom=4.7,

        center={
            "lat": -2.5,
            "lon": 118
        },

        color_discrete_map={
            "Cluster 0: Raksasa IMK (Kecil Dominan)": "#933B5B",
            "Cluster 1: Produktivitas IMK Rendah": "#9F9679",
            "Cluster 2: Produktivitas IMK Tinggi": "#AABAAE",
            "Cluster 3: Raksasa IMK (Mikro Dominan)": "#B5728A"
        }
    )

    fig_map.update_traces(
        marker=dict(
            opacity=0.85
        )
    )

    fig_map.update_layout(

        mapbox_style="carto-positron",

        mapbox_zoom=4.7,

        mapbox_center={
            "lat": -2.5,
            "lon": 118
        },

        height=650,

        paper_bgcolor="#F6EFE8",
        plot_bgcolor="#F6EFE8",

        margin=dict(
            l=0,
            r=0,
            t=20,
            b=0
        ),

        legend=dict(
            title="Cluster",
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="#D9C7B6",
            borderwidth=1,

            x=0.02,
            y=0.98,

            xanchor="left",
            yanchor="top",

            font=dict(size=11)
        ),

        sliders=[{
            "pad": {"t": 0},
            "len": 0.85,
            "x": 0.1,
            "y": -0.1
        }]
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True,
        config={
            "scrollZoom": True,
            "displayModeBar": False
        }
    )
    
    st.write("")
    st.subheader("Sampel Data (20 Baris Pertama)")
    st.dataframe(df.head(20), use_container_width=True)

    st.write("")
    st.download_button(
        label="📥 Download Dataset (CSV)",
        data=df.to_csv(index=False),
        file_name="data_imk.csv",
        mime="text/csv"
    )

# HALAMAN ANALISIS TEMPORAL (menampilkan tren perkembangan indikator IMK dari tahun ke tahun secara nasional)
elif halaman == "📈 Analisis Temporal":
    page_header(
        "Analisis Temporal & Agregasi",
        "Tren perkembangan indikator IMK dari tahun ke tahun secara nasional"
    )

    st.markdown("### 📈 Filter Analisis Temporal")
    indikator = st.selectbox(
        "📊 Pilih Indikator Utama yang Ingin Dilihat:",
        ["nilai_output", "jumlah_perusahaan", "jumlah_tenaga_kerja"]
    )
    st.write("---")

    # Tren Perkembangan Indikator IMK dari Tahun ke Tahun (Agregasi Nasional)
    trend = df.groupby("tahun")[indikator].sum().reset_index()
    fig = px.line(
        trend,
        x="tahun",
        y=indikator,
        markers=True,
        title=f"Tren Perkembangan Total {indikator.replace('_', ' ').title()}",
        color_discrete_sequence=["#933B5B"]
    )
    fig.update_traces(line_width=2.5, marker_size=7,
                      marker_color="#933B5B", marker_line_color="#F6EFE8", marker_line_width=1.5)
    fig.update_layout(**PLOTLY_LAYOUT)
    st.plotly_chart(fig, use_container_width=True)

    st.write("")
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Perbandingan Berdasarkan Pulau")
        pulau = df.groupby("pulau")[indikator].sum().reset_index()
        fig2 = px.bar(
            pulau,
            x="pulau",
            y=indikator,
            color=indikator,
            color_continuous_scale=AMARANTH_SCALE,
            title=f"Distribusi {indikator.replace('_', ' ').title()} per Pulau"
        )
        fig2.update_layout(**PLOTLY_LAYOUT)
        st.plotly_chart(fig2, use_container_width=True)

    with col_chart2:
        st.subheader("Top 10 Provinsi")
        tahun_pilih = st.selectbox(
            "Pilih Tahun untuk Top 10:",
            sorted(df["tahun"].unique()),
            key="tahun_temporal"
        )
        top = (
            df[df["tahun"] == tahun_pilih]
            .sort_values(indikator, ascending=False)
            .head(10)
        )
        fig3 = px.bar(
            top,
            x=indikator,
            y="provinsi",
            orientation="h",
            title=f"10 Provinsi Teratas ({tahun_pilih})",
            color=indikator,
            color_continuous_scale=AMARANTH_SCALE
        )
        bar_layout = PLOTLY_LAYOUT.copy()
        bar_layout.pop('yaxis', None)
        fig3.update_layout(**bar_layout, yaxis=dict(categoryorder="total ascending"))
        st.plotly_chart(fig3, use_container_width=True)

# HALAMAN PERBANDINGAN PROVINSI ( menampilkan perbandingan indikator IMK antara dua provinsi yang dipilih pengguna)
elif halaman == "👥 Perbandingan Provinsi":
    page_header(
        "Perbandingan Spasio-Temporal Antar Provinsi",
        "Bandingkan pertumbuhan performa ekonomi dua daerah secara dinamis"
    )

    col_comp1, col_comp2 = st.columns(2)
    with col_comp1:
        prov_1 = st.selectbox("Provinsi Pertama:", sorted(df["provinsi"].unique()), index=0)
    with col_comp2:
        prov_2 = st.selectbox("Provinsi Kedua:", sorted(df["provinsi"].unique()), index=1)

    ind_comp = st.selectbox(
        "Variabel Pembanding:",
        ["nilai_output", "jumlah_perusahaan", "jumlah_tenaga_kerja"]
    )

    # Filter data untuk kedua provinsi yang dipilih
    df_comp = df[df["provinsi"].isin([prov_1, prov_2])]

    fig_comp = px.line(
        df_comp,
        x="tahun",
        y=ind_comp,
        color="provinsi",
        markers=True,
        title=f"Adu Tren {ind_comp.replace('_', ' ').title()}: {prov_1} vs {prov_2}",
        color_discrete_sequence=COMP_COLORS
    )
    fig_comp.update_traces(line_width=2.5, marker_size=7)
    fig_comp.update_layout(**PLOTLY_LAYOUT)
    st.plotly_chart(fig_comp, use_container_width=True)

    st.subheader("Matriks Data Mentah Perbandingan")
    st.dataframe(
        df_comp[["provinsi", "tahun", "jumlah_perusahaan", "jumlah_tenaga_kerja",
                 "nilai_output", "Kategori_Cluster"]].sort_values("tahun"),
        use_container_width=True
    )

# HALAMAN ANALISIS MACHINE LEARNING ( menampilkan hasil klasterisasi K-Means dan interpretasi karakteristik tiap cluster )
elif halaman == "🧮 Analisis Machine Learning":
    page_header(
        "Analisis Machine Learning (K-Means Clustering)",
        "Segmentasi provinsi berdasarkan pola kapasitas industri mikro dan kecil"
    )

    st.markdown("### 🧮 Filter & Perbandingan Variabel Cluster")
    c_ml1, c_ml2, c_ml3 = st.columns(3)
    with c_ml1:
        tahun_ml = st.selectbox(
            "📅 Pilih Tahun Analisis:",
            sorted(df["tahun"].unique()),
            key="tahun_ml"
        )
    with c_ml2:
        x_var_ml = st.selectbox(
            "🔀 Sumbu X Grafik Scatter:",
            ["jumlah_perusahaan", "nilai_output", "jumlah_tenaga_kerja"],
            index=0,
            key="x_ml"
        )
    with c_ml3:
        y_var_ml = st.selectbox(
            "🔀 Sumbu Y Grafik Scatter:",
            ["nilai_output", "jumlah_perusahaan", "jumlah_tenaga_kerja"],
            index=0,
            key="y_ml"
        )
    st.write("---")

    # Filter data berdasarkan tahun yang dipilih
    filtered_ml = df[df["tahun"] == tahun_ml]

    col_ml1, col_ml2 = st.columns([1, 1])

    with col_ml1:
        st.subheader("Distribusi Cluster")
        cluster_counts = filtered_ml["Kategori_Cluster"].value_counts().reset_index()
        cluster_counts.columns = ["Cluster", "Jumlah Provinsi"]

        fig_pie = px.pie(
            cluster_counts,
            names="Cluster",
            values="Jumlah Provinsi",
            hole=0.52,
            title=f"Proporsi Cluster Provinsi — {tahun_ml}",
            color_discrete_sequence=CLUSTER_COLORS
        )
        pie_layout = PLOTLY_LAYOUT.copy()
        pie_layout.pop('legend', None)
        fig_pie.update_layout(
            **pie_layout,
            height=420,
            legend=dict(
                orientation="v",
                bgcolor="rgba(0,0,0,0)",
                font=dict(size=11),
                x=1.02, y=0.5
            )
        )
        fig_pie.update_traces(textfont_size=12, textposition="inside", insidetextorientation="radial")
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_ml2:
        st.subheader("Sebaran Pola Kluster")
        
        # Grafik scatter untuk membandingkan dua variabel yang dipilih pengguna
        fig_scatter = px.scatter(
            filtered_ml,
            x=x_var_ml,
            y=y_var_ml,
            color="Kategori_Cluster",
            hover_name="provinsi",
            size="jumlah_tenaga_kerja" if (x_var_ml != "jumlah_tenaga_kerja" and y_var_ml != "jumlah_tenaga_kerja") else None,
            title=f"Perbandingan {x_var_ml.replace('_', ' ').title()} vs {y_var_ml.replace('_', ' ').title()} ({tahun_ml})",
            labels={
                x_var_ml: x_var_ml.replace('_', ' ').title(),
                y_var_ml: y_var_ml.replace('_', ' ').title(),
                "Kategori_Cluster": "Cluster"
            },
            color_discrete_sequence=CLUSTER_COLORS
        )
        scatter_layout = PLOTLY_LAYOUT.copy()
        scatter_layout.pop('legend', None)
        fig_scatter.update_layout(
            **scatter_layout,
            height=420,
            legend=dict(
                orientation="v",
                bgcolor="rgba(0,0,0,0)",
                font=dict(size=11),
                x=1.02, y=0.5
            )
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.write("---")
    st.subheader("Profil Statistik per Cluster")
    
    # Agregasi statistik rata-rata untuk setiap cluster berdasarkan indikator utama
    profil = (
        filtered_ml.groupby("Kategori_Cluster")[["nilai_output", "jumlah_perusahaan", "jumlah_tenaga_kerja"]]
        .mean()
        .round(0)
        .reset_index()
    )
    st.dataframe(profil, use_container_width=True, hide_index=True)

    st.write("---")
    st.subheader("Interpretasi Karakteristik Cluster")
    cluster_info = [
        ("#933B5B", "Cluster 0", "Raksasa IMK — Kecil Dominan",
         "Industri skala kecil dengan nilai ekonomi dan output sangat tinggi. Produktivitas per unit usaha menonjol di atas rata-rata nasional."),
        ("#AABAAE", "Cluster 1", "Produktivitas Rendah — Rintisan",
         "Nilai output, jumlah usaha, and serapan tenaga kerja masih berada pada level minimum. Potensi pertumbuhan masih besar."),
        ("#9F9679", "Cluster 2", "Menengah Berkembang",
         "Kapasitas industri tumbuh stabil. Performa ekonomi menengah dengan tren positif yang konsisten."),
        ("#B5728A", "Cluster 3", "Raksasa IMK — Mikro Dominan",
         "Industri rumah tangga/mikro sangat masif dan padat serta menyerap tenaga kerja lokal dalam jumlah besar."),
    ]
    cols = st.columns(4)
    for i, (color, label, judul, deskripsi) in enumerate(cluster_info):
        with cols[i]:
            st.markdown(f"""
            <div style="
                background: #EFE2D6;
                border-top: 4px solid {color};
                border-radius: 10px;
                padding: 1rem 0.9rem;
                height: 100%;
            ">
                <div style="font-size:0.7rem; font-weight:600; text-transform:uppercase;
                            letter-spacing:0.8px; color:{color}; margin-bottom:4px;">
                    {label}
                </div>
                <div style="font-size:0.88rem; font-weight:600; color:#1E1A1A;
                            margin-bottom:8px; line-height:1.3;">
                    {judul}
                </div>
                <div style="font-size:0.8rem; color:#5A4A4E; line-height:1.55;">
                    {deskripsi}
                </div>
            </div>
            """, unsafe_allow_html=True)

# HALAMAN VISUALISASI SPASIAL 
# Menampilkan dua peta Folium interaktif:
#   (1) Peta persebaran cluster dengan CircleMarker berwarna per kelompok K-Means
#   (2) Heatmap intensitas dengan gradien warna berdasarkan nilai indikator terpilih
elif halaman == "🗺️ Visualisasi Spasial":
    page_header(
        "Visualisasi Spasial IMK Indonesia",
        "Persebaran geografis dan intensitas industri mikro & kecil per provinsi"
    )

    st.markdown("### ⚙️ Panel Kontrol Visualisasi Peta")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        tahun_spasial = st.selectbox(
            "📅 Tahun Visualisasi Peta:",
            sorted(df["tahun"].unique()),
            key="thn_spasial"
        )
    with col_f2:
        indikator_spasial = st.selectbox(
            "📊 Indikator Dimensi Ukuran Peta:",
            ["nilai_output", "jumlah_perusahaan", "jumlah_tenaga_kerja"],
            key="ind_spasial"
        )
    with col_f3:
        cluster_pilih = st.selectbox(
            "🤖 Saring Berdasarkan Kelompok Cluster:",
            ["Semua"] + sorted(df["Kategori_Cluster"].unique().tolist())
        )

    # Filter data berdasarkan tahun dan cluster yang dipilih
    filtered_spasial = df[df["tahun"] == tahun_spasial]
    if cluster_pilih != "Semua":
        filtered_spasial = filtered_spasial[filtered_spasial["Kategori_Cluster"] == cluster_pilih]

    st.write("---")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Provinsi Terfilter", filtered_spasial["provinsi"].nunique())
    k2.metric("Total Output Wilayah", f"{filtered_spasial['nilai_output'].sum():,.0f}")
    k3.metric("Total Unit Perusahaan", f"{filtered_spasial['jumlah_perusahaan'].sum():,.0f}")
    k4.metric("Total Tenaga Kerja", f"{filtered_spasial['jumlah_tenaga_kerja'].sum():,.0f}")

    if len(filtered_spasial) > 0:
        top_prov = filtered_spasial.loc[filtered_spasial[indikator_spasial].idxmax()]
        st.success(
            f"**Insight Geografis {tahun_spasial}:** "
            f"Provinsi dengan **{indikator_spasial.replace('_', ' ').title()}** tertinggi adalah "
            f"**{top_prov['provinsi']}** dengan capaian **{top_prov[indikator_spasial]:,.0f}**."
        )

        st.subheader("Peta Persebaran Kluster IMK Indonesia")

        warna_cluster = {
            "Cluster 0": "#933B5B",  
            "Cluster 1": "#AABAAE",  
            "Cluster 2": "#9F9679",  
            "Cluster 3": "#B5728A"   
        }

        m = folium.Map(location=[-2.5, 118], zoom_start=5, tiles="CartoDB positron")

        # Iterasi tiap baris data untuk menambahkan marker ke peta
        for _, row in filtered_spasial.iterrows():
            # Menentukan warna marker berdasarkan kategori cluster
            cluster_key = row["Kategori_Cluster"].split(":")[0].strip()
            hex_color = warna_cluster.get(cluster_key, "#9F9679")
            popup_content = f"""
            <div style='font-family: Inter, sans-serif; min-width: 165px; font-size: 12px;'>
                <b style='font-size:13px; color:#1E1A1A;'>{row['provinsi']}</b>
                <hr style='margin: 5px 0; border-color: #E3D6BF;'>
                <table style='width:100%; border-spacing:0;'>
                    <tr><td style='color:#9F9679; padding:3px 0;'>Tahun</td><td style='text-align:right;'>{row['tahun']}</td></tr>
                    <tr><td style='color:#9F9679; padding:3px 0;'>Output</td><td style='text-align:right;'>{row['nilai_output']:,.0f}</td></tr>
                    <tr><td style='color:#9F9679; padding:3px 0;'>Perusahaan</td><td style='text-align:right;'>{row['jumlah_perusahaan']:,.0f}</td></tr>
                    <tr><td style='color:#9F9679; padding:3px 0;'>Tenaga Kerja</td><td style='text-align:right;'>{row['jumlah_tenaga_kerja']:,.0f}</td></tr>
                </table>
                <div style='margin-top:6px; font-weight:600; color:{hex_color};'>{row['Kategori_Cluster']}</div>
            </div>
            """
            folium.CircleMarker(
                location=[row["latitude"], row["longitude"]],
                # Menentukan radius marker berdasarkan nilai indikator spasial yang dipilih
                radius=max(
                    np.log1p(row[indikator_spasial]) /
                    np.log1p(filtered_spasial[indikator_spasial].max()) * 18 + 5, 5
                ),
                popup=folium.Popup(popup_content, max_width=300),
                color=hex_color,
                fill=True,
                fill_color=hex_color,
                fill_opacity=0.75
            ).add_to(m)

        # Legenda cluster 
        legend_cluster_html = """
        <div style="
            position: fixed;
            bottom: 30px; left: 30px;
            z-index: 1000;
            background: rgba(255,255,255,0.92);
            border: 1px solid #E3D6BF;
            border-radius: 10px;
            padding: 12px 16px;
            font-family: Inter, sans-serif;
            font-size: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            min-width: 200px;
        ">
            <div style="font-weight:700; color:#1E1A1A; margin-bottom:8px; font-size:12px; letter-spacing:0.5px; text-transform:uppercase;">
                Kategori Cluster
            </div>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">
                <div style="width:14px; height:14px; border-radius:50%; background:#933B5B; flex-shrink:0;"></div>
                <span style="color:#3D2830;">Cluster 0: Raksasa IMK (Kecil Dominan)</span>
            </div>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">
                <div style="width:14px; height:14px; border-radius:50%; background:#AABAAE; flex-shrink:0;"></div>
                <span style="color:#3D2830;">Cluster 1: Produktivitas IMK Rendah</span>
            </div>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:5px;">
                <div style="width:14px; height:14px; border-radius:50%; background:#9F9679; flex-shrink:0;"></div>
                <span style="color:#3D2830;">Cluster 2: Produktivitas IMK Tinggi</span>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
                <div style="width:14px; height:14px; border-radius:50%; background:#B5728A; flex-shrink:0;"></div>
                <span style="color:#3D2830;">Cluster 3: Raksasa IMK (Mikro Dominan)</span>
            </div>
        </div>
        """
        m.get_root().html.add_child(folium.Element(legend_cluster_html))
        st_folium(m, width="100%", height=500, key="folium_cluster_map")

        st.write("---")
        st.subheader(f"Heatmap Intensitas {indikator_spasial.replace('_', ' ').title()}")

        # Membuat heatmap berdasarkan nilai indikator spasial yang dipilih
        heat_data = filtered_spasial[["latitude", "longitude", str(indikator_spasial)]].values.tolist()
        heat_map = folium.Map(location=[-2.5, 118], zoom_start=5, tiles="CartoDB positron")
        HeatMap(heat_data, radius=22, blur=15,
                gradient={0.2: "#E3D6BF", 0.5: "#B5728A", 1.0: "#933B5B"}).add_to(heat_map)
        legend_heat_html = f"""
        <div style="
            position: fixed;
            bottom: 30px; left: 30px;
            z-index: 1000;
            background: rgba(255,255,255,0.92);
            border: 1px solid #E3D6BF;
            border-radius: 10px;
            padding: 12px 16px;
            font-family: Inter, sans-serif;
            font-size: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            min-width: 180px;
        ">
            <div style="font-weight:700; color:#1E1A1A; margin-bottom:8px; font-size:12px; letter-spacing:0.5px; text-transform:uppercase;">
                Intensitas {indikator_spasial.replace('_', ' ').title()}
            </div>
            <div style="
                width: 100%;
                height: 12px;
                border-radius: 6px;
                background: linear-gradient(to right, #E3D6BF, #B5728A, #933B5B);
                margin-bottom: 4px;
            "></div>
            <div style="display:flex; justify-content:space-between; color:#9F9679; font-size:10px;">
                <span>Rendah</span>
                <span>Sedang</span>
                <span>Tinggi</span>
            </div>
        </div>
        """
        heat_map.get_root().html.add_child(folium.Element(legend_heat_html))
        st_folium(heat_map, width="100%", height=500, key="folium_heatmap")

        st.write("---")
        st.subheader("Analisis Ekstrem Daerah (Top 5 vs Bottom 5)")
        col_t1, col_t2 = st.columns(2)

        # Menampilkan tabel 5 provinsi dengan performa tertinggi dan terendah berdasarkan indikator spasial yang dipilih
        df_tabel_t1 = filtered_spasial.sort_values(indikator_spasial, ascending=False).head(5).copy()
        df_tabel_t2 = filtered_spasial.sort_values(indikator_spasial, ascending=True).head(5).copy()
        df_tabel_t1["Cluster"] = df_tabel_t1["Kategori_Cluster"].str.split(":").str[0]
        df_tabel_t2["Cluster"] = df_tabel_t2["Kategori_Cluster"].str.split(":").str[0]

        with col_t1:
            st.markdown(f"**5 Provinsi Performa Tertinggi**")
            st.dataframe(
                df_tabel_t1[["provinsi", indikator_spasial, "Cluster"]],
                use_container_width=True
            )

        with col_t2:
            st.markdown(f"**5 Provinsi Performa Terendah**")
            st.dataframe(
                df_tabel_t2[["provinsi", indikator_spasial, "Cluster"]],
                use_container_width=True
            )

        st.write("---")
        st.subheader("Profil Rata-Rata Karakteristik Kelompok")
        # Agregasi statistik rata-rata untuk setiap cluster berdasarkan indikator utama
        summary_table = (
            filtered_spasial.groupby("Kategori_Cluster")[
                ["nilai_output", "jumlah_perusahaan", "jumlah_tenaga_kerja"]
            ]
            .mean()
            .round(0)
        )
        st.dataframe(summary_table, use_container_width=True)

    else:
        st.warning("Tidak ada data yang sesuai dengan kombinasi filter cluster dan tahun yang dipilih.")