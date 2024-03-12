# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Define environment variable
WORKDIR /app/src

# Run the application with a delay using the array format
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]

