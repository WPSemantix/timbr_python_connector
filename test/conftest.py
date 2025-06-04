import os
import pytest
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv(override=True)

# Global fixture to load config values
@pytest.fixture(scope="session")
def test_config():
  return {
    "hostname": os.getenv("HOSTNAME"),
    "port": os.getenv("PORT"),
    "ontology": os.getenv("ONTOLOGY"),
    "username": os.getenv("USERNAME"),
    "password": os.getenv("PASSWORD"),
    "enabled_ssl": os.getenv("ENABLED_SSL"),
    "http_path": os.getenv("HTTP_PATH"),
  }
