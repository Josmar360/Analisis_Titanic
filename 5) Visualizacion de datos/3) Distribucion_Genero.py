import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abrir el archivo CSV
data = pd.read_csv("4) Limpieza de datos/Titanic-Dataset.csv", index_col='PassengerId')

# Crear un DataFrame de ejemplo para ilustrar el código
data = {
    'Pclass': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'Sex_female': [1, 1, 0, 0, 1, 0, 1, 0, 1],
}

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
