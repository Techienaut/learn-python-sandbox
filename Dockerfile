# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the src directory contents into the container at /app
COPY ./src/ /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the debug port
EXPOSE 5678

# Default to running an interactive shell
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "sandbox"]
