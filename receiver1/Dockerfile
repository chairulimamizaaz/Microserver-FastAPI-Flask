# Using a slim version of Python 3.8
FROM python:3.8-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Install PostgreSQL client to interact with the PostgreSQL server
RUN apt-get update && apt-get install -y postgresql-client

# Copy the Python requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code and scripts into /app
COPY . .
COPY wait-for-postgres.sh /usr/wait-for-postgres.sh

# Ensure the wait-for-postgres script is executable
RUN chmod +x /usr/wait-for-postgres.sh

# Command to run the wait-for-postgres script followed by starting the application
CMD ["/usr/wait-for-postgres.sh", "postgres", "python", "app.py"]
