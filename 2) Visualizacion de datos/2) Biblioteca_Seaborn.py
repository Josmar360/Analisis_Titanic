#Ejemplo con Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el conjunto de datos del Titanic
data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")

# Crear la primera gráfica: Relación entre 'Sex', 'Survived'
sns.countplot(data=data, x='Sex', hue='Survived', palette='pastel')
sns.despine()
plt.show()

# Crear la segunda gráfica: Relación entre 'Pclass', 'Survived'
sns.countplot(data=data, x='Pclass', hue='Survived', palette='deep')
sns.despine()
plt.show()
