import streamlit as st
import streamlit.components.v1 as components

def microphone_access_component():
    # Define the HTML + JavaScript for the custom component
    html_string = """
    <!DOCTYPE html>
    <html>
    <head>
        <script>
            async function requestMicrophoneAccess() {
                try {
                    await navigator.mediaDevices.getUserMedia({ audio: true });
                    window.parent.postMessage({ type: 'microphone_access', status: 'granted' }, '*');
                } catch (err) {
                    window.parent.postMessage({ type: 'microphone_access', status: 'denied' }, '*');
                }
            }
            window.onload = requestMicrophoneAccess;
        </script>
    </head>
    <body>
        <p>Requesting microphone access...</p>
    </body>
    </html>
    """
    components.html(html_string, height=100)

