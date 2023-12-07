import pandas as pd
import matplotlib.pyplot as plt

# Abrir archivo CSV
data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')

# Separar las familias (que tengan un padre e hijo)
print("\n========== Seperacion de familias ==========")
count_with_family = data[data['Parch'] > 0]['Survived'].count()
count_no_family = data[data['Parch'] == 0]['Survived'].count()
print("Familias que viajaron juntas: ", count_with_family)
print("Pasajeros que viajaron sin familia (padre o hijo): ", count_no_family)

# Crear un DataFrame simple
df_counts = pd.DataFrame(
    {'Con familia': count_with_family, 'Sin familia': count_no_family}, index=[0])

# Graficar los resultados
df_counts.plot(kind='bar', color=['purple', 'green'], alpha=0.7, stacked=False)
plt.xlabel('Condición familiar')
plt.ylabel('Conteo')
plt.title('Conteo de familias abordo (padres e hijos)')
plt.xticks(rotation=0)
plt.legend([f'Con familia {count_with_family}', f'Sin familia {
           count_no_family}'], loc='upper left')
plt.show()  # Cerrar el primer gráfico

# Separar las familias (que tengan un padre e hijo)
survived_with_family = data[(data['Parch'] > 0) & (
    data['Survived'] == 1)]['Survived'].count()
no_survived_with_family = data[(data['Parch'] > 0) & (
    data['Survived'] == 0)]['Survived'].count()
survived_no_family = data[(data['Parch'] == 0) & (
    data['Survived'] == 1)]['Survived'].count()
no_survived_no_family = data[(data['Parch'] == 0) & (
    data['Survived'] == 0)]['Survived'].count()
print(survived_with_family)
print(no_survived_with_family)
print(survived_no_family)
print(no_survived_no_family)

# Crear DataFram simple
df_counts_Survived = pd.DataFrame({'Sobrevive con familia': survived_with_family, 'Mueren con familia': no_survived_with_family,
                                  'Sobrevive sin familia': survived_no_family, 'Mueren sin familia': no_survived_no_family}, index=[1])

# Graficar resultados de supervivientes
df_counts_Survived.plot(kind='bar', color=[
                        'purple', 'green', 'blue', 'orange'], alpha=0.7, stacked=False)
plt.xlabel('Situacion familiar')
plt.ylabel('Conteo')
plt.title('Comparativa de supervivientes con familia (padres e hijos)')
plt.xticks(rotation=0)
# Corregir la lista de leyendas
plt.legend([f'Sobrevive con familia', f'Mueren con familia',
           f'Sobreviven solos', f'Mueren solos'], loc='upper left')
plt.show()
