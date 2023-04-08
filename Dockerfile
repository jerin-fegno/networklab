FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code
COPY . .

# Run migrations and collect static files
RUN python manage.py migrate --no-input && \
    python manage.py collectstatic --no-input

# Expose the port on which the application runs
EXPOSE 8000

# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hackbox.wsgi:application"]
