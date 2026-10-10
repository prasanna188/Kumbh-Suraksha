
from flask import Flask, render_template, request, session
import pickle
import pandas as pd
from datetime import datetime

app = Flask(__name__)
app.secret_key = "kumbh-suraksha-demo-key"

# Load trained demo model
with open("risk_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/features")
def features():
    return render_template("features.html")


@app.route("/crowd")
def crowd():
    return render_template("crowd.html")


@app.route("/map")
def safety_map():
    return render_template("map.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    result = None
    error = None

    if request.method == "POST":
        try:
            crowd_count = int(request.form["crowd_count"])
            temperature = float(request.form["temperature"])
            density = float(request.form["density"])

            if (
                crowd_count < 0
                or temperature < 0
                or not 0 <= density <= 100
            ):
                raise ValueError

            inputs = pd.DataFrame(
                [[crowd_count, temperature, density]],
                columns=["crowd_count", "temperature", "density"]
            )

            risk = int(model.predict(inputs)[0])

            risk_labels = {
                0: "LOW RISK",
                1: "MEDIUM RISK",
                2: "HIGH RISK"
            }

            result = risk_labels.get(risk, "UNKNOWN RISK")

            # Store the latest demo prediction in the session
            session["latest_prediction"] = {
                "risk": result,
                "crowd_count": crowd_count,
                "temperature": temperature,
                "density": density,
                "time": datetime.now().strftime("%d-%m-%Y %I:%M %p")
            }

        except (ValueError, KeyError):
            error = "Please enter valid numeric values."

    return render_template(
        "prediction.html",
        result=result,
        error=error
    )


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route("/emergency")
def emergency():
    latest_prediction = session.get("latest_prediction")
    return render_template(
        "emergency.html",
        latest_prediction=latest_prediction
    )


if __name__ == "__main__":
    app.run(debug=True)
