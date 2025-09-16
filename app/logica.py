# 1. SETUP
import numpy as np
import pandas as pd
import os

# 2. CARGA DE DATOS (ruta robusta)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "dataset_inquilinos.csv")
df = pd.read_csv(csv_path, index_col='id_inquilino')

df.columns = [
    'horario', 'bioritmo', 'nivel_educativo', 'leer', 'animacion', 
    'cine', 'mascotas', 'cocinar', 'deporte', 'dieta', 'fumador',
    'visitas', 'orden', 'musica_tipo', 'musica_alta', 'plan_perfecto', 'instrumento'
]

# 3. ONE HOT ENCODING sin scikit-learn
for col in df.columns:
    df[col] = df[col].astype('category')
df_encoded = pd.get_dummies(df, dtype=float)

# 4. MATRIZ DE SIMILARIDAD
matriz_s = np.dot(df_encoded.values, df_encoded.values.T)

rango_min = -100
rango_max = 100
min_original = float(np.min(matriz_s))
max_original = float(np.max(matriz_s))

if max_original - min_original == 0:
    matriz_s_reescalada = np.zeros_like(matriz_s, dtype=float)
else:
    matriz_s_reescalada = ((matriz_s - min_original) / (max_original - min_original)) * (rango_max - rango_min) + rango_min

df_similaridad = pd.DataFrame(matriz_s_reescalada,
                              index=df.index,
                              columns=df.index)

# 5. FUNCIÓN PRINCIPAL
def inquilinos_compatibles(id_inquilinos, topn):
    for id_inquilino in id_inquilinos:
        if id_inquilino not in df_similaridad.index:
            return 'Al menos uno de los inquilinos no encontrado'

    filas_inquilinos = df_similaridad.loc[id_inquilinos]
    similitud_promedio = filas_inquilinos.mean(axis=0)
    inquilinos_similares = similitud_promedio.sort_values(ascending=False)
    inquilinos_similares = inquilinos_similares.drop(id_inquilinos)

    topn_inquilinos = inquilinos_similares.head(topn)
    registros_similares = df.loc[topn_inquilinos.index]
    registros_buscados = df.loc[id_inquilinos]
    resultado = pd.concat([registros_buscados.T, registros_similares.T], axis=1)

    similitud_series = pd.Series(data=topn_inquilinos.values, index=topn_inquilinos.index, name='Similitud')
    return (resultado, similitud_series)
