import matplotlib.pyplot as plt
import pandas as pd

# Abrir el archivo CSV
data = pd.read_csv("4) Limpieza de datos/Titanic-Dataset.csv", index_col='PassengerId')

# Crear un diagrama de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(data['Fare'], data['Survived'], alpha=0.5)

# Personalizar el gráfico
plt.title('Relación entre Tarifa Pagada y Supervivencia')
plt.xlabel('Tarifa Pagada')
plt.ylabel('Supervivencia')
plt.grid(True)

# Mostrar el gráfico
plt.show()
