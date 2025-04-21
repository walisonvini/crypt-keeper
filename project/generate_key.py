from cryptography.fernet import Fernet
from dotenv import load_dotenv, set_key
import os

env_path = ".env"

if not os.path.exists(env_path):
    raise FileNotFoundError(f"The file {env_path} does not exist.")

load_dotenv(dotenv_path=env_path)

key = Fernet.generate_key().decode()

set_key(env_path, "CRYPTOGRAPHY_KEY", key)

print("Fernet key generated and saved to .env successfully!")
