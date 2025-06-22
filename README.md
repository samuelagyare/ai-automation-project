# Full-Stack AI Automation Project

This project is a full-stack application that leverages an AI agentic framework to automate a specific business process. The backend is built with Python and FastAPI, the AI agent uses LangChain, and the entire application is designed for deployment on Google Cloud Platform (GCP).

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Deployment](#deployment)

## Project Overview

The goal of this MVP is to automate responses to common customer support questions. The application provides a simple web interface for user interaction and utilizes an AI agent to perform the core logic.

## Tech Stack

- **Backend:** Python, FastAPI
- **AI Agent:** LangChain, Google Gemini
- **Frontend:** React
- **Cloud Platform:** Google Cloud Platform (Cloud Run, Firebase Hosting)
- **Database:** Google Sheets API (for MVP)

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js and npm
- Git

### Installation & Running Locally

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload