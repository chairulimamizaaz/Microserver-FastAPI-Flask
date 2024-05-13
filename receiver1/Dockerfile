FROM python:3.8-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql-client

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and scripts
COPY . .
COPY wait-for-postgres.sh /usr/wait-for-postgres.sh

# Give execution rights on the wait script
RUN chmod +x /usr/wait-for-postgres.sh

# Command to run on container start
CMD ["/usr/wait-for-postgres.sh", "postgres", "python", "app.py"]
