import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load the trained model
model = joblib.load('eth_rf_model_close.pkl')

# Load the data
df = pd.read_csv('Eth_USD_18_23.csv')

# Function to preprocess the input data
def preprocess_input(date: datetime, df: pd.DataFrame) -> np.array:
    # Here, we're using the date to extract relevant features
    # This needs to match how the model was trained
    # We'll use the day as an example, but you should expand this
    day = date.day
    # Normalizing the day (you might need to do more preprocessing based on your model)
    scaler = MinMaxScaler()
    day = scaler.fit_transform(np.array(day).reshape(-1, 1))
    return day

def predict_eth_price():
    st.title('ETH Price Prediction 📈')

    st.write("""
    Use this tool to predict the closing price of Ethereum (ETH) for a specific date.
    """)

    # Input for the date
    date_to_predict = st.date_input("Choose a date", min_value=datetime.today())

    # Button to make predictions
    if st.button("Predict"):
        # Preprocess the input data
        input_data = preprocess_input(date_to_predict, df)

        # Make predictions
        prediction = model.predict(input_data)

        # Display the result
        st.success(f"The predicted closing price for Ethereum on {date_to_predict} is ${prediction[0]:.2f}.")

# Main app
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "ETH Price Prediction"])

    if selection == "Home":
        st.write("# Home Page")
        # Your home page content goes here
    elif selection == "ETH Price Prediction":
        predict_eth_price()

if __name__ == "__main__":
    main()
