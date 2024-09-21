# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at 
COPY . .

# Expose the port that the Django app runs on
EXPOSE 8000

ENV DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME
ENV DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD
ENV DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL

# Run the command to create the superuser
# RUN python manage.py makemigrations && \
#     python manage.py migrate
# RUN python manage.py createsuperuser --noinput \
#     --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL \
#     --password $DJANGO_SUPERUSER_PASSWORD

# Define the command to run the Django server
CMD ["bash run.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blogging_platform.wsgi:application"]
