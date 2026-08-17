# 🌾 Crop Yield Prediction using Machine Learning

## 📌 Project Overview

Crop Yield Prediction is a Machine Learning project that predicts the expected yield of a crop based on agricultural and environmental factors such as rainfall, temperature, fertilizer usage, and pesticide usage.

The project uses a **Random Forest Regression** model to analyze the data and predict crop yield.

## 🎯 Objectives

* Predict crop yield using Machine Learning.
* Analyze the factors affecting crop production.
* Evaluate model performance using MAE and R² Score.
* Visualize actual and predicted crop yields.
* Provide yield predictions for new crop conditions.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Random Forest Regression

## 📊 Input Features

The model uses the following features:

* Crop
* Rainfall
* Temperature
* Fertilizer
* Pesticide

## 🤖 Machine Learning Model

**Random Forest Regressor** is used for predicting crop yield.

The dataset is divided into training and testing sets using an 80:20 ratio.

## 📈 Model Performance

The model achieved:

* **Mean Absolute Error (MAE): 0.0755**
* **R² Score: 0.9359**
* **R² Performance: approximately 93.59%**

## 🌾 Sample Prediction

For the given input conditions:

* Crop: Rice
* Rainfall: 1200
* Temperature: 28°C
* Fertilizer: 150
* Pesticide: 50

**Predicted Yield: 4.53**

## 📂 Project Structure

```text
Crop-Yield-Prediction/
│
├── Crop Yield.py
├── crop_yield.csv
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/pavani2006-20/Crop-Yield-Prediction.git
```

### 2. Open the project folder

```bash
cd Crop-Yield-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Python program

```bash
python "Crop Yield.py"
```

## 📊 Output

The program displays:

* Model evaluation metrics
* Predicted crop yield
* Actual vs Predicted Yield graph
* Feature Importance graph

## 🚀 Future Enhancements

* Add a larger real-world agricultural dataset.
* Add more crop and weather features.
* Build a Streamlit web application.
* Deploy the prediction system online.
* Add real-time weather data integration.

## 👩‍💻 Author

**Pavani Bathi**

GitHub: https://github.com/pavani2006-20
