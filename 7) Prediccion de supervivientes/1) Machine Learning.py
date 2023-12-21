import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Abrir el archivo CSV
data = pd.read_csv("Titanic-Dataset.csv")

# Excluir la columna 'Survived' en las características
X = data.drop(['Survived', 'Name', 'Embarked', 'Sex_male'], axis=1)
y = data['Survived']

# Convertir 'Sex_female' en valores numéricos
X['Sex_female'] = X['Sex_female'].astype(int)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Normalizar las características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicializar el clasificador
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

clf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(
    clf, param_grid, cv=StratifiedKFold(n_splits=5), scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

# Mostrar los mejores parámetros encontrados por Grid Search
best_params = grid_search.best_params_
print(f"Mejores parámetros encontrados: {best_params}")

# Entrenar el modelo con los mejores parámetros ubicados arriba
best_clf = grid_search.best_estimator_
best_clf.fit(X_train_scaled, y_train)

# Realizar predicciones en el conjunto de prueba
y_probs = best_clf.predict_proba(X_test_scaled)[:, 1]

# Ajustar manualmente el umbral de clasificación
threshold = 0.5  # Fue el mas optimo, los demas estaban desvalanceados
y_pred_adjusted = (y_probs > threshold).astype(int)

# Evaluar el rendimiento del modelo después de ajustar manualmente el umbral
accuracy_adjusted = accuracy_score(y_test, y_pred_adjusted)
conf_matrix_adjusted = confusion_matrix(y_test, y_pred_adjusted)
classification_rep_adjusted = classification_report(y_test, y_pred_adjusted)

# Imprimir resultados después de ajustar manualmente el umbral
print(f'Accuracy después de ajustar manualmente el umbral: {
      accuracy_adjusted}')
print(f'Confusion Matrix después de ajustar manualmente el umbral:\n{
      conf_matrix_adjusted}')
print(f'Classification Report después de ajustar manualmente el umbral:\n{
      classification_rep_adjusted}')
