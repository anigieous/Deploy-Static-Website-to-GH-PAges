# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "/app/script.py" ]