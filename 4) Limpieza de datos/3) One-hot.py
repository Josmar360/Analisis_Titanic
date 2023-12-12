import pandas as pd

# Abrir archivo CSV
data = pd.read_csv("4) Limpieza de datos/Titanic-Dataset.csv")

# Aplicar One-Hot a la variable Sex
data = pd.get_dummies(data, columns=['Sex'])

# Asignación de números a la variable 'Pclass'
data['Pclass'] = data['Pclass'].astype('category').cat.codes

# Sobrescribir el archivo SCV
data.to_csv("4) Limpieza de datos/Titanic-Dataset.csv", index=False)