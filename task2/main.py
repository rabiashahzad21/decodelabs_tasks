# ============================
# Spam Email Classifier
# DecodeLabs Project 2
# ============================

# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
# ============================
# Step 1: Load the Dataset
# ============================

data = pd.read_csv("dataset/spam.csv", encoding="latin-1")

# ============================
# Step 2: Remove Unnecessary Columns
# ============================

data = data.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"])

# ============================
# Step 3: Rename Columns
# ============================

data.columns = ["label", "message"]

# ============================
# Step 4: Display Dataset
# ============================

print("First 5 Rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

# ============================
# Step 5: Separate Features and Labels
# ============================

X = data["message"]      # Email messages
y = data["label"]        # Spam or Ham

print("\nFirst 5 Messages:")
print(X.head())

print("\nFirst 5 Labels:")
print(y.head())

# ============================
# Step 6: Convert Text into Numbers (TF-IDF)
# ============================

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

print("\nShape of Vectorized Data:")
print(X.shape)

# ============================
# Step 7: Split Dataset
# ============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)# ============================
# Step 8: Train the Model
# ============================

model = MultinomialNB()

model.fit(X_train, y_train)

print("\nModel trained successfully!")

# ============================
# Step 9: Test the Model
# ============================

# Predict labels for testing data
y_pred = model.predict(X_test)

print("\nPredictions completed!")
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")
# ============================
# Step 10: Predict Custom Message
# ============================

user_message = input("\nEnter an email/message: ")

# Convert the message into TF-IDF features
user_data = vectorizer.transform([user_message])

# Predict
prediction = model.predict(user_data)

print("\nPrediction:")

if prediction[0] == "spam":
    print("🚨 This message is SPAM.")
else:
    print("✅ This message is HAM (Not Spam).")