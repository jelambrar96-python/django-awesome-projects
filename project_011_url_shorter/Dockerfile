# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /wikipedia_app
COPY . /app/

# Expose the port that the Django app runs on
EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Define the command to run the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "url_shorter.wsgi:application"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

