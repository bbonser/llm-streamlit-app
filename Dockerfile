# Use an official Python runtime as a parent image
FROM python:3.12.0rc2-slim-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run main.py when the container launches
CMD ["streamlit", "run", "main.py"]
