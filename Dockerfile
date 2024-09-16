#e the official Python base image with Alpine Linux 3.12
FROM python:3.9-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the entire application directory from your host to /app in the container
COPY . .

# Install Python dependencies from requirements.txt
RUN pip install -r requirement.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"]