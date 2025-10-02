from fastapi import FastAPI
from pydantic import BaseModel
from .agent import run_agent

# Initialize the FastAPI app
app = FastAPI(
    title="Synapse Agent API",
    description="An API for the Synapse AI Orchestration Platform MVP.",
    version="0.1.0",
)

class AgentRequest(BaseModel):
    """Defines the structure of the request body for the /execute endpoint."""
    prompt: str
    api_key: str

@app.get("/")
def read_root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the Synapse Agent API. Use the /execute endpoint to run a task."}

@app.post("/execute")
async def execute_task(request: AgentRequest):
    """
    This endpoint receives a prompt and an API key, runs the agent,
    and returns the result of the task execution.
    """
    print(f"Received request with prompt: {request.prompt}")

    # Run the agent with the user's prompt and API key
    result = run_agent(request.prompt, request.api_key)

    print(f"Agent finished. Sending back result: {result}")

    return {"result": result}