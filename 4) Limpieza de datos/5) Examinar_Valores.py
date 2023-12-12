import pandas as pd

# Cargar los archivos CSV
df_old = pd.read_csv("4) Limpieza de datos/Titanic-Dataset-old.csv")
df_new = pd.read_csv("4) Limpieza de datos/Titanic-Dataset.csv")

# Compara los valores agregados
print(df_new.describe())
print(df_old.describe())