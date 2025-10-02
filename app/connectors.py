import os
import google.generativeai as genai

def get_gemini_model(api_key: str):
    """
    Initializes and returns the Gemini client using the provided API key.
    """
    if not api_key:
        raise ValueError("API key for Gemini is required.")

    genai.configure(api_key=api_key)
    # Corrected model name based on the output of list_models.py
    model = genai.GenerativeModel('models/gemini-pro-latest')
    return model

def generate_code_with_gemini(prompt: str, api_key: str):
    """
    Sends a prompt to the Gemini model and returns the generated code.
    It also cleans up the response to extract only the Python code.
    """
    try:
        model = get_gemini_model(api_key)
        response = model.generate_content(prompt)

        # Basic cleanup to extract code from markdown blocks if they exist.
        code = response.text.strip()
        if code.startswith("```python"):
            code = code[len("```python"):].strip()
        if code.endswith("```"):
            code = code[:-len("```")].strip()

        return code
    except Exception as e:
        print(f"An error occurred while calling Gemini API: {e}")
        # Return a descriptive error message to be displayed on the frontend
        return f"Error: Could not connect to the Gemini API. Please check your API key and network connection. Details: {e}"