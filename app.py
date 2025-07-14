
import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.title("📰 Fake News Detection")
st.markdown("Enter a news article below to check if it's **REAL** or **FAKE**.")

# Input text box
user_input = st.text_area("🖊️ Paste the news content here", height=200)

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        transformed_text = vectorizer.transform([user_input])
        prediction = model.predict(transformed_text)[0]

        if prediction == "FAKE":
            st.error("🚨 This news is predicted to be **FAKE**.")
        else:
            st.success("✅ This news is predicted to be **REAL**.")
