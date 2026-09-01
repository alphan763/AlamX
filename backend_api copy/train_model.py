import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import sklearn

print(f"--- Environment Check ---")
print(f"Training using scikit-learn version: {sklearn.__version__}")
print(f"-------------------------\n")

print("1. Loading dataset...")
df = pd.read_csv("augmented_dataset.csv")

X = df.drop("prognosis", axis=1)
y = df["prognosis"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("2. Training Random Forest model...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

print("3. Evaluating model...")
predictions = rf_model.predict(X_test)
acc = accuracy_score(y_test, predictions)

print(f"\nModel Training Complete! Accuracy: {acc * 100:.2f}%\n")

joblib.dump(rf_model, "random_forest_model.pkl")
joblib.dump(list(X.columns), "feature_names.pkl")
print("Saved artifacts: 'random_forest_model.pkl' and 'feature_names.pkl'")