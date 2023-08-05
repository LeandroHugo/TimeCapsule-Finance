import streamlit as st
import time

# Dummy data for the sake of this example
USER_DATA = {
    "name": "John Doe",
    "wallet_address": "0x88Dae24EbC7F8a30c7eBeF7FEF6b4dcCD283e3d1",
    "balance": 100.5,
    "profile_pic": "https://www.w3schools.com/howto/img_avatar.png"
}

def validate_wallet(wallet_address):
    return wallet_address == USER_DATA["wallet_address"]

def run():
    st.title('👤 User Dashboard')

    # Sidebar for user profile
    st.sidebar.header("User Profile 📸")

    # Attempt to retrieve the wallet address from session_state
    wallet_address = st.session_state.get("wallet_address", "")

    if wallet_address:  # If logged in
        st.sidebar.image(USER_DATA["profile_pic"], caption='Profile Picture', width=150)

        uploaded_file = st.sidebar.file_uploader("Upload/Change Profile Picture", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            st.sidebar.image(uploaded_file, caption='Uploaded Image.', width=150)
        else:
            st.sidebar.image("https://www.w3schools.com/howto/img_avatar.png", caption='Default Profile Picture.', width=150)

        st.sidebar.write(f"**Name:** {USER_DATA['name']}")
        st.sidebar.write(f"**Wallet Address:** {USER_DATA['wallet_address']}")
        st.sidebar.write(f"**Balance:** {USER_DATA['balance']} ETH 💰")

        # Fun features:
        col1, col2, col3 = st.columns([1, 2, 1])
        col1.markdown("### Welcome to my app!")
        col1.write("Here is some info on the app.")

        def change_photo_state():
            st.session_state["photo"] = "done"

        if "photo" not in st.session_state:
            st.session_state["photo"] = "not done"

        uploaded_photo = col2.file_uploader("Upload a photo", on_change=change_photo_state)
        camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

        if st.session_state["photo"] == "done":
            progress_bar = col2.progress(0)
            for perc_completed in range(100):
                time.sleep(0.05)
                progress_bar.progress(perc_completed + 1)
            col2.success("Photo uploaded successfully!")

        col3.metric(label="Temperature", value="60 °C", delta="3 °C")

        with st.expander("Click to read more"):
            st.write("Hello, here are more details on this topic that you were interested in.")

        if uploaded_photo is not None:
            st.image(uploaded_photo)
        elif camera_photo is not None:
            st.image(camera_photo)

        if st.sidebar.button("Logout"):
            del st.session_state["wallet_address"]

    else:
        input_wallet_address = st.sidebar.text_input("Enter Wallet Address 🔒")
        if st.sidebar.button("Login"):
            if validate_wallet(input_wallet_address):
                st.session_state["wallet_address"] = input_wallet_address
                st.sidebar.success("Logged in successfully! ✅")
            else:
                st.sidebar.error("Invalid wallet address! ❌")

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
