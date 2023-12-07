import pandas as pd
import matplotlib.pyplot as plt

# Abrir archivo CSV
data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')

# Separar a pasajeros con familiares y sin familiares
count_no_family = data[(data['SibSp'] == 0) & (
    data['Parch'] == 0)]['Survived'].count()
count_with_family = data[(data['SibSp'] > 0) | (
    data['Parch'] > 0)]['Survived'].count()
print("\n========== Obtencion de datos de pasajeros ==========")
print("Pasajeros que viajan sin acompañantes: ", count_no_family)
print("Pasajeros que viajan con acompañantes: ", count_with_family)

# Crear un DataFrame simple
df_counts = pd.DataFrame({'Sin acompañante': count_no_family,
                         'Con acompañante': count_with_family}, index=[0])

# Graficar como gráfica de pastel
df_counts.transpose().plot(kind='pie', autopct='%1.1f%%',
                           startangle=90, subplots=True)
plt.axis('equal')
plt.title('Proporción de pasajeros con y sin acompañantes')
plt.legend([f'No sobrevivio {count_no_family}', f'Sobrevivio {
           count_with_family}'], loc='lower right')
plt.show()
