# Laboratorio 1: Fundamentos y Entornos de Desarrollo en Python

## Instrucciones de Instalación

1. Clonar el repositorio.
2. Crear un entorno virtual:

python -m venv .venv

1. Activar el entorno virtual:

Windows: .venv\Scripts\activate

Linux/macOS: source .venv/bin/activate

2. Realizar la instalación editable de las dependencias:
   pip install -e .

3. Ejemplo de uso con el entorno virtual activado,puedes ejecutar la aplicación principal con el siguiente comando:
   python src/tecemer_lab1/app.py

4. Estructura del repositorio:
   tecemer-lab1/
   │
   ├── src/
   │ └── tecemer_lab1/
   │ ├── **init**.py
   │ └── app.py
   │
   ├── .gitignore
   ├── pyproject.toml
   ├── requirements.txt
   └── README.md
5. Autor y Curso
   Autor: Angelo PAUCAR MARCA

Curso: Tecnologías Emergentes — ISO46B

## Flujo de Datos (Semana 2)

Fuente: API pública de Open-Meteo (pronóstico de 7 días para la ciudad de Huancayo).
Transformación: Procesamiento con Pandas para calcular la amplitud térmica diaria, detectar días lluviosos y clasificar los días según su temperatura máxima.
Salida: Archivos CSV exportados (pronostico_huancayo_procesado.csv y resumen_por_categoria.csv) listos para análisis visual o reportes.

## Cierre de la Unidad I — Semana 3

Herramienta de automatización: organizador.py clasifica y mueve archivos
de una carpeta en subcarpetas por tipo (Documentos, Imagenes, Videos,
Comprimidos, Otros), con modo de simulacion (--dry-run) mediante argparse.
Uso:

```
python organizador.py <carpeta> [--dry-run]
```

Pruebas: test_organizador.py cubre clasificacion, movimiento real y modo
simulacion, usando la fixture tmp_path de pytest para no afectar el
sistema de archivos real. Ejecutar con: pytest -v

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
