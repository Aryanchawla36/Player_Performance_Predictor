import joblib
import pandas as pd

# Load the saved model
model = joblib.load('linear_regression_model.pkl')

# New data for prediction (only input features)
new_data = pd.DataFrame({
    'temperature': [75, 60],
    'humidity': [50, 70],
    'wind_mph': [5, 10]
})

# Ensure column order matches the training features
new_data = new_data[['temperature', 'humidity', 'wind_mph']]

# Predict home and away scores
predictions = model.predict(new_data)

# Print results
for i, pred in enumerate(predictions):
    print(f"Game {i+1} - Predicted Home Score: {pred[0]:.2f}, Predicted Away Score: {pred[1]:.2f}")