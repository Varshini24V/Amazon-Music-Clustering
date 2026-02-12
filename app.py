import streamlit as st
import pandas as pd

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="🎵 Music Recommendation System",
    layout="wide"
)

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

DATA_PATH = r"C:\Users\Varshini V\OneDrive\Documents\VS_code\venv\Amazon Music Clustering\clustered_final.csv"

df = load_data(DATA_PATH)

# -------------------- PLAYLIST GENERATOR --------------------
def generate_playlist(song_type, top_n):
    playlist = (
        df[df['cluster_label'] == song_type]
        .sort_values(by='popularity_songs', ascending=False)
        .head(top_n)[['genres','release_date','followers','popularity_songs', 'duration_ms']]
        .reset_index(drop=True)
    )
    return playlist

# -------------------- UI --------------------
st.title("🎵 Music Recommendation System")

# Sidebar Controls
st.sidebar.header("Recommendation Controls")
song_type = st.sidebar.selectbox("Select Playlist Song type", sorted(df['cluster_label'].unique()))
top_n = st.sidebar.number_input("Number of Tracks", 5, 50, 20)

# KPI Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Tracks", len(df))
col2.metric("Clusters", df['cluster_label'].nunique())
col3.metric("Genres", df['genres'].nunique())

# Playlist Section
st.subheader(" Auto Playlist Generator")

if st.sidebar.button("Generate Playlist"):
    playlist = generate_playlist(song_type, top_n)
    
    st.success(f"Generated **{song_type}** playlist with **{len(playlist)} tracks**")
    st.dataframe(playlist, use_container_width=True)

    # Download option
    csv = playlist.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Playlist",
        csv,
        file_name=f"{song_type}_playlist.csv",
        mime="text/csv"
    )
