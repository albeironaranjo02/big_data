# Procesamiento de los datos
import pandas as pd
import numpy as np

# Leer y procesar los datos
data = []
with open('/workspaces/big_data/notebooks/votos_actas.txt', 'r') as f:
    for linea in f:
        partes = linea.strip().split(',')
        if len(partes) == 3:
            data.append((partes[0], int(partes[2])))

df = pd.DataFrame(data, columns=['candidato', 'votos'])

# Calcular varianza poblacional para cada candidato
resultados = {}
for candidato in df['candidato'].unique():
    votos = df[df['candidato'] == candidato]['votos']
    n = len(votos)
    media = votos.mean()
    # Varianza poblacional (ddof=0)
    varianza = votos.var(ddof=0)
    resultados[candidato] = {
        'n': n,
        'media': media,
        'varianza': varianza,
        'suma_x': votos.sum(),
        'suma_x2': (votos**2).sum()
    }
    
    print(f"{candidato}:")
    print(f"  Número de actas: {n}")
    print(f"  Suma de votos: {votos.sum():,.0f}")
    print(f"  Suma de cuadrados: {(votos**2).sum():,.0f}")
    print(f"  Media: {media:.2f}")
    print(f"  VARIANZA: {varianza:.2f}")
    print(f"  Desviación estándar: {np.sqrt(varianza):.2f}")
    print(f"  Mínimo: {votos.min()}")
    print(f"  Máximo: {votos.max()}")