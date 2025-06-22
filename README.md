## Full-Stack AI Automation Project
This project is a full-stack application that leverages an AI agent to provide intelligent, conversational responses. The backend is built with Python and FastAPI, the AI agent uses the LangChain framework to connect to Google's Gemini models, and the frontend is a responsive chat interface built with React.

Demo


Key Features
Conversational AI: Engage in natural, human-like conversations powered by Google's Gemini model.

Real-time Interaction: A responsive React frontend provides a seamless, real-time chat experience.

Robust Backend: Built with FastAPI, the Python backend is fast, scalable, and includes interactive API documentation.

Modular Agent Logic: Uses LangChain to structure and orchestrate interactions with the LLM, making it easy to extend.

Ready for Deployment: The entire stack is configured and prepared for deployment on Google Cloud Platform.

Architecture Diagram
The application follows a simple, robust client-server architecture.

+----------------------+         HTTP Request (POST /api/agent)         +--------------------+
|                      |   (User's question as JSON: {"input": "..."})   |                    |
|    React Frontend    |------------------------------------------------>|   FastAPI Backend  |
| (on localhost:3000)  |                                                 | (on localhost:8000)|
|                      |<------------------------------------------------|                    |
+----------------------+      JSON Response (AI's answer as string)      +---------+----------+
                                                                                  |
                                                                                  | 1. LangChain receives input
                                                                                  | 2. Passes it to the LLM
                                                                                  v
                                                                        +---------+----------+
                                                                        |                    |
                                                                        | Google Gemini AI   |
                                                                        |   (Cloud API)      |
                                                                        +--------------------+

Tech Stack
Backend: Python, FastAPI

AI Framework: LangChain, langchain-google-genai

LLM Provider: Google Gemini (gemini-1.5-flash-latest)

Frontend: React.js

Development Server: Uvicorn

Cloud Platform: Designed for Google Cloud Platform (Cloud Run, Firebase Hosting)

Getting Started
Prerequisites
Python 3.10+

Node.js 16+ and npm

Git

A Google AI API Key

Installation & Running Locally
1. Clone the repository:

git clone <your-repo-url>
cd ai-automation-project

2. Backend Setup:

cd backend

# Create and activate virtual environment
python -m venv venv
# On Windows: .\\venv\\Scripts\\activate
# On macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your API key
# GOOGLE_API_KEY="your-key-here"

# Run the backend server
uvicorn main:app --reload

The backend will be running at http://127.0.0.1:8000.

3. Frontend Setup (in a new terminal):

cd frontend

# Install dependencies
npm install

# Run the frontend server
npm start

The frontend will open automatically at http://localhost:3000.