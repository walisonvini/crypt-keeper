# CryptKeeper 🗝️🏦

## Description

CryptKeeper is a password management application developed for the "Rapid Application Development in Python" course in the Computer Science program at Centro Universitário Unimetrocamp Wyden. The project aims to provide a secure platform for storing and managing passwords, ensuring sensitive information is protected with robust security measures.

## 💻 Prerequisites
* Python `3.13+`
* Pip `23.0+`
* PostgreSQL `15.0+`

## 🚀 Installing CryptKeeper

Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

Install the Python dependencies `cd project` or `crypt-keeper\project`
```bash
pip install -r requirements.txt
```

Copy the `.env.example` file to `.env` and fill in the required environment variables:
```bash
cp .env.example .env
```

Generate cryptographic keys:
```bash
python generate_key.py
```

Important: Do not change the cryptographic key once it is generated! Changing the key will make previously encrypted data inaccessible, as the encryption is dependent on the key. If you absolutely need to change the key, you must decrypt all the stored data with the old key and re-encrypt it with the new key before applying the change.

Migrate the database:
```bash
python manage.py migrate
```

Run the application:
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) with your browser to see the result