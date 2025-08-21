# CryptKeeper 🗝️🏦

## Description

CryptKeeper is a password management application developed for the "Rapid Application Development in Python" course in the Computer Science program at Centro Universitário Unimetrocamp Wyden. The project aims to provide a secure platform for storing and managing passwords, ensuring sensitive information is protected with robust security measures.

## 💻 Prerequisites

### Option 1: Local Development
* **Python** `3.13+`
* **Pip** `23.0+`
* **PostgreSQL** `15.0+`

### Option 2: Docker Development
* **Docker** `^24.0`
* **Docker Compose** `^2.0`

## 🐋 Installation with Docker

1. Copy the .env file and configure environment variables
    ```bash
    cp .env.example .env
    ```

2. Configure your .env file
    ```bash
    # Update the database credentials for Docker:
    # DB_NAME=your_database_name
    # DB_USER=your_username
    # DB_PASSWORD=your_password
    ```

3. Build Docker images
    ```bash
    docker-compose build
    ```

4. Start containers
    ```bash
    docker-compose up -d
    ```

5. Access the application container
    ```bash
    docker exec -it cryptkeeper_web bash
    ```

6. Generate cryptographic key:
    ```bash
    python generate_cryptography_key.py
    ```

7. Generate secret key:
    ```bash
    python generate_secret_key.py
    ```

8. Run migrations
    ```bash
    python manage.py migrate
    ```

9. Access the application
    ```bash
    # Open your browser and navigate to:
    http://localhost
    ```

## ⚙️ Installation without Docker

Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

Install the Python dependencies
```bash
pip install -r requirements.txt
```

Copy the `.env.example` file to `.env` and fill in the required environment variables:
```bash
cp .env.example .env
```

Generate cryptographic key:
```bash
python generate_cryptography_key.py
```

> ⚠️ **CRITICAL WARNING** ⚠️
> 
> **Do not change the cryptographic key once it is generated!** Changing the key will make previously encrypted data inaccessible, as the encryption is dependent on the key. If you absolutely need to change the key, you must decrypt all the stored data with the old key and re-encrypt it with the new key before applying the change.

Generate secret key:
```bash
python generate_secret_key.py
```

Migrate the database:
```bash
python manage.py migrate
```

Run the application:
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) with your browser to see the result