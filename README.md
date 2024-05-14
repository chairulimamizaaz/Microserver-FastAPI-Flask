# Microservice Architecture with FastAPI and Flask

This project demonstrates a microservice architecture using FastAPI and Flask, encapsulated in Docker containers. The setup includes a PostgreSQL database for user data storage, a Flask application to handle user registration and authentication, and a FastAPI service designed to send data to Flask services.

## Architecture Overview

- **Postgres Database**: Manages user credentials storage.
- **Flask Application**: Handles user registration and authentication.
- **FastAPI Service**: Responsible for sending requests to Flask services.

## Setup Instructions

### Prerequisites

Before you begin, ensure you have Docker and Docker Compose installed on your machine. These tools are required to run the services and manage the containers.

### Environment Setup

1. **Clone the Repository**
Clone the project repository to your local machine using the following command:
```bash
git clone https://github.com/your-repository.git
```
2. **Navigate to the Project Directory**
Change into the project directory:
```bash
cd Microservice-FastAPI-Flask
```
3. **Build and Start Services**
Use Docker Compose to build and start the services:
```bash
docker-compose up --build
```
To stop the services and remove the containers, use:
```bash
docker-compose down
```

## Interacting with the Services
### Access the PostgreSQL Database
To open a PostgreSQL shell in the running Postgres container:
```bash
docker exec -it uts-iae-postgres-1 psql -U user -d mydatabase
```
### Initialize the Database
Once inside the PostgreSQL shell, create the necessary user table by executing:
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```
noted: This program automatically creates tables, so just use it

### Register a User
To register a new user:
* URL: http://localhost:5001/register
* Method: POST
* Body
```json
{
    "email": "test2@example.com",
    "name": "Test User2",
    "password": "securepassword1234"
}
```
### User Login
To authenticate a user:
* URL: http://localhost:5001/login
* Method: POST
* Body
```json
{
    "email": "test2@example.com",
    "password": "securepassword1234"
}
```

### Update User
To update an existing user's details:
* URL: `http://localhost:5002//users/<int:user_id>`
* Method: PUT
* Body:
```json
{
    "id": 1,
    "email": "updated@example.com",
    "name": "Updated Name",
    "password": "newsecurepassword"
}
```

### Delete User
To delete an existing user:
* URL: `http://localhost:5002//users/<int:user_id>`
* Method: DELETE
* Parameters:
```json
id=1
```

### Retrieve All Users
To retrieve a list of all registered users:
* URL: `http://localhost:5002//users`
* Method: GET
* This endpoint does not require any body or parameters and will return a list of all users in the database.

### Development Notes
This project is configured for development purposes. For production environments, additional configuration for security, performance, and reliability is recommended.

### Contributions
Contributions to this project are welcome! Please fork the repository and submit a pull request with your suggested changes.

### License
This project is released under the MIT License. For more details, see the LICENSE file included in the repository.

### Notes

- This README is designed to provide clear, step-by-step instructions for getting the project up and running on any developer's local machine.
- It includes basic commands to clone the repository, navigate into the project directory, and commands to build and start the Docker containers.
- It details how to access the PostgreSQL database, set up the necessary database table, and how to interact with the system via provided API endpoints for user registration and login.
- Security notes are added to remind users that the current configuration is intended for development, not production use.
