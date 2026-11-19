
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API configuration
API_BASE_URL = os.getenv("API_BASE_URL")

# Validate configuration
if not API_BASE_URL:
    raise ValueError("API_BASE_URL is missing from .env")
