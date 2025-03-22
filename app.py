import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define model path
model_path = "best_random_forest_model.pkl"

# Check if the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Error: Model file '{model_path}' not found. Ensure it is in the correct directory.")

# Load the model
model = joblib.load(model_path)

@app.route('/')
def home():
    return "Welcome to the House Price Prediction API! Use the /predict endpoint."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'features' not in data:
            return jsonify({'error': "Missing 'features' key in request JSON"}), 400
        
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
