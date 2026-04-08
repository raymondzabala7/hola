from gestion_libros import cargar_datos, guardar_datos

def prestar_libro():
    libros = cargar_datos()
    titulo = input("\nTítulo del libro a prestar: ")
    for l in libros:
        if l['titulo'].lower() == titulo.lower():
            if l['estado'] == "Disponible":
                l['prestado_a'] = input("Nombre del usuario: ")
                l['estado'] = "Prestado"
                guardar_datos(libros)
                print("Préstamo registrado.")
                return
            else:
                print("El libro ya está prestado.")
                return
    print("Libro no encontrado.")

def devolver_libro():
    libros = cargar_datos()
    titulo = input("\nTítulo del libro a devolver: ")
    for l in libros:
        if l['titulo'].lower() == titulo.lower():
            l['estado'] = "Disponible"
            l['prestado_a'] = None
            guardar_datos(libros)
            print("Devolución exitosa.")
            return
    print("Libro no encontrado.")