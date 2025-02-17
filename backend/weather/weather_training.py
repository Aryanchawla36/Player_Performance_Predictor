from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
import pandas as pd
import math
import joblib

weather_data = pd.read_csv('datasets\cleaned_weather_data.csv')

X = weather_data[['temperature', 'humidity', 'wind_mph']]
y = weather_data[['home_score', 'away_score']]  # Target: home team score
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)

print(f"MAE: {mae}, RMSE: {rmse}")

joblib.dump(model, 'linear_regression_model.pkl')
print("Model saved successfully.")