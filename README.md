# CastAway Cruise Line Prediction App

## Overview
The **CastAway Cruise Line Prediction App** is a web application built using Streamlit that allows users to input various parameters related to cruise costs and customer satisfaction. The app interacts with a Flask API to provide predictions about customer behavior.

## Features
- User-friendly interface for inputting cruise-related data.
- Integration with a Flask API for real-time predictions.
- Data visualization capabilities (if implemented).
- Easy setup and deployment instructions.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- pip (Python package installer)
- Flask (for the backend API)
- Streamlit (for the frontend)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/castaway-cruise-prediction-app.git
   cd castaway-cruise-prediction-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
   streamlit
   requests
   scikit-learn
   pandas
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the Flask API**:
   Navigate to the directory where your Flask API code is located and install its dependencies if you have a separate `requirements.txt` for it.

## Usage

1. **Run the Flask API**:
   In the terminal, navigate to the folder containing your Flask API code and run:
   ```bash
   python app.py
   ```
   This should start the Flask server on `http://127.0.0.1:5000`.

2. **Run the Streamlit app**:
   In another terminal, navigate back to the Streamlit app directory and run:
   ```bash
   streamlit run streamlit_app.py
   ```
   This should open a new tab in your web browser with the Streamlit app.

3. **Interact with the app**:
   - Input the required parameters in the sidebar.
   - Click the "Get Prediction" button to retrieve predictions from the Flask API.

## API Integration
The app communicates with the Flask API using HTTP requests. Ensure that the API is running before you try to make predictions in the Streamlit app. The API endpoint for predictions should be set to `http://127.0.0.1:5000/predict`.

### Example API Endpoint
```python
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Process data and return prediction
    return jsonify({"prediction": "Your prediction here"})
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/segunumoru1/CastAway-Cruise-Line-Travel-Again-App-Prediction/blob/master/LICENSE) file for more details.

---
