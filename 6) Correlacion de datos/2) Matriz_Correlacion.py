import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Abrir el archivo CSV
data = pd.read_csv("6) Correlacion de datos/Titanic-Dataset.csv", index_col="PassengerId")

# Excluir las columnas no numéricas
numeric_data = data.select_dtypes(include=['number'])

# Agregar las columnas de sexo
numeric_data['Sex_male'] = data['Sex_male']
numeric_data['Sex_female'] = data['Sex_female']

# Calcular la matriz de correlación
correlation_matrix = numeric_data.corr()

# Utilizar clustermap para visualizar la matriz de correlación de manera diferente
plt.figure(figsize=(12, 8))
sns.clustermap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()
