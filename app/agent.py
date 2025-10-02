import os
from .connectors import generate_code_with_gemini
from .actions import execute_python_code

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'sales_data.csv')

def create_prompt(user_query: str, csv_data: str) -> str:
    """
    Creates a detailed prompt for the LLM, including the user's query,
    the CSV data, and instructions for the expected output.
    """
    prompt = f"""
    You are an expert data analyst. Your task is to write a Python script to answer the user's question based on the provided data.

    User's Question:
    "{user_query}"

    Data (from sales_data.csv):
    ---
    {csv_data}
    ---

    Instructions:
    1.  Write a Python script that performs the requested analysis.
    2.  The script MUST NOT attempt to read 'sales_data.csv'. The data is already provided above.
    3.  The script should save its final result to a file named `output.txt`. For example, if calculating total sales, the script should write the final number to `output.txt`.
    4.  Do not include any explanation or markdown formatting in your response. Only provide the raw Python code.
    5.  The script must be self-contained and not require any external libraries that are not part of the standard Python library, unless it is pandas.
    """
    return prompt.strip()

def run_agent(user_query: str, api_key: str) -> str:
    """
    Runs the agent to process a user query from start to finish.
    """
    # 1. Read the local CSV data
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            csv_data = f.read()
    except FileNotFoundError:
        return "Error: The data file 'data/sales_data.csv' was not found."

    # 2. Create the prompt for the LLM
    prompt = create_prompt(user_query, csv_data)

    # 3. Call the Gemini connector to get the Python code
    generated_code = generate_code_with_gemini(prompt, api_key)

    if generated_code.startswith("Error:"):
        # If there was an error from the Gemini API, return it directly
        return generated_code

    # 4. Execute the generated code
    execution_result = execute_python_code(generated_code)

    # 5. Return the final result
    return f"Agent task finished.\n{execution_result}"