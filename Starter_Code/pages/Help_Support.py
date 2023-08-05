import streamlit as st

def run():

    st.title('🆘 Help & Support')

    # FAQs
    st.subheader("Frequently Asked Questions")
    faq_expander = st.expander("View FAQs")
    with faq_expander:
        st.write("""
        **1. How does the TimeLock feature work?**
        The TimeLock feature allows you to lock your assets until a specified time has passed.

        **2. What is the Deadman Switch?**
        The Deadman Switch is a feature that will transfer your assets to a designated address if you're inactive for a set period.

        **3. How can I deposit funds into the wallet?**
        Navigate to the User Dashboard and use the deposit function.
        """)

    # Contact Information
    st.subheader("Contact Information")
    st.write("""
    **Email**: support@timelockwallet.com
    **Phone**: +1 (123) 456-7890
    **Live Chat**: [Click here to start a chat](#)
    """)

    # Guides & Tutorials
    st.subheader("Guides & Tutorials")
    st.write("Check out our video tutorials and how-to guides below:")
    # Replace '#' with actual links to your guides or video tutorials
    st.write("[How to use TimeLock Wallet](#)")
    st.write("[Setting up Deadman Switch](#)")
    st.write("[Depositing and Withdrawing Funds](#)")

    # Troubleshooting
    st.subheader("Troubleshooting")
    troubleshoot_expander = st.expander("Common Issues & Solutions")
    with troubleshoot_expander:
        st.write("""
        **Issue**: I can't access my funds even after the timer expired.
        **Solution**: Ensure that your account is verified and you've completed all security checks. If the issue persists, contact support.

        **Issue**: My Deadman Switch did not activate.
        **Solution**: Ensure that the inactivity period was actually surpassed and that you've set up the switch correctly.
        """)

    # Feedback Form
    st.subheader("Feedback & Issue Reporting")
    st.write("Your feedback is invaluable to us. Please let us know if you have any suggestions or if you're facing any issues.")
    feedback = st.text_area("Enter your feedback or issue here...")
    if st.button("Submit"):
        # Logic to handle the feedback, e.g., sending an email or storing in a database
        st.success("Thank you for your feedback!")

if __name__ == '__main__':
    run()
