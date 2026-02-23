from libro import Libro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, isbn, id_usuario):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(id_usuario)

        if libro and usuario and libro.prestar():
            usuario.libros_prestados.append(libro)
            print("Libro prestado correctamente")
        else:
            print("No se pudo prestar el libro")