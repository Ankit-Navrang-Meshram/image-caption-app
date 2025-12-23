# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
# We add --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# We don't specify a CMD here because we will specify it in docker-compose
# depending on whether this container is acting as the backend or frontend.