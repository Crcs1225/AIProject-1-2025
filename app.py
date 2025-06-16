from flask import Flask, request, jsonify, render_template
# Assuming util/predict.py contains the predict function and loaded_model
from util.predict import predict # Keep this import as it is

import pandas as pd # Import pandas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
# It's good practice to rename this function to avoid conflict with the imported 'predict'
def handle_predict_request(): 
    data = request.get_json(force=True)
    required_fields = [
        'Bathrooms', 'Bedrooms', 'Car Spaces',
        'Floor area (m²)', 'Land Size (m²)', 'Rooms (total)'
    ]
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f"Missing required field: '{field}'"}), 400
        if isinstance(data[field], str) and data[field].strip() == '':
            return jsonify({'error': f"Empty value for required field: '{field}'"}), 400
            
    # --- THIS IS THE CRUCIAL PART TO CHANGE ---
    # Wrap each scalar value in a list to form a single-row DataFrame
    feature_data = {
        'Bathrooms': [int(data['Bathrooms'])],
        'Bedrooms': [int(data['Bedrooms'])],
        'Car Spaces': [int(data['Car Spaces'])],
        'Floor area (m²)': [float(data['Floor area (m²)'])],
        'Land Size (m²)' : [float(data['Land Size (m²)'])],
        'Rooms (total)': [int(data['Rooms (total)'])]
    }

    # Now pd.DataFrame(feature_data) will work correctly
    input_data = pd.DataFrame(feature_data)
    
    # Call the actual prediction function from util.predict
    prediction = predict(input_data)

    return jsonify({
        'predicted_price': float(prediction)
    })
    
if __name__ == '__main__':
    app.run(debug=True)