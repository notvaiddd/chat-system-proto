# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn
import uuid

# Import your existing services.
# This works when you run the app from the project's root directory.
from app.services.gemini_service import GeminiService
from app.database import Database   

# --- Pydantic Models for Request/Response ---
# By defining these models, FastAPI handles request validation and serialization automatically.
class ChatRequest(BaseModel):
    """Defines the structure of the incoming request body for the /chat endpoint."""
    prompt: str = Field(..., description="The user's prompt for the AI model.", min_length=1)
    user_id: Optional[str] = Field(None, description="An optional unique identifier for the user.")

class ChatResponse(BaseModel):
    """Defines the structure of the response body for the /chat endpoint."""
    user_id: str
    response: str

# --- Application Setup ---
# Initialize the FastAPI application
app = FastAPI(
    title="Chat API",
    description="An API for interacting with a generative AI model.",
    version="1.0.0"
)

# --- Service Initialization ---
# Create instances of our services. These will be available for the app's lifecycle.
# In a more advanced setup, you might use FastAPI's dependency injection system.
print("Initializing services...")
gemini_service = GeminiService()
db_service = Database()
print("Services initialized.")

# --- API Endpoints ---
@app.get("/", summary="Health Check")
def read_root():
    """
    A simple health check endpoint to confirm the server is running.
    """
    return {"status": "API is running"}

@app.post("/chat", response_model=ChatResponse, summary="Generate AI Response")
async def chat(request: ChatRequest):
    """
    The main chat endpoint. It accepts a prompt, generates a response using
    the Gemini service, logs the interaction, and returns the response.
    """
    user_id = request.user_id if request.user_id else str(uuid.uuid4())
    print(f"\nReceived prompt from user '{user_id}': '{request.prompt}'")

    # --- Core Logic ---
    # 1. Generate a response using the Gemini service
    response_text = gemini_service.generate_text(request.prompt)

    # Check for errors from the Gemini service
    if response_text.startswith("Error:"):
        # HTTPException is the standard way to return HTTP errors in FastAPI
        raise HTTPException(status_code=500, detail=response_text)

    # 2. Log the conversation to the database
    log_success = db_service.log_conversation(user_id, request.prompt, response_text)
    if not log_success:
        # If logging fails, we still return the response but can note the issue server-side.
        print("Warning: Failed to log conversation to the database.")

    # 3. Return the response to the client
    # FastAPI will automatically convert this Pydantic model to a JSON response.
    return ChatResponse(user_id=user_id, response=response_text)

# --- Application Runner ---
if __name__ == '__main__':
    # This block allows running the app directly with `python main.py`
    # It will start a Uvicorn server for development.
    # For production, it's recommended to run Uvicorn directly:
    # uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    uvicorn.run(app, host='0.0.0.0', port=8000)
