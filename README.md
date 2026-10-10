# Kumbh Suraksha – Smart Disaster Mitigation System

## About the Project
Kumbh Suraksha is a student project designed to demonstrate how technology can support disaster preparedness and crowd safety during large gatherings like the Kumbh Mela.

## Problem Statement
Managing massive crowds during the Kumbh Mela can create safety risks and make emergency response difficult.

## Key Features
- Crowd risk prediction using Machine Learning
- Crowd monitoring dashboard
- Interactive map using Leaflet and OpenStreetMap
- Risk analytics and visualizations
- Emergency alerts interface

## Technologies Used
- Python
- Flask
- Pandas
- Scikit-learn
- HTML, CSS and JavaScript
- Leaflet and OpenStreetMap

## Machine Learning
A Random Forest model demonstrates crowd-risk prediction using sample data. Predictions are for demonstration purposes only.

## Project Structure
- `app.py` – Flask application
- `train_model.py` – Model training script
- `risk_model.pkl` – Saved machine learning model
- `templates/` – HTML pages
- `static/` – Images and other assets
- `requirements.txt` – Project dependencies

## How to Run Locally
1. Install Python.
2. Run `pip install -r requirements.txt`.
3. Run `python app.py`.
4. Open `http://127.0.0.1:5000` in your browser.

## Limitations
This is a student prototype using sample data. It is not intended for real-world emergency decisions.

## Future Scope
- Integration with reliable real-time crowd data
- GPS-based crowd monitoring
- Improved risk prediction using real-world datasets
- Integration with official emergency services
