class Libro:
    def __init__(self, titulo, autor, isbn, materia):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.materia = materia
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False

    def devolver(self):
        if self.prestado:
            self.prestado = False
            return True
        return False