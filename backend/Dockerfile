# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container at /app
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
# --no-cache-dir makes the image smaller
# --upgrade pip upgrades the installer first
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# 5. Copy the rest of the backend application's code into the container at /app
COPY . .

# 6. Expose port 8000 for FastAPI. Cloud Run will use this.
EXPOSE 8000

# 7. Define the command to run your app using uvicorn
# This will be run when the container starts
CMD ["python", "main.py"]