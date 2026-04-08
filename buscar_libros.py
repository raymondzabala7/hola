from gestion_libros import cargar_datos

def buscar_libro():
    libros = cargar_datos()
    if not libros:
        print("\nNo hay libros registrados.")
        return

    print("\n--- BUSCADOR ---")
    criterio = input("Ingrese Título, Autor o Género a buscar: ").lower()
    encontrados = []

    for l in libros:
        if (criterio in l['titulo'].lower() or 
            criterio in l['autor'].lower() or 
            criterio in l['genero'].lower()):
            encontrados.append(l)

    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} resultados:")
        for l in encontrados:
            estado = l['estado'] if not l['prestado_a'] else f"Prestado a {l['prestado_a']}"
            print(f"-> {l['titulo']} | Autor: {l['autor']} | Género: {l['genero']} | Estado: {estado}")
    else:
        print(f"No se encontraron libros que coincidan con '{criterio}'.")