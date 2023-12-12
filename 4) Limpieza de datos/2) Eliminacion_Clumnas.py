import pandas as pd

# Abrir archivo CSV
data = pd.read_csv("4) Limpieza de datos/Titanic-Dataset.csv")

# Eliminar la columa de Ticket
data = data.drop('Ticket', axis=1)

# Sobrescribir el archivo SCV
data.to_csv("4) Limpieza de datos/Titanic-Dataset.csv", index=False)