import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Abrir el archivo CSV
data = pd.read_csv("5) Visualizacion de datos/Titanic-Dataset.csv", index_col='PassengerId')

# Crear un gráfico de barras
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

# Usar seaborn para crear un gráfico de barras agrupado por género y supervivencia
sns.countplot(x="Survived", hue="Sex_female", data=data)

# Personalizar el gráfico
plt.title('Comparación entre Género y Supervivencia')
plt.xlabel('Supervivencia (0 = No, 1 = Sí)')
plt.ylabel('Cantidad de Pasajeros')
plt.legend(title='Género', labels=['Masculino', 'Femenino'])

# Mostrar el gráfico
plt.show()
