# raphael

this project is an (ongoing) attempt to visualise all my liked spotify songs. generated plots available [here](assets/plot.html).
<br>

![Alt Text](assets/plot_complete.gif)
<p style="text-align: center;"> scatter plot of all 727 songs </p>

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
<p style="text-align: center;"> bob dylan songs grouped together </p>

<br>

![Alt Text](assets/electro.gif)
<p style="text-align: center;"> electronic music? VU definitely being an anomaly </p>

<br>

![Alt Text](assets/cluster_rap.gif)
<p style="text-align: center;"> rap/hip-hop </p>


## to dos:
- attempt to generate better embeddings (auto encoders?)
- model the song genre
- look for other relevant features