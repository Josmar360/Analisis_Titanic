import pandas as pd
import matplotlib.pyplot as plt

# Abrir archivo csv
print("========== Imprimir el archivo csv ==========")
# data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')
# print(data)

# print(data.describe())

data = pd.read_csv("Titanic-Dataset.csv")
print(data.isnull().sum())

survival_by_gender = data.groupby(['Sex', 'Survived']).size().unstack()

survival_by_gender.plot(kind='bar', stacked=True)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Survival Count by Sex')
plt.xticks(rotation=0)
plt.legend(['Did not survive', 'Survived'], loc='upper left')
plt.show()