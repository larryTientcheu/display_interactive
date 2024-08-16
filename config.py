"""
 Configuration file for the project.
"""

import os
import logging
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# Dev environment is the default
URL = os.getenv("DEV_CLOUD_API_URL")
LEVEL = 10

if os.getenv("ENV") == "prod":
    URL = os.getenv("PROD_CLOUD_API_URL")
    LEVEL = 20
elif os.getenv("ENV") == "stage":
    URL = os.getenv("STAGE_CLOUD_API_URL")

# Configure logging settings with level changing from dev to prod
logging.basicConfig(
    level=LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        # Log to a file
        logging.FileHandler("app.log"),
        # Log to the console
        logging.StreamHandler(),
    ],
)
