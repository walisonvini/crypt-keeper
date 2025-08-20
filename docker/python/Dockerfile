FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 generate_cryptography_key.py && \
    python3 generate_secret_key.py

EXPOSE 8000

CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000"]
