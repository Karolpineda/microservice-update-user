# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Instalar herramientas de compilación necesarias para mariadb
RUN apt-get update && apt-get install -y gcc libmariadb-dev

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose the port
EXPOSE 8089

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8089"]
