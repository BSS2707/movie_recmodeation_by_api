# 🎬 Movie Recommender System (TMDb + ML + Streamlit)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![TMDb](https://img.shields.io/badge/TMDb-API-green.svg)](https://www.themoviedb.org/)

An interactive **Movie Recommendation System** built for demos, classrooms, and projects.  
It combines the **TMDb API** for movie metadata, **Machine Learning (TF‑IDF + Cosine Similarity)** for recommendations, and **Streamlit** for a clean UI.

---

## 📂 Project Structure
movie-recommender/
│── app.py              # Streamlit UI
│── model.py            # ML + API logic
│── .env                # TMDb API key
│── requirements.txt    # Dependencies
│── README.md           # Documentation


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender

pip install -r requirements.txt
TMDB_API_KEY=your_tmdb_api_key_here
streamlit run app.py

