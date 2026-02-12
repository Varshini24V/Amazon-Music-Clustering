**Amazon Music Clustering**

The objective of this project is to automatically group similar songs based on their audio characteristics using unsupervised machine learning clustering techniques. By analyzing patterns in musical features, the system organizes songs into meaningful clusters that support music recommendation, playlist generation, and user experience enhancement.

**Project Objective**

The primary goal is to segment songs into coherent clusters that capture underlying musical similarities. These clusters enable:
  Improved music recommendations
  Smarter playlist curation
  Enhanced song discovery
  Actionable listening pattern insights

**Dataset Overview**

The dataset contains comprehensive song-level and artist-level metadata.

🔹 Columns:
id_songs, name_song, popularity_songs, duration_ms, explicit,
id_artists, release_date, danceability, energy, key,
loudness, mode, speechiness, acousticness, instrumentalness,
liveness, valence, tempo, time_signature, followers, genres,
name_artists, popularity_artists

**Feature Selection**

🔹 Selected Numerical Features for Clustering:

    danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms

🔹 Text Fields:

    track_id, track_name, artist_name

**Clustering Technique**

🔹 K-Means Clustering

    K-Means is used to partition the dataset into distinct clusters, grouping songs with similar audio patterns. 
    The optimal number of clusters is determined using:

      Elbow Method
      Silhouette Score

**Evaluation Metrics**

🔹 Silhouette Score - Measures how similar a song is to its own cluster compared to other clusters.
Higher score ⇒ better cluster separation.

🔹 Davies-Bouldin Index - Measures average similarity between each cluster and its most similar cluster.
Lower score ⇒ better clustering performance.

🔹 Inertia (K-Means Objective Function) - Measures within-cluster compactness.
Lower inertia ⇒ tighter clusters.
