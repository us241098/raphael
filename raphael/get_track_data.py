import json


with open('spotify_song_data.json') as f:
    tracks = json.load(f)


tracks_meta_data = []
for i in tracks:
    temp_dict ={}

    temp_dict["spotify_link"] = i["track"]["external_urls"]["spotify"]
    temp_dict["song_name"] = i["track"]["name"]
    temp_dict["artist_name"] = i["track"]["artists"][0]["name"]
    temp_dict["album_name"] = i["track"]["album"]["name"]
    temp_dict["track_id"] = i["track"]["id"]
    temp_dict["preview_url"] = i["track"]["preview_url"]
    temp_dict["song_href"] = i["track"]["href"]
    temp_dict["track_uri"] = i["track"]["uri"]
    temp_dict["track_image"] = i["track"]["album"]["images"][0]["url"]
    tracks_meta_data.append(temp_dict)

with open('./data/spotify_song_data_meta.json', 'w') as outfile:
    json.dump(tracks_meta_data, outfile)
