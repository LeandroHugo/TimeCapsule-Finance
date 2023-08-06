import streamlit as st
from streamlit_elements import elements, mui, html
import time
import replicate
import os

# Basic chatbot logic using predefined Q&A
def basic_bot_response(user_input):
    responses = {
        "hello": "Hello! How can I assist you?",
        "how are you": "I'm just a bot, so I don't have feelings, but thanks for asking! How can I help you?",
        "bye": "Goodbye! If you have more questions, feel free to ask.",
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that. Please try again.")

def chatbot_page():
    st.title("Basic Chatbot Assistant 🤖")
    st.write("Ask me anything!")

    user_input = st.text_input("You: ", key="userInput")
    if st.button("Send"):
        response = basic_bot_response(user_input)
        st.write(f"Bot: {response}")

# App title
st.set_page_config(page_title="🦙💬 Llama 2 Chatbot")

# Replicate Credentials
with st.sidebar:
    st.title('🦙💬 Llama 2 Chatbot')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api) == 40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')
os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
                        input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                "temperature": 0.1, "top_p": 0.9, "max_length": 512, "repetition_penalty": 1})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)

# Link to the basic chatbot page
if st.sidebar.button("Go to Basic Chatbot"):
    chatbot_page()




def photo_upload_widget():
    """
    Function to handle photo upload widget and its associated operations.
    """
    if "photo" not in st.session_state:
        st.session_state["photo"] = "not_done"

    col1, col2, col3 = st.columns([1, 2, 1])

    # Displaying introduction and info
    col1.markdown("# Welcome to my app!")
    col1.markdown("Here is some info on the app.")

    # Function to change photo state
    def change_photo_state():
        st.session_state["photo"] = "done"

    # Upload or take a photo
    uploaded_photo = col2.file_uploader("Upload a photo", on_change=change_photo_state)
    camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

    # Progress bar after photo is chosen
    if st.session_state["photo"] == "done":
        progress_bar = col2.progress(0)
        for perc_completed in range(100):
            time.sleep(0.05)  # Simulating some processing time
            progress_bar.progress(perc_completed + 1)
        col2.success("Photo uploaded successfully!")

    # Displaying a metric
    col3.metric(label="Temperature", value="60 °C", delta="3 °C")

    # Additional info in an expander
    with st.expander("Click to read more"):
        st.write("Hello, here are more details on this topic that you were interested in.")

    # Display the chosen photo
    if uploaded_photo is not None:
        st.image(uploaded_photo, caption="Uploaded Photo", use_column_width=True)
    elif camera_photo is not None:
        st.image(camera_photo, caption="Camera Photo", use_column_width=True)


def streamlit_elements_demo():
    """
    Function to showcase various Streamlit Elements.
    """
    # Displaying Typography
    with elements("new_element"):
        mui.Typography("Hello world with Typography!")

    # Displaying Button with Multiple Children
    with elements("multiple_children"):
        mui.Button(
            mui.icon.EmojiPeople,
            mui.icon.DoubleArrow,
            "Button with multiple children"
        )

    # Nested Children
    with elements("nested_children"):
        with mui.Paper:
            with mui.Typography:
                html.p("Hello world")
                html.p("Goodbye world")

    # Adding Properties to an Element
    with elements("properties"):
        with mui.Paper(elevation=3, variant="outlined", square=True):
            mui.TextField(
                label="My text input",
                defaultValue="Type here",
                variant="outlined",
            )

    # Applying Custom CSS Styles
    with elements("style_mui_sx"):
        mui.Box(
            "Some text in a styled box",
            sx={
                "bgcolor": "background.paper",
                "boxShadow": 1,
                "borderRadius": 2,
                "p": 2,
                "minWidth": 300,
            }
        )

    # Callbacks to Retrieve Element's Data
    with elements("callbacks_retrieve_data"):
        if "my_text" not in st.session_state:
            st.session_state.my_text = ""

        def handle_change(event):
            st.session_state.my_text = event.target.value

        mui.Typography(st.session_state.my_text)
        mui.TextField(label="Input some text here", onChange=handle_change)


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Choose Page", ["Home", "Photo Upload Widget", "Streamlit Elements Demo"])

    if selection == "Home":
        st.title("Home Page")
        st.write("Welcome to the home page of this Streamlit app!")

    elif selection == "Photo Upload Widget":
        st.title("Photo Upload Widget")
        photo_upload_widget()

    elif selection == "Streamlit Elements Demo":
        st.title("Streamlit Elements Demo")
        streamlit_elements_demo()



if __name__ == "__main__":
    main()
