import json
import os

PATH = "libros.json"

def cargar_datos():
    if not os.path.exists(PATH):
        with open(PATH, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []
    with open(PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def guardar_datos(libros):
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

def registrar_libro():
    libros = cargar_datos()
    print("\n--- REGISTRAR LIBRO ---")
    titulo = input("Título: ")

    if any(l['titulo'].lower() == titulo.lower() for l in libros):
        print("Error: El libro ya existe.")
        return

    autor = input("Autor: ")
    genero = input("Género: ")
    anio = input("Año: ")
    
    nuevo = {
        "titulo": titulo, 
        "autor": autor, 
        "genero": genero, 
        "anio_publicacion": anio, 
        "estado": "Disponible", 
        "prestado_a": None
    }
    
    libros.append(nuevo)
    guardar_datos(libros)
    print(f"¡Libro '{titulo}' guardado con éxito!")

def ver_inventario():
    libros = cargar_datos()
    if not libros:
        print("\nEl inventario está vacío.")
        return
    print("\n--- INVENTARIO ---")
    for l in libros:
        estado = l['estado'] if not l['prestado_a'] else f"Prestado a {l['prestado_a']}"
        print(f"[{estado}] {l['titulo']} - {l['autor']} ({l['genero']})")