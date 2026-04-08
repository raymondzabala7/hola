from gestion_libros import cargar_datos
import json
import os

def generar_reporte():
    libros = cargar_datos()
    if not libros:
        print("No hay datos.")
        return

    print("\n--- REPORTE DE INVENTARIO ---")
    for l in libros:
        print(f"Libro: {l['titulo']} | Estado: {l['estado']}")

    nombre_rep = "reporte_libros_2026.json"
    with open(nombre_rep, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)
    print(f"\nArchivo '{nombre_rep}' generado.")