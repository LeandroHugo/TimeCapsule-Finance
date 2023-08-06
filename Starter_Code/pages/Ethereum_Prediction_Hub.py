import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load the trained models
price_model = joblib.load('eth_rf_model_close.pkl')
rf_model_complex = joblib.load('rf_model_complex.pkl')
rf_model_simple = joblib.load('rf_model_simple.pkl')

# Load the data
df = pd.read_csv('Eth_USD_18_23.csv')

# Function to preprocess the input data for price prediction
def preprocess_input(date: datetime, df: pd.DataFrame) -> np.array:
    day = date.day
    scaler = MinMaxScaler()
    day = scaler.fit_transform(np.array(day).reshape(-1, 1))
    return day

def predict_eth_price():
    st.title('ETH Price Prediction 📈')
    st.write("Use this tool to predict the closing price of Ethereum (ETH) for a specific date.")
    date_to_predict = st.date_input("Choose a date", min_value=datetime.today())
    if st.button("Predict"):
        input_data = preprocess_input(date_to_predict, df)
        prediction = price_model.predict(input_data)
        st.success(f"The predicted closing price for Ethereum on {date_to_predict} is ${prediction[0]:.2f}.")

def predict_eth_trend():
    st.title('ETH Price Trend Prediction 📉📈')
    st.write("Use this tool to predict the price trend of Ethereum (ETH) for a specific date.")
    # Assuming latest_data fetch and preprocessing is done here...
    pred_complex, pred_simple = get_ethereum_predictions(latest_data)
    st.subheader('Predicted Ethereum Trend:')
    if pred_complex[0] == 1:
        st.write("Based on complex model: Expected Upward Trend")
    else:
        st.write("Based on complex model: Expected Downward Trend")
    if pred_simple[0] == 1:
        st.write("Based on simple model: Expected Upward Trend")
    else:
        st.write("Based on simple model: Expected Downward Trend")

# Main app
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "ETH Price Prediction", "ETH Trend Prediction"])
    if selection == "Home":
        st.write("# Home Page")
    elif selection == "ETH Price Prediction":
        predict_eth_price()
    elif selection == "ETH Trend Prediction":
        predict_eth_trend()

if __name__ == "__main__":
    main()
