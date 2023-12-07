#Ejemplo con matplotlib
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')

survival_by_gender = data.groupby(['Sex', 'Survived']).size().unstack()

survival_by_gender.plot(kind='bar', stacked=True)
plt.xlabel('Genero')
plt.ylabel('Conteo')
plt.title('Conteo de supervivientes por sexo')
plt.xticks(rotation=0)
plt.legend(['No sobrevivio', 'Sobrevivio'], loc='upper left')
plt.show()
