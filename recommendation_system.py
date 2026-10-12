# recommendation_system.py

# Importar las librerías necesarias
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

# Si no existe el dataset, se genera uno simulado (el script necesita un CSV para funcionar)
if not os.path.exists('products.csv'):
    rng = np.random.default_rng(42)  # semilla fija para que sea reproducible
    simulado = pd.DataFrame({
        'feature1': rng.uniform(0, 10, 200),
        'feature2': rng.uniform(0, 10, 200),
        'feature3': rng.uniform(0, 10, 200),
    })
    # Etiqueta simulada: depende de la suma de las características
    simulado['label'] = (simulado[['feature1', 'feature2', 'feature3']].sum(axis=1) > 15).astype(int)
    simulado.to_csv('products.csv', index=False)

# Cargar los datos (dataset de productos)
data = pd.read_csv('products.csv')

# Preprocesamiento: seleccionar características y etiqueta
features = data[['feature1', 'feature2', 'feature3']]
labels = data['label']

# Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# Crear y entrenar el modelo con 5 vecinos
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train.values, y_train)

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test.values)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Función de recomendación
def recommend(product_features):
    prediction = model.predict(product_features)
    return prediction

# Ejemplo de uso de la función de recomendación
example_product = [[1.0, 2.0, 3.0]]
recommended_product = recommend(example_product)
print(f'Recommended Product: {recommended_product}')