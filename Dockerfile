FROM python:3.11-slim

WORKDIR /app

# Set Python to unbuffered
ENV PYTHONUNBUFFERED=1

# Install only essential packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY simple_requirements.txt .
RUN pip install --no-cache-dir --compile -r simple_requirements.txt && \
    find /usr/local -name "*.pyc" -delete && \
    find /usr/local -name "__pycache__" -delete

# Copy app only
COPY simple_app.py app.py

# Clean up
RUN rm -rf /tmp/* /var/tmp/*

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
