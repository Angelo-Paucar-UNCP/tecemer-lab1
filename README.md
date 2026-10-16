# Laboratorio 4: Construcción de una red neuronal artificial con la librería Keras sobre TensorFlow.

Breve proyecto de laboratorio para configurar un entorno de desarrollo profesional en Python, implementando un script que consume una API pública de chistes.

## Instrucciones:

    1. Abrir el repositorio.
    2. Activar un entorno virtual:
    3. Instalar librerias
        -TensorFlow (incluye Keras), scikit-learn y Matplotlib.
    4. Reutilizar el archivo pronostico_huancayo.csv(laboratorio 2)
    5. Preparación de datos: Limpieza, transformación y partición de un dataset climático real para tareas de clasificación.
    6. Primer modelo neuronal: Construcción y entrenamiento de una red neuronal multicapa (MLP) sobre datos sintéticos para entender la arquitectura y el flujo de trabajo en Keras.
    7. Clasificador real: Desarrollo de un modelo que predice días lluviosos, comparación con un modelo baseline (regresión logística), y creación de scripts para predicción e implementación de pruebas automatizadas.

# Estructura

tecemer-lab/
| └── semana04/
| ├── pronostico_huancayo.csv
| ├── preparar_dataset.py
| ├── dataset_preparado.npz
| ├── perceptron_sintetico.py
| ├── curvas_entrenamiento_sintetico.png
| ├── clasificador_lluvia.py
| ├── curvas_entrenamiento_lluvia.png
| ├── modelo_lluvia.keras
| ├── predecir.py
| ├── README.md
| └── tests/
| └── test_preparacion.py
