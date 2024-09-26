import streamlit as st
import requests
import pickle
from sklearn.preprocessing import LabelEncoder

# Set page configuration
st.set_page_config(page_title="CastAway Cruise Line Travel Again Prediction App", layout="wide")

# Add a title and subtitle
st.title("🚣🏻 CastAway Cruise Line Travel Again Prediction App")
st.subheader("Get predictions from our Flask API")

# Create a sidebar for user inputs
st.sidebar.header("User Input Features")

# Add input fields for user data
total_cost = st.sidebar.number_input("Total Cost", min_value=0.0, max_value=5000.0)
room_costs = st.sidebar.number_input("Room Costs", min_value=0.0, max_value=500.0)
ship_board_expenses = st.sidebar.number_input("Ship Board Expenses", min_value=0.0, max_value=500.0)
casino_expenses = st.sidebar.number_input("Casino Expenses", min_value=0.0, max_value=500.0)
excursion_expenses = st.sidebar.number_input("Excursion Expenses", min_value=0.0, max_value=500.0)

# Room Type selection
room_type = st.sidebar.selectbox("Room Type", ['Interior', 'Window', 'Balcony', 'Suite'])

average_customer_satisfaction = st.sidebar.number_input("Average Customer Satisfaction (1-5)", min_value=1, max_value=5)
overall_trip_satisfaction = st.sidebar.number_input("Overall Trip Satisfaction (1-5)", min_value=1, max_value=5)

# Add a button to make predictions
if st.sidebar.button("Get Prediction"):
    # Prepare the data for the POST request
    data = {
        "Total Cost": total_cost,
        "Room Costs": room_costs,
        "Ship BoardExpenses": ship_board_expenses,
        "Casino Expenses": casino_expenses,
        "Excursion Expenses": excursion_expenses,
        "Room Type": room_type,
        "Average Customer Satisfaction": average_customer_satisfaction,
        "Overall Trip Satisfaction": overall_trip_satisfaction
    }
    
    # Make a request to the Flask API
    response = requests.post('http://127.0.0.1:5000/predict', json=data)
    
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Prediction: {prediction['prediction']}")
    else:
        st.error("Failed to get prediction")

# Button to fetch data from Flask
if st.button('Get Data from Flask'):
    response = requests.get('http://127.0.0.1:5000/api/data')
    if response.status_code == 200:
        data = response.json()
        st.success(data["message"])
    else:
        st.error("Failed to retrieve data")

# Add some styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        border: None;
        border-radius: 5px;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

# Add an image or logo
st.image("logo.png", width=200)  # Ensure you have a logo.png file in your project directory

# Add footer
st.markdown("---")
st.markdown("Made with ❤️ by [Segun Umoru]")
