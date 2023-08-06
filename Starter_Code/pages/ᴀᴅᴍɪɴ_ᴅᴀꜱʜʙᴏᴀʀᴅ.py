import streamlit as st
import pandas as pd
import hashlib

# Dummy database simulation
DATABASE = {}

def send_email(to, subject, content):
    # Dummy function to represent sending an email
    st.write(f"Sending email to {to} with subject: {subject} and content: {content}")

def register_user(username, email):
    token = hashlib.sha256((username + email).encode()).hexdigest()
    DATABASE[username] = {'email': email, 'token': token, 'confirmed': False}

    confirmation_link = f"http://your_app_link/confirm?token={token}"
    send_email(email, "Please confirm your registration", f"Click this link to confirm: {confirmation_link}")

def confirm_registration(token):
    for username, data in DATABASE.items():
        if data['token'] == token:
            data['confirmed'] = True
            return username
    return None

def validate_credentials(username, password):
    return username == "admin" and password == "password123"

def load_user_data():
    data = {
        'User Address': ['0xabc...', '0xdef...', '0xghi...'],
        'Balance': [100, 200, 50],
        'Last Active': ['2023-08-05', '2023-08-04', '2023-08-06']
    }
    return pd.DataFrame(data)

def run():
    st.title('🛠️ Admin Dashboard')

    # Admin registration
    st.sidebar.header('Admin Registration')
    new_username = st.sidebar.text_input("New Username")
    email = st.sidebar.text_input("Email")

    if st.sidebar.button('Register'):
        if new_username not in DATABASE:
            register_user(new_username, email)
            st.sidebar.success('Registration successful! Check your email for confirmation link.')
        else:
            st.sidebar.error('Username already exists!')

    # Admin login feature
    st.sidebar.header('Admin Login')
    username = st.sidebar.text_input("Username", key="login_username")
    password = st.sidebar.text_input("Password", type='password', key="login_password")

    if st.sidebar.button('Login'):
        if validate_credentials(username, password):
            st.sidebar.success('Logged in successfully')
            logged_in = True
        else:
            st.sidebar.error('Invalid credentials')
            logged_in = False
    else:
        logged_in = False

    # If logged in, display the admin features
    if logged_in:
        st.subheader('User Overview')
        df = load_user_data()
        st.table(df)
        # ... rest of the admin features ...

    else:
        st.warning('Please login to access the admin dashboard.')

    # Admin Guidelines
    st.subheader('🛡️ Admin Guidelines')

    st.write("""
    **Responsibilities:**
    - **Monitor Transactions:** Regularly check the transaction history to detect any suspicious activities.
    - **User Support:** Always be ready to assist users with their queries and issues related to the TimeLock Wallet.
    - **System Health:** Ensure the system is running smoothly. Regular maintenance and updates are crucial.
    - **Security:** Always use strong, unique passwords. Regularly change your credentials and use two-factor authentication if possible.

    **Best Practices:**
    - **Backup:** Always have a backup of the system data. Regularly back up the database to prevent data loss.
    - **Updates:** Keep the system updated. Ensure that any third-party libraries or dependencies are also updated to their latest versions.
    - **Audits:** Regularly audit the system. Check for vulnerabilities and fix them immediately.

    **Tips:**
    - Always stay updated with the latest trends and threats in the crypto world.
    - Engage with the user community. Feedback can be invaluable.
    - Consider regular training or workshops to improve your skills and knowledge.
    """)

    # User Best Practices
    st.subheader('🔑 User Best Practices')

    st.write("""
    **Understanding TimeLock:**
    TimeLock Wallets, as the name suggests, allow users to lock their funds for a set period. These funds cannot be accessed until the lock duration expires. This feature can be useful for saving, vesting schedules, or simply ensuring that funds aren't spent impulsively.

    **Security Tips:**
    - **Private Key:** Always keep your private key secret. Never share it with anyone or store it online without encryption.
    - **Phishing:** Beware of phishing websites or emails that pretend to be the official TimeLock Wallet service.
    - **Backup:** Regularly backup your wallet data. Consider using hardware wallets for added security.

    **Using TimeLock Efficiently:**
    - **Set Reasonable Durations:** While it might be tempting to lock funds for a long time, always consider your financial needs and set a reasonable lock duration.
    - **Notifications:** Use the notification feature to get alerts about your wallet status.
    - **Deadman Switch:** Understand and use the Deadman Switch feature. It allows transferring funds in case of prolonged inactivity, adding a layer of safety.

    **General Advice:**
    - Always double-check wallet addresses when making transactions.
    - Stay updated with the latest features and updates from the official TimeLock Wallet announcements.
    """)

if __name__ == '__main__':
    run()
