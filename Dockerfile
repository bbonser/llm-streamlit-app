# Use an official Python runtime as a parent image
FROM python:3.10.6

# Set the working directory in the container to /app
WORKDIR /app

RUN git clone https://github.com/bbonser/llm-streamlit-app

RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run main.py when the container launches
CMD ["streamlit", "run", "main.py"]