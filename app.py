
from flask import Flask, request, jsonify
from predict import predict

flask_app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    if not data or 'input' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    required_fields = [
            'Bathrooms', 'Bedrooms', 'Car Spaces',
            'Floor area (m²)', 'Land Size (m²)', 'Rooms (total)'
    ]
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({'error': f"Missing required field: '{field}'"}), 400
        # Basic check for empty strings, common from frontend forms
        if isinstance(data[field], str) and data[field].strip() == '':
            return jsonify({'error': f"Empty value for required field: '{field}'"}), 400
    feature_data = {
            'Bathrooms': int(data['Bathrooms']),
            'Bedrooms': int(data['Bedrooms']),
            'Car Spaces': int(data['Car Spaces']),
            'Floor area (m²)': float(data['Floor area (m²)']),
            'Land Size (m²)': float(data['Land Size (m²)']),
            'Rooms (total)': int(data['Rooms (total)'])
        }

    # Simulate a prediction process
    input_data = pd.DataFrame(data[feature_data])
    prediction = predict(input_data)

    return jsonify({'prediction': prediction}), 200