import streamlit as st
import requests
import os

# --- Configuration ---
API_URL = "http://127.0.0.1:8000/execute"

# --- Helper Functions ---
def get_api_key():
    """
    Gets the Gemini API key from the user.
    Uses session_state to avoid asking for the key on every rerun.
    """
    if 'api_key' not in st.session_state or not st.session_state['api_key']:
        st.header("Enter Your Gemini API Key")
        api_key = st.text_input("API Key", type="password", help="Your key is not stored permanently.")
        if st.button("Save Key"):
            if api_key:
                st.session_state['api_key'] = api_key
                st.success("API Key saved for this session.")
                st.rerun() # Rerun to show the main app
            else:
                st.error("Please enter a valid API key.")
        return None
    return st.session_state['api_key']

def call_agent_api(prompt: str, api_key: str):
    """
    Calls the FastAPI backend to run the agent.
    """
    try:
        response = requests.post(API_URL, json={"prompt": prompt, "api_key": api_key})
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to connect to the backend API. Is it running? Details: {e}"}

# --- Streamlit App ---
st.set_page_config(page_title="Synapse MVP", layout="wide")

st.title("🧠 Synapse MVP")
st.caption("A modular, human-in-the-loop agent to execute complex tasks.")

# 1. Get API Key
api_key = get_api_key()

# 2. If API key is available, show the main application
if api_key:
    st.header("Describe the task you want to perform")

    prompt = st.text_area(
        "Enter your prompt here:",
        "Read the sales data and calculate the total revenue. Save the result to output.txt.",
        height=100
    )

    if st.button("Run Agent"):
        if not prompt:
            st.warning("Please enter a prompt.")
        else:
            with st.spinner("🤖 The agent is thinking and at work..."):
                result_data = call_agent_api(prompt, api_key)

            st.subheader("Agent's Final Report")
            if "result" in result_data:
                st.code(result_data["result"], language="text")
            elif "error" in result_data:
                st.error(result_data["error"])
            else:
                st.error("An unknown error occurred.")
else:
    st.info("Please enter your Gemini API key to begin.")