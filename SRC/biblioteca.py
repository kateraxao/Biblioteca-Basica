from libro import Libro
from usuario import Usuario
from libro import Libro
from usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    # -------------------------
    # Métodos de gestión
    # -------------------------

    def agregar_libro(self, titulo, autor, isbn, materia):
        libro = Libro(titulo, autor, isbn, materia)
        self.libros.append(libro)
        print("Libro agregado correctamente.")

    def registrar_usuario(self, nombre, id_usuario):
        usuario = Usuario(nombre, id_usuario)
        self.usuarios.append(usuario)
        print("Usuario registrado correctamente.")

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def prestar_libro(self, isbn, id_usuario):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(id_usuario)

        if libro and usuario:
            if libro.prestar():
                usuario.libros_prestados.append(libro)
                print("Libro prestado correctamente.")
            else:
                print("El libro ya está prestado.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(id_usuario)

        if libro and usuario:
            if libro in usuario.libros_prestados:
                libro.devolver()
                usuario.libros_prestados.remove(libro)
                print("Libro devuelto correctamente.")
            else:
                print("Ese usuario no tiene este libro.")
        else:
            print("Libro o usuario no encontrado.")

    def menu(self):
        while True:
            print("\n--- MENÚ BIBLIOTECA ---")
            print("1. Agregar libro")
            print("2. Registrar usuario")
            print("3. Prestar libro")
            print("4. Devolver libro")
            print("5. Ver libros")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                isbn = input("ISBN: ")
                materia = input("Materia: ")
                self.agregar_libro(titulo, autor, isbn, materia)

            elif opcion == "2":
                nombre = input("Nombre: ")
                id_usuario = input("ID usuario: ")
                self.registrar_usuario(nombre, id_usuario)

            elif opcion == "3":
                isbn = input("ISBN del libro: ")
                id_usuario = input("ID usuario: ")
                self.prestar_libro(isbn, id_usuario)

            elif opcion == "4":
                isbn = input("ISBN del libro: ")
                id_usuario = input("ID usuario: ")
                self.devolver_libro(isbn, id_usuario)

            elif opcion == "5":
                for libro in self.libros:
                    print(libro)

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")