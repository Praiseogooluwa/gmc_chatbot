import streamlit as st
from bot import predict_class, get_response
import json
import random
from PIL import Image
from io import BytesIO
import base64
import speech_recognition as sr
from microphone_component import microphone_access_component  # Custom component for microphone access
import pyttsx3  # For text-to-speech

# Load the intents from the intents.json file
with open('intents.json', 'r') as file:
    data = json.load(file)

def get_response(return_list, data_json):
    result = "Sorry, I don't have an answer to that question. Drag the sidebar to chat with one of our active Educational consultants."
    for intent in return_list:
        tag = intent['intent']
        for i in data_json['intents']:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
    return result

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        st.info("Adjusting for ambient noise, please wait...", icon="⏳")
        recognizer.adjust_for_ambient_noise(source)
        st.info("Recording, speak now...", icon="🎙️")
        audio = recognizer.listen(source)
    st.info("Recognizing speech...", icon="🧠")
    try:
        response = recognizer.recognize_google(audio)
    except sr.RequestError:
        response = "API unavailable"
    except sr.UnknownValueError:
        response = "Unable to recognize speech"
    return response

# Function to speak the response
def speak_response(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main(intents):
    st.write("Enter your message:")
    message = st.text_input("", "")
    if st.button("Send"):
        return_list = predict_class(message)
        response = get_response(return_list, data_json=intents)
        st.text_area("GMC's Response:", response, height=100)
        speak_response(response)  # Speak the response

# Open the logo image
logo_image = Image.open('logo1.png')
buffered = BytesIO()
logo_image.save(buffered, format="PNG")
logo_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

# Use the base64-encoded string in the img tag
st.markdown(f"""
<div class="navbar">
    <a href="mailto:hello@gomycode.com" target="_blank" class="nav-link">Help/Support</a>
</div>
<div class="header">
    <img src="data:image/png;base64,{logo_base64}" alt="Logo" class="logo"/>
    <h1 class="title">GOMYC<span class="highlight">O</span>DE</h1>
</div>
<div class="footer">
    Made with love by - <a href="https://praiseogooluwa.github.io/" target="_blank" class="footer-link">Praise Ogooluwa Bakare</a>
</div>
""", unsafe_allow_html=True)

st.write("#### Welcome to GMC Chatbot! Type your message below:")

# Sidebar content
st.sidebar.markdown("# Technical Coding Information")
st.sidebar.markdown("""
## Programming Languages
- Python
- JavaScript
- HTML/CSS
- SQL
""")

st.sidebar.markdown("# Contact Our Educational Consultants")

# Consultant profile
def get_consultant_image(file_path):
    image = Image.open(file_path)
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

consultants = [
    {"name": "Esther Abiona", "image": "esther.jpg", "link": "https://wa.link/8b4aht"},
    {"name": "Dele Fayemi", "image": "dele.jpeg", "link": "https://wa.link/kfpbnn"},
    {"name": "Temitope Bamidele", "image": "tope.jpeg", "link": "https://wa.link/d7gbl9"},
    {"name": "Praise Ogooluwa", "image": "praise.jpg", "link": "https://wa.link/f7tm3h"}
]

st.sidebar.markdown("### Meet Our Consultants")
for consultant in consultants:
    img_base64 = get_consultant_image(consultant["image"])
    status = "online" if consultant["name"] != "Praise Ogooluwa" else "offline"
    st.sidebar.markdown(f"""
    <div class="consultant">
        <a href="{consultant["link"]}" target="_blank">
            <img src="data:image/jpeg;base64,{img_base64}" alt="{consultant["name"]}" class="consultant-img">
        </a>
        <div>
            <strong>{consultant["name"]}</strong><br>
            <span class="status {status}"></span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("""
## Leave a Message
If you have any questions or need further assistance, feel free to
<a href="mailto:hello@gomycode.com?subject=Help%20and%20Support" class="sidebar-link" target="_blank">send a message via mail</a>.
""", unsafe_allow_html=True)

# Main app where user enters prompt and gets the response
user_input = st.text_area("You:", "", key="user_input")

# Add a microphone button
microphone_access_component()  # Custom component for requesting microphone access

if st.button("🎤"):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    try:
        user_input = recognize_speech_from_mic(recognizer, microphone)
        st.text_area("Recognized Text:", value=user_input, height=50, key="recognized_text")
        # Generate a response based on the recognized text
        return_list = predict_class(user_input)
        response = get_response(return_list, data_json=data)
        st.text_area("GMC's Response:", response, height=100)
        speak_response(response)  # Speak the response
    except OSError as e:
        st.error("No Default Input Device Available. Please connect a microphone.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

generate_button = st.button("Generate Response")

# Generate response based on user input
if generate_button and user_input.strip() != "":
    return_list = predict_class(user_input)
    response = get_response(return_list, data_json=data)
    st.text_area("GMC's Response:", response, height=100)
    speak_response(response)  # Speak the response

# Additional styling to make the app visually appealing
st.markdown("""
<style>
body {
    font-family: 'Montserrat', sans-serif;
    background-color: #ffffff;
    color: #333;
}
.stApp {
    background-color: #f9f9f9;
}
.navbar {
    display: flex;
    justify-content: flex-end;
    padding: 10px;
}
.navbar .nav-link {
    color: blue;
    text-decoration: none;
    font-family: 'Times New Roman', serif;
    font-size: 1em;
    padding: 0 15px;
}
.navbar .nav-link:hover {
    text-decoration: underline;
}
.header {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 10px;
    font-family: 'Times New Roman', serif;
    margin-bottom: 40px; /* Clearer gap from the footer */
}
.header .logo {
    width: 20%;
    max-width: 100px;
    margin-right: 15px;
}
.header .title {
    color: black;
    margin: 0;
    font-family: 'Times New Roman', serif;
    font-size: 2.5em; /* Slightly larger font size */
    flex-grow: 1;
    text-align: center;
}
.header .highlight {
    color: red;
}
.footer {
    text-align: left;
    margin-top: 20px;
}
.footer-link {
    color: blue;
    text-decoration: none;
}
.footer-link:hover {
    text-decoration: underline;
}
.consultant {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.consultant .consultant-img {
    border-radius: 50%;
    margin-right: 10px;
    cursor: pointer;
    border: 1.5px solid red;
    width: 50px;
    height: 55px;
}
.status {
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
}
.status.online {
    background-color: green;
}
.status.offline {
    background-color: grey;
}
.stTextInput>div>div>textarea {
    background-color: #ffffff;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
}
.stButton button {
    background-color: red;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
.stButton button:hover {
    background-color: darkred;
}
.stTextArea textarea {
    background-color: #ffffff;
    color: #333;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
}
.sidebar-link {
    color: blue;
    text-decoration: none;
}
.sidebar-link:hover {
    text-decoration: underline;
}
.info-message {
    margin-bottom: 0px; /* Reduce space between microphone access request and icon */
}
</style>
""", unsafe_allow_html=True)

# Run the main function
main(data)
