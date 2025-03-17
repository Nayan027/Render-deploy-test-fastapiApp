# Use an official lightweight Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the FastAPI default port
EXPOSE 5000

# Command to run the application
# CMD ["gunicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]