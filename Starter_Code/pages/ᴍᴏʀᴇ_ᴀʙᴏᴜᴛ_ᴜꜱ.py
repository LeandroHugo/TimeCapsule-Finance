import streamlit as st

def run():

    # Animated Header or Logo
    # st.image("path_to_your_logo.png", use_column_width=True)  # Replace 'path_to_your_logo.png' with the path to your logo or image

    st.title('⏳ TimeLock Wallet')
    st.write("Welcome to TimeLock Wallet. This application allows you to securely store and manage your digital assets.")

    # Feature Highlights
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🔒 Security")
        st.write("Top-notch security features to ensure your digital assets are safe and encrypted.")

    with col2:
        st.subheader("⏲️ TimeLock")
        st.write("Set specific time locks on your assets, ensuring they remain inaccessible until the timer expires.")

    with col3:
        st.subheader("🔥 Deadman Switch")
        st.write("A unique feature that transfers your assets to a trusted person if you're inactive for a prolonged period.")

    # Quick Links
    st.subheader("Quick Links")
    if st.button("Go to User Dashboard"):
        # Navigate to User Dashboard
        pass
    if st.button("Go to Admin Dashboard"):
        # Navigate to Admin Dashboard
        pass

    # User Testimonials/Reviews
    st.subheader("What our users say")
    st.write("""
    "The TimeLock Wallet has changed the way I manage my cryptocurrencies. The Deadman Switch feature is a game changer!" - Alex
    """)
    st.write("""
    "I feel much safer with my digital assets now. The intuitive UI and the TimeLock feature make it my go-to wallet." - Samantha
    """)

    # FAQ Section
    if st.button("Frequently Asked Questions"):
        st.write("""
        **1. How does the TimeLock feature work?**
        The TimeLock feature allows you to lock your assets until a specified time has passed. 

        **2. What is the Deadman Switch?**
        The Deadman Switch is a feature that will transfer your assets to a designated address if you're inactive for a set period.

        **3. How can I deposit funds into the wallet?**
        Navigate to the User Dashboard and use the deposit function.
        """)

    # Footer
    st.write("---")
    st.write("""
    [Terms of Service](#) | [Privacy Policy](#) | [Support](#)
    """)  # Add actual links in place of '#' 

if __name__ == '__main__':
    run()
