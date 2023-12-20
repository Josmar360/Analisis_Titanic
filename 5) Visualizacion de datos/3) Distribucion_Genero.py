import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abrir el archivo CSV
data = pd.read_csv("5) Visualizacion de datos/Titanic-Dataset.csv", index_col='PassengerId')

df = pd.DataFrame(data)

# Crear un gráfico de barras usando seaborn
plt.figure(figsize=(10, 6))
sns.countplot(x='Pclass', hue='Sex_female', data=df, palette='Set1')

# Personalizar el gráfico
plt.title('Distribución de género por clases')
plt.xlabel('Clase')
plt.ylabel('Número de pasajeros')
plt.legend(title='Género', labels=['Male', 'Female'])

# Mostrar el gráfico
plt.show()
