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
plt.show()
