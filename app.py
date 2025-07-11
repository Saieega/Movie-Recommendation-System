import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def load_data():
    ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])

    movie_info = pd.read_csv(
        'ml-100k/u.item',
        sep='|',
        encoding='latin-1',
        header=None,
        names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
               'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime',
               'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
               'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    )

    genre_data = movie_info.drop(['release_date', 'video_release_date', 'IMDb_URL'], axis=1)

    genre_features = genre_data.drop(['movie_id'], axis=1)
    genre_features.set_index('title', inplace=True)

    cosine_sim = cosine_similarity(genre_features.values, genre_features.values)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=genre_features.index, columns=genre_features.index)

    return genre_features, cosine_sim_df

def recommend_movies(title, sim_df, num=5):
    if title not in sim_df:
        return ["Movie not found in database."]
    
    sim_scores = sim_df[title].sort_values(ascending=False)
    recommendations = sim_scores.iloc[1:num+1].index.tolist()
    return recommendations

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommender System (Content-Based)")
st.markdown("Recommend similar movies based on genre overlap using the **MovieLens 100K** dataset.")

genre_features, cosine_sim_df = load_data()

movie_titles = genre_features.index.tolist()
selected_movie = st.selectbox("🎥 Select a movie", sorted(movie_titles))

if st.button("🔍 Recommend"):
    recommendations = recommend_movies(selected_movie, cosine_sim_df)
    st.subheader("🎯 Top 5 Recommendations:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
