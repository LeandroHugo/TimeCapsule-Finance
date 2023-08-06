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

# Basic FAQ bot logic using predefined Q&A
def faq_bot_response(user_input):
    faq_responses = {
        "timelock": "The TimeLock feature allows you to lock your assets until a specified time has passed.",
        "deadman switch": "The Deadman Switch is a feature that will transfer your assets to a designated address if you're inactive for a set period.",
        "deposit funds": "Navigate to the User Dashboard and use the deposit function."
    }
    for key, value in faq_responses.items():
        if key in user_input.lower():
            return value
    return "Sorry, I don't have an answer for that. Please try rephrasing your question or ask another one."

# FAQ Chatbot Section
st.header("FAQ Chatbot")
user_input = st.text_input("Ask me about TimeLock, Deadman Switch, and more!")
if st.button("Ask"):
    response = faq_bot_response(user_input)
    st.write(f"Answer: {response}")

# Pre-defined FAQ Section
st.header("Frequently Asked Questions")
faq_dict = {
    "How does the TimeLock feature work?": "The TimeLock feature allows you to lock your assets until a specified time has passed.",
    "What is the Deadman Switch?": "The Deadman Switch is a feature that will transfer your assets to a designated address if you're inactive for a set period.",
    "How can I deposit funds into the wallet?": "Navigate to the User Dashboard and use the deposit function."
}

selected_question = st.selectbox("Choose a question:", list(faq_dict.keys()))
st.write(f"**{selected_question}**")
st.write(faq_dict[selected_question])

    # Footer
st.write("---")
st.write("""
    [Terms of Service](#) | [Privacy Policy](#) | [Support](#)
    """)  # Add actual links in place of '#'

if __name__ == '__main__':
    run()
