# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]
