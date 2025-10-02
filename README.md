# 🧠 Synapse: AI Orchestration Platform

Synapse is a prototype for a powerful, human-in-the-loop AI agent designed to understand user intent, connect to various data sources and AI models, and execute complex tasks. It serves as an "agentic middleware" layer, abstracting the complexity of different tools into a unified, conversational interface.

This MVP demonstrates the core end-to-end concept: a user can provide a natural language prompt, and the agent will use an LLM to generate and execute code to perform a data analysis task.

## ✨ MVP Features

The current version of Synapse is a proof-of-concept with the following features:

*   **Web-Based UI:** A simple and user-friendly interface built with Streamlit.
*   **Natural Language Prompting:** Users can describe tasks in plain English.
*   **LLM-Powered Code Generation:** Uses Google's Gemini model to generate Python code based on the user's prompt and provided data.
*   **Local Data Analysis:** Reads a local CSV file (`data/sales_data.csv`) to use as context for the user's task.
*   **Automated Code Execution:** Runs the generated Python script to perform the requested analysis.
*   **File-Based Output:** Saves the result of the analysis to a text file (`output.txt`).

## 🚀 How to Run the MVP

Follow these steps to run the Synapse MVP on your local machine.

### Prerequisites

*   Python 3.8+
*   An active Gemini API Key. You can get one from [Google AI for Developers](https://ai.google.dev/).

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies

Install all the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Start the Backend Server

The backend is a FastAPI application that powers the agent's core logic. Run the following command in your terminal:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

The API server will now be running at `http://127.0.0.1:8000`.

### 4. Run the Frontend Application

In a **new terminal window**, run the Streamlit application:

```bash
streamlit run frontend/ui.py
```

This will open a new tab in your browser with the Synapse UI.

### 5. Use the Application

1.  When you first open the app, it will prompt you to enter your Gemini API key.
2.  Once the key is entered, the main interface will appear.
3.  Use the default prompt or write your own task in the text area.
4.  Click the "Run Agent" button and wait for the agent to complete the task.
5.  A confirmation message will appear in the UI, and the result will be saved to `output.txt` in the project's root directory.

## 📂 Project Structure

The project is organized into three main directories to keep the code modular and maintainable:

```
/
├── app/            # The core backend application (FastAPI)
│   ├── main.py     # API endpoints
│   ├── agent.py    # Core agent logic and orchestration
│   ├── connectors.py # Connects to the Gemini LLM
│   └── actions.py    # Executes the generated code
├── data/           # Sample data files for the agent
│   └── sales_data.csv
├── frontend/       # The Streamlit user interface
│   └── ui.py
└── requirements.txt  # Project dependencies
```

---

## 🗺️ Roadmap for Future Development

This MVP is just the beginning. The following roadmap outlines the next steps to evolve Synapse into a more robust and user-friendly platform.

### Phase 1: Core Enhancements & Security

These are the most critical next steps to make the platform more secure and reliable.

*   **🔒 Security Sandboxing:** The highest priority is to replace the current `subprocess` execution with a secure, sandboxed environment. **Using Docker containers** to execute the LLM-generated code is the standard best practice. This will isolate the code and prevent it from accessing the host system.
*   **📝 Improved Error Handling & Logging:** Provide more detailed feedback to the user when something goes wrong. Implement structured logging on the backend to make debugging easier.
*   **🔑 Secure Key Management:** Move away from session-based API keys to a more secure solution like **HashiCorp Vault** or a cloud provider's secret manager (e.g., AWS Secrets Manager, GCP Secret Manager).

### Phase 2: UI/UX Improvements

These features will dramatically improve the user experience and make the application more interactive.

*   **📄 Dynamic File Uploads:** Instead of relying on a hardcoded CSV file, add a file uploader to the Streamlit UI. This will allow users to upload their own data files (CSV, TXT, etc.) for analysis.
*   **📊 Display Results in the UI:** Instead of just writing to `output.txt`, parse the result and display it directly in the Streamlit interface. This could include tables, charts, or plain text summaries.
*   **🤖 Agent "Thinking" Status:** Show the user what the agent is doing at each step (e.g., "Connecting to Gemini," "Executing code," "Finalizing report"). This provides transparency and makes the process feel more interactive.
*   **💬 Conversational History:** Implement a chat-like interface where users can see the history of their requests and the agent's responses, allowing for multi-turn conversations.

### Phase 3: Expanding Agent Capabilities

This phase focuses on realizing the full vision of Synapse as a modular and extensible agentic platform.

*   **🔌 True Plugin Architecture:** Redesign the `connectors` and `actions` modules into a formal plugin system. This would allow new data sources (e.g., PostgreSQL, S3, Salesforce) and new actions (e.g., sending an email, updating a dashboard) to be added easily without modifying the core agent logic.
*   **🧠 Smarter Planner/Router:** Enhance the agent's "brain." Instead of a simple linear workflow, the agent should be able to decompose complex tasks into multiple steps and choose the right tool for each step. This is where frameworks like **LangChain** or **LlamaIndex** could be integrated.
*   **💸 Cost-Effective Model Selection:** Give the agent the ability to choose the best LLM for the job based on the complexity of the task. Simple tasks could be routed to cheaper, faster models, while complex reasoning would use more powerful ones.
*   **✅ Human-in-the-Loop Confirmation:** For potentially destructive or costly actions, have the agent present its plan to the user for approval before execution (e.g., "I am about to run a script that will update the sales database. Do you want to proceed?").