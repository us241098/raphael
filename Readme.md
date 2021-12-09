# raphael

this project is an (ongoing) attempt to visualise all my liked spotify songs

<br>

## so far:
- downloaded the metadata of all liked songs
- used spotify audio features api to extract acoustic features like `'danceability',
       'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
       'instrumentalness', 'liveness', 'valence',` and `'tempo'`
- used t-SNE for dimensionality reduction and plotly for user friendly visualisation


## findings:



## to dos:
- attempt to generate better embeddings (auto encoders?)
- model the song genre
- look for other relevant features