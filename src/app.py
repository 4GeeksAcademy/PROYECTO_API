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



# Gráfico de dispersión para relacionar popularidad y duración
plt.figure(figsize=(10, 6))
plt.scatter(df['duration_ms']/1000/60, df['popularity'], alpha=0.7, s=60)  # Convertir a minutos
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad')
plt.title('Relación entre Duración y Popularidad de las Canciones de Shakira')
plt.grid(True, alpha=0.3)

# Agregar línea de tendencia
import numpy as np
z = np.polyfit(df['duration_ms']/1000/60, df['popularity'], 1)
p = np.poly1d(z)
plt.plot(df['duration_ms']/1000/60, p(df['duration_ms']/1000/60), "r--", alpha=0.8, label='Tendencia')
plt.legend()

plt.tight_layout()
plt.show()

# Calcular correlación
correlation = df['duration_ms'].corr(df['popularity'])
print(f"Correlación entre duración y popularidad: {correlation:.3f}")