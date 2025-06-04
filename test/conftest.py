import os
import pytest
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv(override=True)

def convert_env_to_bool(value):
  """Convert environment variable string to boolean."""
  if value is None:
    return None
  if value.lower() in ['true', '1', 'yes']:
    return True
  elif value.lower() in ['false', '0', 'no']:
    return False
  else:
    raise ValueError(f"Invalid boolean value: {value}")

# Global fixture to load config values
@pytest.fixture(scope="session")
def test_config():
  return {
    "hostname": os.getenv("HOSTNAME"),
    "port": os.getenv("PORT"),
    "ontology": os.getenv("ONTOLOGY"),
    "username": os.getenv("USERNAME"),
    "password": os.getenv("PASSWORD"),
    "enabled_ssl": convert_env_to_bool(os.getenv("ENABLED_SSL")),
    "http_path": os.getenv("HTTP_PATH"),
  }
