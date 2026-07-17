import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Load dataset
data = pd.read_csv(
    "dataset/spam.csv",
    encoding="latin-1"
)


# Remove unnecessary columns
data = data.drop(
    columns=[
        "Unnamed: 2",
        "Unnamed: 3",
        "Unnamed: 4"
    ],
    errors="ignore"
)


# Rename columns
data.columns = ["label", "message"]


# Convert labels
data["label"] = data["label"].map(
    {
        "ham": 0,
        "spam": 1
    }
)


# Split data

X_train, X_test, y_train, y_test = train_test_split(
    data["message"],
    data["label"],
    test_size=0.2,
    random_state=42
)


# Convert text into numbers

vectorizer = TfidfVectorizer(
    stop_words="english"
)

X_train_vector = vectorizer.fit_transform(
    X_train
)

X_test_vector = vectorizer.transform(
    X_test
)


# Train model

model = MultinomialNB()

model.fit(
    X_train_vector,
    y_train
)


# Check accuracy

prediction = model.predict(
    X_test_vector
)

accuracy = accuracy_score(
    y_test,
    prediction
)

print(
    f"Model Accuracy: {accuracy*100:.2f}%"
)


# Save model

with open(
    "model/spam_model.pkl",
    "wb"
) as file:
    pickle.dump(
        model,
        file
    )


# Save vectorizer

with open(
    "model/vectorizer.pkl",
    "wb"
) as file:
    pickle.dump(
        vectorizer,
        file
    )


print("Model saved successfully!")