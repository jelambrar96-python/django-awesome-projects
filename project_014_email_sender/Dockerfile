# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Django app runs on
EXPOSE 8000


# Copy the current directory contents into the container at /app
COPY . /app/

# Change ownership of the /app directory to appuser
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser


# Make entrypoint.sh and run.sh executable
RUN chmod +x /app/run.sh

# Define the command to run the Django server
ENTRYPOINT [ "./run.sh" ]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "email_sender.wsgi:application"]
