import streamlit as st
import pickle
import string
import re

# Load the saved model 
with open('spam_classifier_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer (2).pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text

# Streamlit UI
st.set_page_config(page_title="SMS Spam Detector", layout="centered")
st.title("📩 SMS Spam Detection App")
st.markdown("Enter an SMS message below to check if it's **spam** or **ham (not spam)**.")

# User input
user_input = st.text_area("Type or paste your message here:", height=150)

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to classify.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        
        if prediction == 1:
            st.error("🚨 This message is likely **SPAM**.")
        else:
            st.success("✅ This message is **HAM** (not spam).")

