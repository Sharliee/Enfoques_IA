!pip install scikit-learn

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Paso 1: Preparar los datos de entrenamiento y etiquetas
X = [[1, 2], [2, 3], [3, 3], [2, 1], [3, 2]]  # Datos de entrenamiento
y = [0, 0, 0, 1, 1]  # Etiquetas correspondientes a los datos

# Paso 2: Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 3: Crear una instancia de la Máquina de Vectores de Soporte
svm = SVC(kernel='linear')

# Paso 4: Entrenar la SVM
svm.fit(X_train, y_train)

# Paso 5: Realizar predicciones en el conjunto de prueba
y_pred = svm.predict(X_test)

# Paso 6: Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)
