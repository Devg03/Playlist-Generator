import base64
import json
import os

from dotenv import load_dotenv
from requests import get, post

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET_ID = os.getenv("CLIENT_SECRET_ID")
REDIRECT_URL = os.getenv("REDIRECT_URL")

print(CLIENT_ID + " " + CLIENT_SECRET_ID + " " + REDIRECT_URL)
