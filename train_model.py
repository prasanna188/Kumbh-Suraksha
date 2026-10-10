
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Demo training data only — not real Kumbh data
data = {
    "crowd_count": [
        1000, 5000, 10000, 20000, 30000, 40000,
        50000, 60000, 70000, 80000, 90000, 100000,
        15000, 35000, 55000, 75000, 25000, 85000
    ],
    "temperature": [
        22, 25, 28, 30, 32, 34,
        35, 36, 38, 40, 42, 43,
        27, 33, 36, 39, 31, 41
    ],
    "density": [
        10, 15, 20, 30, 40, 50,
        60, 65, 70, 80, 90, 95,
        25, 45, 65, 85, 35, 90
    ],
    "risk": [
        0, 0, 0, 0, 0, 1,
        1, 1, 1, 2, 2, 2,
        0, 1, 1, 2, 0, 2
    ]
}

df = pd.DataFrame(data)

X = df[["crowd_count", "temperature", "density"]]
y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

with open("risk_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("ML model trained successfully!")
print(f"Demo test accuracy: {accuracy:.2%}")
print("Model saved as risk_model.pkl")