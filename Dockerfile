# Use official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the API server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
