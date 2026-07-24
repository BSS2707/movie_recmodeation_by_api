import streamlit as st
from model import fetch_movies, build_similarity, recommend

st.title("🎬Movie Recommender ")

query = st.text_input("Enter a keyword (e.g., sci-fi, comedy, action):")

if st.button("Fetch Movies"):
    df = fetch_movies(query)
    if not df.empty:
        for _, row in df.iterrows():
            cols = st.columns([1, 3])
            if row["poster"]:
                cols[0].image(row["poster"], width=150)
            cols[1].markdown(f"**{row['title']}** ({row['release_date']})\n⭐ {row['vote_average']}\n\n{row['overview']}")
        cosine_sim = build_similarity(df)
        selected_movie = st.selectbox("Pick a movie to get recommendations:", df["title"].values)
        if st.button("Recommend Similar Movies"):
            recs = recommend(selected_movie, df, cosine_sim)
            for _, row in recs.iterrows():
                if row["poster"]:
                    st.image(row["poster"], caption=row["title"], width=150)
                else:
                    st.write(row["title"])
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="tmdb_movies.csv",
            mime="text/csv",
        )
    else:
        st.warning("No results found. Try another keyword.")
