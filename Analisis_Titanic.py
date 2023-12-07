# Blibliotecas que se usan en el analisis
import pandas as pd
import numpy as np
import seaborn as sns

# Abrir archivo csv
print("\n========== abrir el archivo csv ==========")
data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')
print(data)

# Visualizar las columnas que existen
print("\n========== Visualizar columnas ==========")
print(data.columns)

# Descripcion del archivo
print("\n========== Descripcion del archivo ==========")
print(data.describe())

# Ver los tipos de datos que contiene cada atributo
print("\n========== Tipos de datos ==========")
print(data.dtypes)

# Ver el conteo de nullos que contiene cada atributo
print("\n========== Conteno de nulos ==========")
print(data.isnull().sum())
