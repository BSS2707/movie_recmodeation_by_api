import os
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_IMG_URL = "https://image.tmdb.org/t/p/w200"

def fetch_movies(query, page=1):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={query}&page={page}&include_adult=false"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        return pd.DataFrame()
    movies = []
    if "results" in data:
        for m in data['results']:
            movies.append({
                "id": m.get("id"),
                "title": m.get("title"),
                "release_date": m.get("release_date", ""),
                "vote_average": m.get("vote_average", 0),
                "overview": m.get("overview", ""),
                "poster": BASE_IMG_URL + m["poster_path"] if m.get("poster_path") else None
            })
    return pd.DataFrame(movies)

def build_similarity(df):
    if df.empty:
        return None
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["overview"].fillna(""))
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(title, df, cosine_sim):
    if df.empty or cosine_sim is None:
        return []
    if title not in df['title'].values:
        return []
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    movie_indices = [i[0] for i in sim_scores]
    return df.iloc[movie_indices]
