from flask import Flask, request, jsonify
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the model
with open('classifier.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize LabelEncoder for room types
label_encoder = LabelEncoder()
# Define the categories for Room Type (make sure these match your training data)
room_types = ['Interior', 'Window', 'Balcony', 'Suite'] 
label_encoder.fit(room_types)

# Default route to test if the API is running
@app.route('/')
def home():
    return "Model API is Running!"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get the data from the POST request (expects JSON)
    
    # Ensure the data has the necessary features
    features = [
        data['Total Cost'],
        data['Room Costs'],
        data['Ship BoardExpenses'],
        data['Casino Expenses'],
        data['Excursion Expenses'],
        label_encoder.transform([data['Room Type']])[0],  # Convert Room Type to numerical value
        data['Average Customer Satisfaction'],
        data['Overall Trip Satisfaction']
    ]
    
    # Make prediction
    prediction = model.predict([features])
    
    # Return the prediction as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
