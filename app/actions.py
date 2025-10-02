import subprocess
import sys

def execute_python_code(code: str):
    """
    Executes a string of Python code and returns the output.
    For the MVP, this uses the system's Python interpreter directly.

    Args:
        code: A string containing the Python code to execute.

    Returns:
        A string containing the output of the execution (stdout and stderr).
    """
    try:
        # We use subprocess to run the code in a separate process, which is slightly
        # safer than `exec()` as it won't share the same memory space.
        # It's still not a true sandbox, but it's a reasonable MVP compromise.
        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True,
            text=True,
            timeout=30  # Add a timeout to prevent long-running code
        )

        if result.returncode == 0:
            return f"Execution successful.\nOutput:\n{result.stdout}"
        else:
            return f"Execution failed.\nError:\n{result.stderr}"

    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out after 30 seconds."
    except Exception as e:
        return f"An unexpected error occurred during code execution: {e}"