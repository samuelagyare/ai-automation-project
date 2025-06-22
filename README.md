## Full-Stack AI Automation Project
This project is a full-stack application that leverages an AI agent to provide intelligent, conversational responses. The backend is built with Python and FastAPI, the AI agent uses the LangChain framework to connect to Google's Gemini models, and the frontend is a responsive chat interface built with React. The entire application is deployed on the Google Cloud Platform.

✅ Live Application
Frontend (Firebase Hosting): https://ai-automation-project-463709.web.app

Backend API (Cloud Run): https://ai-automation-backend-685273303639.europe-west1.run.app

Demo
![app-demo gif](https://github.com/user-attachments/assets/74184478-c666-41c5-a077-b378ee65160d)

Key Features
Conversational AI: Engage in natural, human-like conversations powered by Google's Gemini model.

Live & Publicly Accessible: Fully deployed on Google Cloud Platform, accessible to anyone in the world.

Robust Backend: Built with FastAPI, the Python backend is fast, scalable, and includes interactive API documentation.

CI/CD Ready: The backend is containerized with Docker, ready for automated build and deploy pipelines.

Secure API Key Management: API keys are handled securely as environment variables in the cloud, not in the code.

CORS Enabled: The backend is configured to securely accept requests from the deployed frontend.

Architecture Diagram
The application follows a standard, scalable cloud architecture.

+-----------------------------------+      HTTPS Request (POST)      +---------------------------------+
|                                   | (api/agent, handled by browser)|                                 |
|    React Frontend                 |------------------------------->|   FastAPI Backend               |
| (Hosted on Firebase)              |                                | (Container on Google Cloud Run) |
|                                   |<-------------------------------|                                 |
+-----------------------------------+         JSON Response          +----------------+----------------+
                                                                                      |
                                                                                      | API Call (Secure)
                                                                                      v
                                                                        +-------------+---------------+
                                                                        |                             |
                                                                        | Google Gemini AI Service    |
                                                                        |      (Cloud API)            |
                                                                        +-----------------------------+

Tech Stack
Backend: Python, FastAPI

AI Framework: LangChain, langchain-google-genai

LLM Provider: Google Gemini (gemini-1.5-flash-latest)

Frontend: React.js

Cloud Deployment:

Backend: Google Cloud Run, Artifact Registry, Cloud Build

Frontend: Firebase Hosting

Containerization: Docker

Local Development Setup
Prerequisites
Python 3.10+

Node.js 16+ and npm

Git

Google Cloud SDK (gcloud)

Firebase CLI (firebase-tools)

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

# Install dependencies from the requirements file
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

Deployment
This project is configured for deployment on the Google Cloud Platform.

Backend (Cloud Run):

Build the container: From the backend directory, run gcloud builds submit --tag [REGION]-docker.pkg.dev/[PROJECT_ID]/[REPO_NAME]/[IMAGE_NAME].

Deploy the image: Run gcloud run deploy [SERVICE_NAME] --image ... --set-env-vars="GOOGLE_API_KEY=...".

Frontend (Firebase Hosting):

Initialize Firebase: From the frontend directory, run firebase init.

Build the React App: Run npm run build.

Deploy to Firebase: Run firebase deploy.