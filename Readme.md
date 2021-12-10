# raphael

this project is an (ongoing) attempt to visualise all my liked spotify songs. generated plots available [here](assets/plot.html).
<br>

![Alt Text](assets/plot_complete.gif)
<center>scatter plot of all 727 songs </center>

<br>

## so far:
- downloaded the metadata of all liked songs
- used spotify audio features api to extract acoustic features like `'danceability',
       'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
       'instrumentalness', 'liveness', 'valence',` and `'tempo'`
- used t-SNE for dimensionality reduction and plotly for user friendly visualisation


## findings:
while embeddings are quite simple, some observations are interesting

![Alt Text](assets/bob_dylan_cluster.gif)
<center>bob dylan songs grouped together</center>

<br>

![Alt Text](assets/electro.gif)
<center>electronic music? VU definitely being an anomaly </center>

<br>

![Alt Text](assets/cluster_rap.gif)
<center> rap/hip-hop </center>


## to dos:
- attempt to generate better embeddings (auto encoders?)
- model the song genre
- look for other relevant features