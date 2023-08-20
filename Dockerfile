# Use an official lightweight Python image.
FROM python:3.8-slim

# Set the working directory in docker
WORKDIR /app

# Copy local code to the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available for the app
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
