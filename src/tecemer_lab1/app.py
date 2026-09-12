import requests

try:
    respuesta = requests.get("https://official-joke-api.appspot.com/random_joke")
    respuesta.raise_for_status() # Verifica si hubo un error HTTP
    datos = respuesta.json()
    print(datos["setup"])
    print(datos["punchline"])
except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API: {e}")