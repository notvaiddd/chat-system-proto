# app/core/config.py
# Contains application configuration settings.

import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the root directory
load_dotenv()

# Get the database URL from the environment variable.
DATABASE_URL = os.getenv("DATABASE_URL")

# --- JWT Settings ---
# A strong, random secret key is crucial for security.
# You can generate one using: openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY", "a_very_secret_key_that_should_be_in_env_file")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token will be valid for 30 minutes
