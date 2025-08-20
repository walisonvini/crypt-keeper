from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv, set_key
import os

env_path = ".env"

if not os.path.exists(env_path):
    raise FileNotFoundError(f"The file {env_path} does not exist.")

load_dotenv(dotenv_path=env_path)

secret_key = get_random_secret_key()

set_key(env_path, "SECRET_KEY", secret_key)

print("Django SECRET_KEY generated and saved to .env successfully!")
