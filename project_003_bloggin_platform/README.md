# Django Blogging Platform

This is a blogging platform built using Django that allows users to create, publish, and manage blog posts. It also provides an image gallery for each blog post. The project includes a user-friendly interface, administrative functions, and can be easily deployed using Docker and Docker Compose.

## Features

- Create, edit, and delete blog posts.
- Display blog posts in a gallery with images.
- Manage blog posts through the Django admin interface.
- Easily deployable using Docker Compose.
  
## Prerequisites

Before running this project, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.x (if running without Docker)
- [Pipenv](https://pypi.org/project/pipenv/) (optional, for virtual environment management)

## Setting Up the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/jelambrar96-python/django-awesome-projects
cd django-awesome-projects
cd project_003_bloggin_platform
```

### Step 2: Create a `.env` file

Create a `.env` file in the project root directory with the following content:

```bash
# Django Secret Key
DJANGO_SECRET_KEY="your_django_secret_key"

# Django Debug Mode: True or False
DJANGO_DEBUG=True

DJANGO_SUPERUSER_USERNAME=your_django_username
DJANGO_SUPERUSER_PASSWORD=your_django_password
DJANGO_SUPERUSER_EMAIL=your_django_email@django.com
```

Replace `your-secret-key`configuration with your own values.

### Step 3: Build and run the project with Docker Compose

Ensure Docker is running and then execute the following command:

```bash
docker-compose --env-file .env build
docker-compose --env-file .env up
```

### Step 6: Access the application

You can now access the application in your browser at `http://localhost:8000`.

To access the admin panel, go to `http://localhost:8000/admin` and log in using the superuser credentials.

## Directory Structure

- `gallery/`: Contains the Django app for the blogging platform.
- `templates/`: Contains the HTML files for rendering the blog list, details, editing, and deleting.
- `static/`: Static files like CSS, JavaScript, and images.
- `Dockerfile`: Used to create the Docker image for the project.
- `docker-compose.yml`: Configuration for Docker Compose, setting up the web and database services.

## Available Commands

To run the development server (if not using Docker):

```bash
python manage.py makegrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## Credits
This project is based on the tutorial "[Weather App using Django | Python](https://www.geeksforgeeks.org/blogging-platform-using-django/)" by GeeksforGeeks.

## License
This project is licensed under the MIT License.
