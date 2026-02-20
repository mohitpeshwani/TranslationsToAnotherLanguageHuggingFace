FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY simple_requirements.txt .
RUN pip install --no-cache-dir -r simple_requirements.txt

# Copy app
COPY simple_app.py .

# Expose port
EXPOSE 8000

# Run
CMD ["uvicorn", "simple_app:app", "--host", "0.0.0.0", "--port", "8000"]
