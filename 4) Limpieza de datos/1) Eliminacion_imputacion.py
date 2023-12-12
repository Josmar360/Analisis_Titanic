import pandas as pd
from sklearn.impute import SimpleImputer

# Abrir el archivo CSV
data = pd.read_csv("4) Limpieza de datos/Titanic-Dataset.csv", index_col='PassengerId')

# Ver valores nulos
print(data.isnull().sum())

# Eliminar la columna de Cabina
data = data.drop('Cabin', axis=1)

# Imputar la columna de Edad
Imputar = SimpleImputer(strategy='mean')
data['Age'] = Imputar.fit_transform(data[['Age']])

# Eliminar las dos filas en Embarked
data = data.dropna(subset=['Embarked'])

# Sobreescribir el archivo CSV
data.to_csv("4) Limpieza de datos/Titanic-Dataset.csv", index=False)