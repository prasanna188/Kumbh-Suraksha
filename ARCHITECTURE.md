# Kumbh Suraksha – System Architecture

## 1. Project Overview
Kumbh Suraksha is a web-based prototype designed to demonstrate disaster preparedness and crowd-risk awareness during Kumbh Mela.

## 2. System Components
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python and Flask
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas
- **Map Visualization:** Leaflet and OpenStreetMap
- **Model File:** risk_model.pkl

## 3. System Workflow
1. The user opens the website.
2. Flask serves the requested webpage.
3. The user explores crowd monitoring, maps, analytics, and prediction pages.
4. The prediction module uses the trained machine-learning model and input features to demonstrate risk prediction.
5. Results are displayed on the website.

## 4. Data Flow
User → Web Interface → Flask Backend → Prediction Model → Result Display

## 5. Limitations
The current prototype uses sample data. Predictions are for demonstration only and must not be used for real emergency decisions. Real-world deployment requires validated data, testing, and authorized emergency-service integration.