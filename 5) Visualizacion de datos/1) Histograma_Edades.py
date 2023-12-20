import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abrir el archivo CSV
data = pd.read_csv("5) Visualizacion de datos/Titanic-Dataset.csv", index_col='PassengerId')

# Configuración del estilo de seaborn para gráficos más atractivos
sns.set(style="whitegrid")

# Crear el histograma utilizando seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=30, kde=True, color='skyblue')
plt.title('Histograma de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()