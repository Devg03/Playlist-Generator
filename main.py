import base64
import json
import os
import urllib.parse
import random
import string
from dotenv import load_dotenv
from requests import get, post

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET_ID = os.getenv("CLIENT_SECRET_ID")
<<<<<<< HEAD
REDIRECT_URI = os.getenv("REDIRECT_URL")

# print(CLIENT_ID + " " + CLIENT_SECRET_ID + " " + REDIRECT_URL)

# The code below serves for authorization
def auth():
    scope = 'user-read-private user-read-email' 

    state = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=16))

    redirect = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "scope": scope,
        "redirect_uri": REDIRECT_URI,
        "state": state,
    }

    url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(redirect)

    print(url)

# Code: 

auth()
=======
REDIRECT_URL = os.getenv("REDIRECT_URL")

print(CLIENT_ID + " " + CLIENT_SECRET_ID + " " + REDIRECT_URL)
>>>>>>> 2320c341312a45371f543451b733e08bc5b0ab60
