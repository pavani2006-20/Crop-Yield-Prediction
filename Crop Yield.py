import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("crop_yield.csv")

# Encode crop names
encoder = LabelEncoder()
data["Crop"] = encoder.fit_transform(data["Crop"])

# Features and target
X = data[["Crop", "Rainfall", "Temperature",
          "Fertilizer", "Pesticide"]]

y = data["Yield"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("===== CROP YIELD PREDICTION =====")
print("Mean Absolute Error:", round(mae, 4))
print("R2 Score:", round(r2, 4))
print("Accuracy:", round(r2 * 100, 2), "%")

# Actual vs Predicted graph
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual vs Predicted Crop Yield")
plt.grid(True)
plt.show()

# Feature importance
importance = model.feature_importances_

plt.figure(figsize=(8, 5))
plt.bar(X.columns, importance)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance")
plt.xticks(rotation=30)
plt.show()

# New crop prediction
crop = "Rice"

new_data = pd.DataFrame({
    "Crop": [encoder.transform([crop])[0]],
    "Rainfall": [1200],
    "Temperature": [28],
    "Fertilizer": [150],
    "Pesticide": [50]
})

result = model.predict(new_data)

print("\nCrop:", crop)
print("Predicted Yield:", round(result[0], 2))