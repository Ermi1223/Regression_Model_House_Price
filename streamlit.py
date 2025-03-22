import joblib
import numpy as np
import streamlit as st

# Load the trained model
model = joblib.load('best_random_forest_model.pkl')

st.title("🏠 House Price Prediction Model Application")

# Create input fields for 8 features
features = []
features.append(st.number_input("Feature 1 (Example: Median Income)", value=8.3252))
features.append(st.number_input("Feature 2 (Example: House Age)", value=41))
features.append(st.number_input("Feature 3 (Example: Average Rooms)", value=6.984))
features.append(st.number_input("Feature 4 (Example: Average Bedrooms)", value=1.023))  # Example additional feature
features.append(st.number_input("Feature 5 (Example: Population)", value=322))
features.append(st.number_input("Feature 6 (Example: Households)", value=2.555))  # Example additional feature
features.append(st.number_input("Feature 7 (Example: Latitude)", value=37.88))
features.append(st.number_input("Feature 8 (Example: Longitude)", value=-122.23))

# Button to predict price
if st.button("Predict Price"):
    # Convert features into a numpy array and reshape for the model
    prediction = model.predict(np.array(features).reshape(1, -1))
    st.success(f"🏡 Predicted House Price: ${prediction[0]:,.2f}")
