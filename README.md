# Housing Price Prediction

## Overview
This project builds regression models to predict housing prices based on features like median income, number of rooms, property age, and geographic location. It uses **Linear Regression** and **Random Forest Regressor** models, with **Optuna** for hyperparameter tuning. The models are deployed in an interactive web app using **Flask** and **Streamlit**.

## Dataset
The dataset, obtained from scikit-learn, includes features such as:
- Median income
- Number of rooms
- Property age
- Geographic location

## Preprocessing
1. **Missing Values**: No missing data.
2. **Feature Scaling**: Standardized using `StandardScaler`.
3. **Train-Test Split**: 80% training, 20% testing.

## Models
- **Linear Regression**: Baseline model.
- **Random Forest Regressor**: Tuned using **Optuna** for better performance.

### Evaluation Metrics
- **Linear Regression**: RMSE = 0.71, R² = 0.81
- **Random Forest (Baseline)**: RMSE = 0.58, R² = 0.88
- **Random Forest (Tuned)**: RMSE = 0.55, R² = 0.89

## Deployment
The models are deployed using **Flask** and **Streamlit**, allowing users to input property details and receive predicted prices.

## Conclusion
The **tuned Random Forest model** achieved the best performance. An interactive web app was created to access the model for housing price predictions.

## Repository Link
[GitHub Repository](Replace with your actual repo link)

### Requirements
- Python 3.x
- `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `flask`, `streamlit`, `optuna`

### Usage
1. Clone the repo:
   ```
   git clone <repository-url>
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run Streamlit app:
   ```
   streamlit run app.py
   ```
