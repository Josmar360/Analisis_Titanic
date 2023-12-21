import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abrir el archivo CSV
data = pd.read_csv("6) Correlacion de datos/Titanic-Dataset.csv", index_col="PassengerId")

# Variables para analizar
variables_a_visualizar = ['Sex_female', 'Sex_male', 'Pclass', 'Fare', 'Survived']

# Filtrar el conjunto de datos
subset_data = data[variables_a_visualizar]

# Crear el gráfico de dispersion
sns.pairplot(subset_data, hue='Survived', markers=['o', 's'], palette={0: 'red', 1: 'blue'})
plt.show()
