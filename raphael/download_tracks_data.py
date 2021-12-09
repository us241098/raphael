
import requests
import json

def get_saved_songs_from_spotify(token, url):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    res = requests.get(url=url, headers=headers)
    data = res.json()
    print(data)
    return data["items"], data["next"]

token = "redacted"
spotify_tracks_list = []
url = "https://api.spotify.com/v1/me/tracks?limit=50"
while url:
    try:
        tracks, url = get_saved_songs_from_spotify(token, url)
        spotify_tracks_list.extend(tracks)
    except Exception as e:
        print(e)



with open('./data/spotify_song_data.json', 'w') as f:
    json.dump(spotify_tracks_list, f)
