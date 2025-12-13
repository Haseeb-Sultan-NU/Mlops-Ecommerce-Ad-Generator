# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# 1. Install Dependencies
# We point to the file location relative to the Project Root
COPY src/api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# 2. Copy the API Code
COPY src/api/app.py .

# 3. Copy the Trained Model
# Since we are building from the root, we can access 'model_output' directly
COPY model_output /app/model_output

# Expose the API port
EXPOSE 8000

# Start the API server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
