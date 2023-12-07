import pandas as pd
import numpy as np

# Abrir el archivo CSV
data = pd.read_csv("Titanic-Dataset.csv", index_col='PassengerId')

print(data.isnull().sum())