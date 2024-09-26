from flask import Flask, request, jsonify
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the model
try:
    with open('classifier.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    raise Exception("Model file 'classifier.pkl' not found. Please check the path.")

# Initialize LabelEncoder for room types
label_encoder = LabelEncoder()
room_types = ['Interior', 'Window', 'Balcony', 'Suite']
label_encoder.fit(room_types)

# Default route to test if the API is running
@app.route('/')
def home():
    return "Model API is Running!"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    required_features = [
        'Total Cost',
        'Room Costs',
        'Ship BoardExpenses',
        'Casino Expenses',
        'Excursion Expenses',
        'Room Type',
        'Average Customer Satisfaction',
        'Overall Trip Satisfaction'
    ]

    for feature in required_features:
        if feature not in data:
            return jsonify({'error': f'Missing feature: {feature}'}), 400

    try:
        features = [
            data['Total Cost'],
            data['Room Costs'],
            data['Ship BoardExpenses'],
            data['Casino Expenses'],
            data['Excursion Expenses'],
            label_encoder.transform([data['Room Type']])[0],
            data['Average Customer Satisfaction'],
            data['Overall Trip Satisfaction']
        ]
        
        prediction = model.predict([features])
        return jsonify({'prediction': int(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# New GET endpoint to fetch data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Data fetched successfully!"})

if __name__ == '__main__':
    app.run(debug=True)