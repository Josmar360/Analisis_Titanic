import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')

# Dividir en 5 intervalos
num_bins = 5

# Crear intervalos para la columna 'Fare'
fare_bins = pd.cut(data['Fare'], bins=num_bins)

# Crear un nuevo DataFrame con la información de supervivencia y los intervalos de tarifas
survival_by_fare = data.groupby(fare_bins)['Survived'].value_counts().unstack().fillna(0)

# Graficar
survival_by_fare.plot(kind='bar', stacked=True)
plt.xlabel('Tarifa')
plt.ylabel('Conteo de Pasajeros')
plt.title('Conteo de Sobrevivientes por Rango de Tarifa')
plt.legend(['No sobrevivió', 'Sobrevivió'], loc='upper right')
plt.show()
