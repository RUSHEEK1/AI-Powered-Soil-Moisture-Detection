# AI-Powered-Soil-Moisture-Detection

Soil Moisture Predictor is a web-based application that predicts soil moisture levels based on user-input parameters such as date, location (latitude & longitude), temperature, humidity, sand content, and auxiliary soil moisture data.
It also recommends suitable crops based on the predicted soil moisture percentage.
🚀 Features
    Predict soil moisture percentage (sm_tgt) using a trained machine learning model
    Recommend crops based on predicted soil moisture levels
    Interactive and user-friendly web interface
    Real-time predictions with dynamic result display
    Built with Flask (backend) and vanilla HTML/CSS/JavaScript (frontend)

🛠️ Tech Stack
    Frontend: HTML5, CSS3, JavaScript (Fetch API)
    Backend: Python (Flask)
    Machine Learning: scikit-learn (joblib for model loading)
⚙️ Setup Instructions

Follow these steps to run the project locally:

  Clone the repository:

    git clone https://github.com/yourusername/soil-moisture-predictor.git
    cd soil-moisture-predictor

  Create a virtual environment (recommended):
    
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

  Install the required packages:
    
    pip install requirements.txt
    
  Make sure the trained model (soil_moisture_model.pkl) is placed in the project root directory.
    
  Run the Flask application:
    
    python app.py

  💬 Future Improvements

  -> Deploy the application using Heroku, Render, or AWS
  
  -> Add user authentication and save past predictions

  -> Integrate real-time weather APIs for automatic temperature and humidity inputs

  -> Build a dashboard for visualizing soil moisture trends
