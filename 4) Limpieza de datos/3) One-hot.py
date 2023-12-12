import pandas as pd

# Abrir archivo CSV
data = pd.read_csv("4) Limpieza de datos/Titanic-Dataset.csv")

# Aplicar One-Hot a la variable Sex
data = pd.get_dummies(data, columns=['Sex'])

# Asignación de números a la variable 'Pclass' (Label Encoding)
data['Pclass'] = data['Pclass'].astype('category').cat.codes

# Asignación de números a la variable 'Embarked' (Label Encoding)
data['Embarked'] = data['Embarked'].astype('category').cat.codes

data.to_csv("4) Limpieza de datos/Titanic-Dataset.csv", index=False)