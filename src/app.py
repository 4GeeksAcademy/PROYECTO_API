import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Spotify API credentials

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

url_shakira = "https://open.spotify.com/intl-es/artist/0EmeFodog0BfCgMzAIvKQp"

# → Devuelve las canciones más populares del artista en un país específico.
top_track = spotify.artist_top_tracks("0EmeFodog0BfCgMzAIvKQp", country='ES')
print("\nCanciones mas populares de Shakira en España:\n")
for track in top_track['tracks'][:10]:
    print(track['name'], track['popularity'])

# convertir a dataframe
data = []
for track in top_track['tracks']:
    data.append({
        'name': track['name'],
        'popularity': track['popularity'],
        'album': track['album']['name'],
        'duration_ms': track['duration_ms'],
       
    })
df = pd.DataFrame(data)
df.head(10)
print("\nDataframe de las canciones mas populares de Shakira en España:\n")
print(df.head(10))

# ordenarlo por popularidad
df_popularity = df.sort_values(by='popularity', ascending=True).reset_index(drop=True)
df_popularity = pd.DataFrame(df_popularity)
df_popularity.head(3)
print("\nDataframe ordenado por popularidad (menor a mayor), Top 3:\n")
print(df_popularity.head(3))

x = df['duration_ms']
y = df['popularity']

fig, ax = plt.subplots()
ax.scatter(x,y, 
           color='purple', # Color de puntos
           s=50,           # Tamaño de puntos
           alpha=0.7,      # Transparencia
           marker='*')     # Forma del marcador
ax.set_title('Relación entre Duración y Popularidad')
ax.set_xlabel('Duración (ms)')
ax.set_ylabel('Popularidad')
plt.show()



