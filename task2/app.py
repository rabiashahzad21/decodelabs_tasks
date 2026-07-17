import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)


# ---------------- TITLE ----------------

st.title("📧 Spam Email Classifier")
st.write(
    "Enter an email message below and the AI model will predict "
    "whether it is Spam or Not Spam."
)

st.divider()


import pickle


# ---------------- LOAD SAVED MODEL ----------------

@st.cache_resource
def load_model():

    model = pickle.load(
        open(
            "model/spam_model.pkl",
            "rb"
        )
    )

    vectorizer = pickle.load(
        open(
            "model/vectorizer.pkl",
            "rb"
        )
    )

    return model, vectorizer


model, vectorizer = load_model()






# ---------------- SIDEBAR ----------------

st.sidebar.header("📊 Model Information")

st.sidebar.write(
    "Model: Multinomial Naive Bayes"
)

st.sidebar.write(
    "Accuracy: Calculated during training"
)

st.sidebar.write(
    """
    Algorithm:
    
    ✅ TF-IDF Vectorizer
    
    ✅ Multinomial Naive Bayes
    
    ✅ Supervised Learning
    """
)



# ---------------- INPUT SECTION ----------------


email = st.text_area(
    "✉️ Enter Email Text",
    placeholder="Example: Congratulations! You won a free prize..."
)


st.write("")


# ---------------- PREDICTION ----------------


if st.button(
    "🔍 Predict",
    use_container_width=True,
    key="predict_button"
):

    if email.strip() == "":
        st.warning(
            "Please enter an email message."
        )

    else:

        # Convert text into numbers
        email_vector = vectorizer.transform(
            [email]
        )


        prediction = model.predict(
            email_vector
        )


        if prediction[0] == 1:

            st.error(
                "🚨 This Email is SPAM"
            )

            st.write(
                "The message looks suspicious."
            )


        else:

            st.success(
                "✅ This Email is NOT SPAM"
            )

            st.write(
                "The message looks safe."
            )



# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Built using Python, Machine Learning & Streamlit"
)