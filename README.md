# 📰 Fake News Detection using Machine Learning

This project uses machine learning techniques to detect fake news articles based on their content. It is built using Python, with preprocessing, vectorization (TF-IDF), and classification using a Random Forest classifier.

## 📌 Project Objective

To develop a robust system that automatically classifies news articles as either **Real** or **Fake** based on their textual content.

---

## 📂 Dataset

- Source: Public dataset containing over 20,000 news articles
- Fields:
  - `id` — Unique identifier
  - `title` — Headline of the article
  - `author` — Author name
  - `text` — Full content of the article
  - `label` — 0 (Real), 1 (Fake)

---

## ⚙️ Technologies Used

- Python 3.x
- Pandas, NumPy
- Scikit-learn (TF-IDF, Random Forest)
- Flask (for Web App)
- HTML/CSS (UI for prediction)
- Jupyter Notebook

---

## 📈 Model Used

- **Random Forest Classifier**
  - Achieved **99% accuracy**
  - Chosen for its high performance and interpretability

---

## 🧪 Preprocessing Steps

- Removal of null entries
- Lowercasing text
- Removing stopwords and punctuation
- TF-IDF Vectorization

---

## 🧠 Features

- Input: News title and content
- Output: Prediction → `REAL` or `FAKE`
- Admin panel to monitor all submitted predictions
- Stores user-submitted data for future analysis

---

## 🚀 Running the Project

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/CaitlynMary/Machine-Learing-Project.git
   cd Machine-Learing-Project

