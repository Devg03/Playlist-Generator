from requests import get, post
import spotipy
import base64
import json
import os
import utils
from dotenv import load_dotenv


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")
spotify_user_id = os.getenv("SPOTIFY_USER_ID")

def get_token():
    auth_string = client_id + ":" + client_secret_id
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {"Authorization": "Basic " + auth_base64,
               "Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_headers(token):
    return {"Authorization": "Bearer " + token}

token = util.prompt_for_user_token('WildWolf', "user-read-private", client_id, client_secret_id, "localhost")

# def search_for_userID(token, user_id):
#     url = "https://api.spotify.com/v1/me" #What spotify url to request from
#     headers = get_auth_headers(token)
#     query = f"?q={user_id}&type=artist&limit = 1" # Defines query. q = searching for what, & lets you type the type of content you are querying and limit sets the number of results

#     query_url = url + query
#     result = get(query_url, headers = headers) # Stores the returned headers
#     json_result = json.loads(result.content)["artists"]["items"] # Only searches for the artists name and related info.

#     # If no artists exists by that name then returns the following
#     if len(json_result) == 0:
#         print("No artist with the name entered exists....")
#         return None
    
#     return json_result[0] # If the artists exists then the returns the info.


# def get_songs_by_user(token, user_id):
#     url = "https://api.spotify.com/v1/me/albums"
#     headers = get_auth_headers(token)
#     query = f"?q={user_id}&type=user_id&limit=1"

#     query_url = url + query
#     result = get(query_url, headers=headers)
#     json_result = json.loads(result.content)['items']['name']
#     return json_result

# token = get_token()
# result = get_songs_by_user(token, spotify_user_id) # Searchig for ACDC

# print(result)

sp = spotipy.client.Spotify(auth = get_token())
results = sp.me()
print(results)

# May need to fetch User's top items first in order to get the most played genres