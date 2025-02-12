# microservice-update-user

This project is a microservice created with Python and FastAPI that allows you to update user information in a database. The service is configured to run inside a Docker container, making it easy to deploy and portable.

## Technologies Used
- Python 3.9+
- FastAPI
- Docker
- MySQL (for the database)
- SQLAlchemy (ORM)
- Alembic (for database migrations)

## Description

This microservice allows you to perform **CRUD operations** on users in a database. The main endpoint it provides is to **UPDATE** existing users.

## Requirements

To run this project, you need to have the following programs installed:

- [Docker]
- [Visual Studio Code]
- **Python 3.9+**: The recommended version.
- **Pipenv**: For managing Python dependencies.

## Dependencies

- **FastAPI**: For building the web framework and API endpoints.
- **SQLAlchemy**: ORM for interacting with the MySQL database.
- **Alembic**: For database migrations.
- **MySQL**: Database for storing user information.
- **Pydantic**: For data validation and serialization.
- **dotenv**: For managing environment variables.

## Steps to Run the Project

### 1. Clone the Repository

If you haven't downloaded the project yet, clone or download it from GitHub:

```bash
git clone https://github.com/Karolpineda/microservice-update-user.git
```
### 2. Build the Docker Image
In the project directory, run the following command to build the Docker image:
```bash
docker build -t <your-username>/microservice-create-user

```
### 3. Run the Project
After building the image, run the project with this command:
```bash
docker run -p 8089:8089 <your-username>/microservice-update-user
```
The application will run at: http://localhost:8089

## API Usage
### Update a User
Endpoint: POST /user

This endpoint allows you to update a user in the database using the provided data.
