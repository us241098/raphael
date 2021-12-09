import json
import requests

with open("./data/spotify_song_data_meta.json", "r") as f:
    data = json.load(f)

token = "redacted"
spotify_tracks_list = []

def get_track_audio_features_spotify(token, song_id):
    url = "https://api.spotify.com/v1/audio-features/" + song_id
    headers = {
        "Authorization": "Bearer {}".format(token),
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    r = requests.get(url, headers=headers)
    return r.json()


for i in data:
    a = (get_track_audio_features_spotify(token, i["track_id"]))
    i.update(a)
    spotify_tracks_list.append(i)

with open("./data/spotify_song_data_features.json", "w") as f:
    json.dump(spotify_tracks_list, f)
