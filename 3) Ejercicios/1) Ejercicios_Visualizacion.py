# Librerias que se usaran
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abrir el documento CSV
print("\n========== Abrir el archivo csv ==========")
data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')
data = data.dropna(subset=['Age', 'Ticket'])

# Calcular el promedio de la edad
print("\n========== Obtener el promedio de la edad ==========")
print("El promedio de edad es: ", data['Age'].mean())

# Obtener informacion sobre edad y ticket
print("\n========== Obtener información de edad y ticket ==========")
Estadisticas = data.groupby('Ticket')['Age'].describe()
print(Estadisticas)