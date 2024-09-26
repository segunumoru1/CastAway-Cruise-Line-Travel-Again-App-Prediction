# CastAway Cruise Line Prediction App

## Overview
The **CastAway Cruise Line Prediction App** is designed to predict customer loyalty based on various factors such as satisfaction levels, trip costs, and customer demographics. The project integrates a machine learning model to analyze the likelihood of a customer choosing the cruise line for future travel. This app uses a Flask API for backend predictions and Streamlit for the frontend interface, allowing users to interact with the prediction model in real time.

The goal of the project is to help the cruise line company make informed decisions regarding customer retention by predicting future customer behavior based on past experiences.

---

## Features
- **User-Friendly Interface**: Intuitive web app built with Streamlit.
- **Real-Time Predictions**: Predict customer loyalty based on input parameters.
- **Flask API**: Serves predictions and handles communication with the machine learning model.
- **Machine Learning Model**: Utilizes a Random Forest classifier with high accuracy for predictions.
- **Scalability**: Ready for deployment to cloud platforms like Heroku or Streamlit Cloud.

---

## Table of Contents
- [Methodology](#methodology)
  - [Data Ingestion](#data-ingestion)
  - [Data Preprocessing](#data-preprocessing)
  - [Model Development](#model-development)
  - [API Development](#api-development)
  - [Frontend Development](#frontend-development)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)
- [License](#license)

---

## Methodology

### 1. Data Ingestion
The dataset used for this project was collected from various sources, including customer demographic information, trip costs, and satisfaction scores. The data is ingested into a Python environment for further processing and analysis.

### 2. Data Preprocessing
- **Cleaning**: Missing values and outliers were addressed. Rows with incomplete or errorneous data were either filled using mean imputation technique.
- **Feature Engineering**: Categorical variables such as room types and cruise packages were encoded using label encoding. All numerical features were scaled using **Min-Max scaling** to standardize the range of input data.

### 3. Model Development
- **Model Selection**: After exploring several algorithms, including Logistic Regression, and SVM, the **Random Forest** model was chosen due to its superior performance in terms of accuracy, precision, recall, and F1-score:
  - **Accuracy**: 0.97
  - **Precision**: 0.969
  - **Recall**: 0.969
  - **F1-Score**: 0.969
- **Train-Test Split**: The data was split into training and testing sets (80%-20%) to validate the model's performance.
- **Hyperparameter Tuning**: **RandomizedSearchCV** was used for optimizing hyperparameters, yielding the best model with Best Cross-Validation Score: `0.95`
- **Model Saving**: The trained model was saved using **Pickle** for future use and deployment.

### 4. API Development
A Flask-based API was developed to serve the machine learning model predictions. The API provides a simple interface where users can send data via POST requests and receive predictions in real time.
  
### 5. Frontend Development
**Streamlit** was used to build the frontend of the application. Users can input customer information and trip details into a form, and the app communicates with the Flask API to retrieve and display predictions.

---

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/castaway-cruise-prediction-app.git
   cd castaway-cruise-prediction-app
   ```

2. **Set up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use venv\Scripts\activate
   ```

3. **Install the Required Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
   Flask
   streamlit
   scikit-learn
   pandas
   pickle-mixin
   ```
   Then install them:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask API**:
   Start the backend by running:
   ```bash
   python app.py
   ```

5. **Run the Streamlit App**:
   In a separate terminal, run the following to launch the frontend:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## Usage

1. **Open the App**: Once both Flask and Streamlit are running, navigate to `http://localhost:8501` to interact with the app.
2. **Input Data**: Use the form in the Streamlit app to input customer details such as income, age, cruise type, and satisfaction ratings.
3. **Get Predictions**: Click the "Get Prediction" button to send data to the Flask API and receive predictions about customer loyalty.

---

## Testing

Testing was performed on both the API and the machine learning model to ensure robustness:
- **Unit Tests**: Check the validity of input and output formats for the API.
- **Model Tests**: Validate the accuracy and reliability of the predictions using test datasets.

---

## Deployment

### Local Deployment
Follow the installation steps to run the app on your local machine.

### Cloud Deployment (Heroku)
1. **Install the Heroku CLI**: Follow the instructions on the [Heroku website](https://devcenter.heroku.com/articles/heroku-cli).
2. **Create `requirements.txt`**:
   ```bash
   pip freeze > requirements.txt
   ```
3. **Create a `Procfile`**:
   ```bash
   echo "web: python app.py" > Procfile
   ```
4. **Deploy the App**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku create your-app-name
   git push heroku master
   ```

---

## Future Enhancements

- **User Authentication**: Add user accounts to store previous predictions and allow customized recommendations.
- **Advanced Visualization**: Provide insights through detailed visualizations such as customer demographics trends and satisfaction analysis.
- **Model Improvements**: Incorporate additional data sources or advanced algorithms like Gradient Boosting Machines for improved predictions.

---

## Conclusion
The **CastAway Cruise Line Prediction App** successfully predicts customer loyalty based on satisfaction levels and trip costs. By integrating machine learning with Flask and Streamlit, the app provides a seamless and interactive user experience.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README is designed to ensure that users, developers, and contributors can clearly understand the structure, methodology, and purpose of the project.
