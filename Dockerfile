FROM python:3.11-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/app/.cache

# Minimal dependencies for Alpine
RUN apk add --no-cache gcc musl-dev

# Install with CPU-only torch + aggressive cleanup
RUN pip install --no-cache-dir uvicorn fastapi transformers torch --index-url https://download.pytorch.org/whl/cpu && \
    find /usr/local -name "*.pyc" -delete && \
    find /usr/local -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true && \
    rm -rf /usr/local/lib/python*/site-packages/tests

COPY simple_app.py app.py

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
