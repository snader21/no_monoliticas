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
ENV FLASK_APP=./src/app.py

# Run the application with a delay using the array format
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3000"]
