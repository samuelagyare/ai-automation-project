import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 1. NEW IMPORT
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- 1. SETUP ---
# Load environment variables from the .env file
load_dotenv()

# Check if the Google API Key is set
if "GOOGLE_API_KEY" not in os.environ:
    print("Error: GOOGLE_API_KEY not found in .env file.")
    exit()

# Initialize our FastAPI app
app = FastAPI(
    title="AI Automation Agent API",
    description="An API for an AI agent that can automate tasks.",
    version="0.1.0",
)

# --- 2. NEW: CONFIGURE CORS ---
# Define the list of allowed origins.
# We include localhost for local testing and "*" to allow any domain,
# which is acceptable for this public-facing portfolio project.
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "*" # Allows all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)


# --- 3. THE AI AGENT LOGIC ---
# Initialize the Large Language Model (LLM)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.7)

# Define the prompt template for our agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the user's question clearly and concisely."),
    ("user", "{input}")
])

# Create the agent chain by chaining the prompt, the LLM, and an output parser
# The output parser simply converts the LLM's message object into a string
agent_chain = prompt | llm | StrOutputParser()


# --- 4. API ENDPOINTS ---
# Define a simple health check endpoint
@app.get("/api/health", tags=["Health Check"])
def health_check():
    """Check if the API is running."""
    return {"status": "ok"}

# Define the endpoint for our AI agent
@app.post("/api/agent", tags=["AI Agent"])
def run_agent(request: dict):
    """
    Receives a user query and returns the AI agent's response.
    Expects a JSON payload with a key 'input'.
    e.g., {"input": "What is the capital of France?"}
    """
    user_input = request.get("input")
    if not user_input:
        return {"error": "Input text is required."}, 400

    # Run the agent chain with the user's input
    response = agent_chain.invoke({"input": user_input})

    return {"response": response}

# --- 5. RUN THE APP (for deployment) ---
# This block allows the script to be run directly by the container
# It reads the port from the environment variable provided by Cloud Run
if __name__ == "__main__":
    import uvicorn
    # Get the port from the environment variable, defaulting to 8000 for local dev
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
