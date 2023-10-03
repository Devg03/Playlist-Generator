import random
import urllib.parse
import os
from flask import Flask, redirect, request

client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")


redirect_uri = 'http://localhost:8888/callback'
app = Flask(__name__)

@app.route('/login')
def login():
    state = generateRandomString(16)
    scope = 'user-read-private user-read-email'
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'redirect_uri': redirect_uri,
        'state': state
    }
    url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)
    return redirect(url)

print(login)