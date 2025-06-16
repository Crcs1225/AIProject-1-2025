import joblib
import pandas as pd # Make sure pandas is imported here too if you're using it within the predict function

# Export the model to a file
# Ensure the path is correct relative to where app.py is run or use an absolute path
try:
    loaded_model = joblib.load('model/model_RFR.joblib')
except FileNotFoundError:
    print("Error: model/model_RFR.joblib not found. Make sure the model file exists at the specified path.")
    loaded_model = None # Handle case where model isn't loaded

def predict(input_data):
    if loaded_model is None:
        return "Model not loaded. Cannot make prediction."

    try:
        # input_data is already a DataFrame from app.py
        predicted_price = loaded_model.predict(input_data)[0]

        # Ensure price is not negative
        predicted_price = max(0, predicted_price)

        print(f"\nPredicted Housing Price: {predicted_price}")
        return predicted_price
    except Exception as e:
        print(f"An error occurred during prediction: {e}")
        # Consider returning an error message or re-raising the exception
        return str(e)