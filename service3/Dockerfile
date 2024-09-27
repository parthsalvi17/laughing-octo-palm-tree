# service1/Dockerfile

# Use official Python image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install dependencies, including Gunicorn
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the current directory contents into the container at /app
COPY . .

# Expose the Flask port
EXPOSE 5013

# Run the Flask app with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5013", "app:app"]
