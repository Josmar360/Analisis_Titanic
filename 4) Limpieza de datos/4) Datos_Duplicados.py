import pandas as pd

# Abrir archivo CSV
data = pd.read_csv("4) Limpieza de datos/Titanic-Dataset.csv")

# Verificar duplicados en todo el conjunto de datos
duplicados = data.duplicated()

# Imprimir las filas duplicadas
print("Filas duplicadas:")
print(data[duplicados])

# Imprimir la cantidad total de filas duplicadas
print("\nCantidad total de filas duplicadas:", duplicados.sum())