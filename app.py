from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load trained model
model = joblib.load('soil_moisture_model.pkl')

def recommend_crop(moisture_percent):
    """Recommend crops based on soil moisture percentage"""
    if moisture_percent < 30:
        return "Millet, Sorghum, Groundnut"
    elif 30 <= moisture_percent < 60:
        return "Maize, Cotton, Sunflower"
    else:
        return "Paddy, Sugarcane, Jute"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Validate and convert input data
        input_data = np.array([[
            float(data['lat']),
            float(data['lon']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['sand_content']),
            float(data['sm_aux']),
            int(data['date'].split('-')[1]),  # Month
            int(data['date'].split('-')[2])   # Day
        ]]).reshape(1, -1)

        # Predict and format results
        moisture = model.predict(input_data)[0] * 100
        return jsonify({
            'prediction': f"{moisture:.2f}%",
            'crops': recommend_crop(moisture)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)