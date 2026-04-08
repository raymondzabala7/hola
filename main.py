import gestion_libros
import buscar_libros
import prestamos
import reportes

def menu():
    while True:
        print("\n==========================================")
        print("    SISTEMA DE BIBLIOTECA VIRTUAL")
        print("==========================================")
        print("1. Registrar nuevo libro")
        print("2. Ver inventario completo")
        print("3. Buscar un libro")
        print("4. Prestar un libro")
        print("5. Devolver un libro")
        print("6. Generar reporte")
        print("7. Salir")
        print("==========================================")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestion_libros.registrar_libro()
        elif opcion == "2":
            gestion_libros.ver_inventario()
        elif opcion == "3":
            buscar_libros.buscar_libro()
        elif opcion == "4":
            prestamos.prestar_libro()
        elif opcion == "5":
            prestamos.devolver_libro()
        elif opcion == "6":
            reportes.generar_reporte()
        elif opcion == "7":
            print("Saliendo... ¡Adiós!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()