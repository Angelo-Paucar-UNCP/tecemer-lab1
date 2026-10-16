"""Módulo para organizar archivos de una carpeta automáticamente por su tipo."""


import argparse
from pathlib import Path
import shutil

# Las constantes globales van en MAYÚSCULAS y después de los imports.
CATEGORIAS = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".jpg": "Imágenes",
    ".jpeg": "Imágenes",
    ".png": "Imágenes",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
}


def clasificar(archivo: Path) -> str:
  """Determina la categoría de un archivo basándose en su extensión.

  Args:
    archivo: Objeto Path del archivo a clasificar.

  Returns:
    El nombre de la carpeta destino (categoría) o 'Otros'.
  """
  return CATEGORIAS.get(archivo.suffix.lower(), "Otros")


def organizar_carpeta(carpeta: Path, simulacion: bool = False) -> int:
  """Organiza los archivos de una carpeta en subcarpetas por su categoría.

  Args:
    carpeta: La ruta de la carpeta que se va a organizar.
    simulacion: Si es True, solo muestra los cambios sin mover archivos.

  Returns:
    El número total de archivos procesados.
  """
  movidos = 0
  for archivo in carpeta.iterdir():
    if archivo.is_dir() or archivo.name.startswith("."):
      continue

    categoria = clasificar(archivo)
    destino_carpeta = carpeta / categoria
    destino = destino_carpeta / archivo.name

    if simulacion:
      print(f"[SIMULACIÓN] {archivo.name} -> {categoria}")
    else:
      destino_carpeta.mkdir(exist_ok=True)
      shutil.move(str(archivo), str(destino))
      print(f"Movido: {archivo.name} -> {categoria}")
    movidos += 1
  return movidos


def main() -> None:
  """Función principal que ejecuta la CLI para organizar carpetas."""
  parser = argparse.ArgumentParser(description="Organiza archivos por tipo.")
  parser.add_argument("carpeta", type=Path, help="Carpeta a organizar")
  parser.add_argument(
      "--dry-run",
      action="store_true",
      help="Solo simula, no mueve archivos",
  )
  args = parser.parse_args()

  total = organizar_carpeta(args.carpeta, simulacion=args.dry_run)
  print(f"Total de archivos procesados: {total}")


if __name__ == "__main__":
  main()
