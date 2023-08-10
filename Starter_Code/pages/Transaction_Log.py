import streamlit as st
import pandas as pd  # Assuming you'll use a pandas DataFrame for the transaction data

def load_transaction_data(user_address):
    # For demonstration purposes, let's create dummy data. 
    # In a real-world scenario, you'd fetch this data from your backend or the blockchain.
    data = {
        'Transaction Type': ['Deposit', 'Withdrawal', 'Transfer', 'Deposit'],
        'Date & Time': ['2023-08-05 10:10', '2023-08-06 11:15', '2023-08-07 14:20', '2023-08-08 09:05'],
        'Amount': [100, 50, 30, 150],
        'Status': ['Completed', 'Completed', 'Pending', 'Completed'],
        'Transaction Hash': ['0xabc...', '0xdef...', '0xghi...', '0xjkl...']
    }
    return pd.DataFrame(data)

def run():
    st.title('📜 Transaction History')

    # Allow user to input/select their address
    user_address = st.text_input('Enter your wallet address:', value='0x...')

    # Load transaction data
    df = load_transaction_data(user_address)

    # Filters
    transaction_type = st.selectbox('Filter by Transaction Type', ['All'] + list(df['Transaction Type'].unique()))
    if transaction_type != 'All':
        df = df[df['Transaction Type'] == transaction_type]

    # Display data
    st.table(df)

    # Export option
    if st.button('Export as CSV'):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        href = f'<a href="data:file/csv;base64,{b64}" download="transaction_history.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

    # Additional Information
    st.write(f"Total Transactions: {len(df)}")
    st.write(f"Total Amount Deposited: {df[df['Transaction Type'] == 'Deposit']['Amount'].sum()}")
    st.write(f"Total Amount Withdrawn: {df[df['Transaction Type'] == 'Withdrawal']['Amount'].sum()}")

if __name__ == '__main__':
    run()
