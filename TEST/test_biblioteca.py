from src.libro import Libro

def test_prestar_libro():
    libro = Libro("Python", "Ana", "123", "Programación")
    assert libro.prestar() == True