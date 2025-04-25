# 📱 SMS Spam Detection

A machine learning web app that classifies SMS messages as **Spam** or **Not Spam** using natural language processing (NLP). The app is built with **Streamlit** and deployed on **Hugging Face Spaces**.

---
## 🚀 Live Demo

👉 [Click here to use the app](https://huggingface.co/spaces/ADITHYAPOOJARI/sms)  
---

## 📌 Features

- Input any SMS message and get a prediction.
- Clean, simple, and responsive user interface.
- Built using:
  - **Python**
  - **scikit-learn**
  - **Natural Language Processing (NLP)**
  - **Streamlit**
  - **Hugging Face Spaces**

---

## 🧠 Model Details

- Model: **Multinomial Naive Bayes**
- Dataset: Provided in the git repo
- Preprocessing:
  - Lowercasing
  - Removing stop words
  - Stemming
  - Vectorization using **TF-IDF**

---

## 🛠️ How It Works

1. User enters an SMS message.
2. The input is preprocessed using standard NLP techniques.
3. The model classifies the message as **Spam** or **Not Spam**.
4. Output is displayed instantly on the Streamlit interface.

---

## 🖼️ App Preview

![image](https://github.com/user-attachments/assets/152e9d94-0061-4a48-a38a-20dd3c6ecb69)


---

## 📂 File Structure

```bash
├── app.py                 # Main Streamlit app
├── spam classifier model.pkl              # Trained machine learning model
├── tfidf vectorizer (2).pkl         # TF-IDF vectorizer
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
