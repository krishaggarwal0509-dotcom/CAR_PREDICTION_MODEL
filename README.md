Readme · MDCar Price Predictor 🚗

A machine learning web application that predicts the resale price of a used car based on its company, model, manufacturing year, fuel type, and kilometers driven. Built with Flask and a Linear Regression model trained using scikit-learn.

Features


Predicts used car prices instantly based on user input
Dynamic dropdowns — selecting a company auto-populates its available models
Clean, simple single-page interface (Bootstrap + vanilla JS, no page reloads)
Lightweight Flask backend serving a pre-trained ML pipeline


Tech Stack


Backend: Flask (Python)
ML/Data: scikit-learn, pandas, NumPy
Frontend: HTML, CSS, Bootstrap 4, vanilla JavaScript
Model: Linear Regression with One-Hot Encoding (via ColumnTransformer + Pipeline)


How It Works


The user selects a car company, model, year of purchase, and fuel type, and enters the kilometers driven.
The frontend sends this data asynchronously to the /predict route.
Flask loads the pre-trained model pipeline and feeds the input through it.
The pipeline one-hot encodes the categorical features (name, company, fuel_type) and passes everything to the linear regression model.
The predicted price is returned and displayed on the page without a reload.


Model Training

The model was trained on a cleaned dataset of used car listings. Key preprocessing steps:


Removed noisy/inconsistent rows (non-numeric years, malformed prices, etc.)
Extracted only the first three words of car names for consistency
One-hot encoded categorical features: name, company, fuel_type
Selected the best-performing train/test split via r2_score across multiple random states
Final pipeline: ColumnTransformer (One-Hot Encoding) → LinearRegression


The full training workflow is documented in the accompanying Jupyter notebook.

Author

Krish Aggarwal

License

This project is open source and available for educational and personal use.
