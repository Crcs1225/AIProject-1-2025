import joblib

# Export the model to a file
loaded_model = joblib.load('model_RFR.joblib')

def predict(input_data):
    
    try:
        predicted_price = loaded_model.predict(input_data)[0]

        # Ensure price is not negative
        predicted_price = max(0, predicted_price)

        print(f"\nPredicted Housing Price: {predicted_price}")
        return predicted_price
    except Exception as e:
        print(f"An error occurred during prediction: {e}")
        return str(e)