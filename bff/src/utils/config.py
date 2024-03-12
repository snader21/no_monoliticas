import os
from dotenv import load_dotenv

load_dotenv()
# Get the environment variables from the .env file
propiedades_path = os.getenv("PROPIEDADES_PATH", "http://localhost:5002")
compania_path = os.getenv("COMPANIA_PATH", "http://localhost:5000")