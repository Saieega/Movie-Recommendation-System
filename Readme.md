# 🎬 Content-Based Movie Recommender System

This is a simple and effective **movie recommender system** built using Python and Streamlit. It recommends movies based on **genre similarity** using **content-based filtering**.

---

## 🚀 Features

* Uses the [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/)
* Recommends top 5 movies based on a selected movie
* Built with **Streamlit** for an interactive UI
* Uses **cosine similarity** to measure genre similarity between movies

---

## 🧰 Tech Stack

* Python 🐍
* Pandas 📼
* Scikit-learn 📚
* Streamlit 🚀

---

## 📁 Folder Structure

```
movie_recommender/
├── app.py               # Streamlit application
├── ml-100k/             # Dataset folder (MovieLens 100K)
│   ├── u.data
│   └── u.item
└── Readme.md
```

---

## 📌 How It Works

1. Each movie is represented as a **binary genre vector**
2. Cosine similarity is used to measure **content similarity** between movies
3. Given an input movie, the system recommends the top 5 most similar ones

---

## ✨ Future Improvements

* Add movie posters using TMDB API
* Include collaborative filtering (user-based or item-based)
* Deploy online with Streamlit Cloud or Hugging Face Spaces
* Combine content-based and collaborative filtering (hybrid model)

---

## 🙌 Acknowledgments

* [MovieLens Dataset - GroupLens](https://grouplens.org/datasets/movielens/)
* [Streamlit Docs](https://docs.streamlit.io/)
# Movie-Recommendation-System