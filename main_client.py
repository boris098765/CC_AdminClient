import os

from cc_admin_client.client import CCAPIClient
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("CC_API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

client = CCAPIClient(API_BASE_URL, API_KEY)
