import streamlit as st

# Dummy data for the sake of this example
USER_DATA = {
    "name": "John Doe",
    "wallet_address": "0xabc123...",
    "balance": 100.5
}

def run():
    st.title('👤 User Dashboard')

    # Profile Section
    st.subheader('Profile')

    # Load and display the profile picture
    uploaded_file = st.file_uploader("Upload/Change Profile Picture", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    else:
        st.image("https://www.w3schools.com/howto/img_avatar.png", caption='Default Profile Picture.', use_column_width=True)

    st.write(f"**Name:** {USER_DATA['name']}")
    st.write(f"**Wallet Address:** {USER_DATA['wallet_address']}")
    st.write(f"**Balance:** {USER_DATA['balance']} ETH")

    # File Upload
    st.subheader('Upload Documents')
    uploaded_docs = st.file_uploader("Choose a file", type=["pdf", "doc", "txt", "docx"])
    if uploaded_docs:
        for doc in uploaded_docs:
            st.write(f"Uploaded {doc.name}")

    # Tips & Best Practices
    st.subheader('Tips & Best Practices')
    st.write("""
    **Security Tips:**
    - **Private Key:** Always keep your private key secret. Never share it with anyone or store it online without encryption.
    - **Phishing:** Beware of phishing websites or emails that pretend to be the official service.
    - **Backup:** Regularly backup your wallet data.

    **Using Wallet Efficiently:**
    - **Notifications:** Use the notification feature to get alerts about your wallet status.

    **General Advice:**
    - Always double-check wallet addresses when making transactions.
    """)

    # Recent Transactions (dummy data)
    st.subheader('Recent Transactions')
    transactions = {
        'Date': ['2023-08-05', '2023-08-04', '2023-08-03'],
        'Type': ['Sent', 'Received', 'Sent'],
        'Amount': [-50, 100, -20],
        'Status': ['Completed', 'Completed', 'Pending']
    }
    st.table(transactions)

if __name__ == '__main__':
    run()
