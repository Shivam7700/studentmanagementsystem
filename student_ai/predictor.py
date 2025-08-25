import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "grade_model.pkl")

def train_model():
    # Example dataset (replace with real Student DB values later)
    data = pd.DataFrame({
        "attendance": [80, 60, 95, 70, 85, 50],
        "assignments": [75, 50, 90, 60, 80, 45],
        "previous_score": [70, 55, 92, 65, 83, 40],
        "final_grade": [72, 58, 93, 67, 84, 42]
    })

    X = data[["attendance", "assignments", "previous_score"]]
    y = data["final_grade"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)
    print("✅ Model trained and saved at", MODEL_PATH)

def predict_grade(attendance, assignments, previous_score):
    if not os.path.exists(MODEL_PATH):
        train_model()

    model = joblib.load(MODEL_PATH)
    prediction = model.predict([[attendance, assignments, previous_score]])
    return round(prediction[0], 2)