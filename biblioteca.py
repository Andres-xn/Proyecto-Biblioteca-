from collections import defaultdict
from time import perf_counter
import random


class Biblioteca:
    """Gestiona el registro, organización y consulta de libros."""

    def __init__(self):
        # CONJUNTO: almacena ISBN únicos y evita duplicados.
        self.isbns = set()

        # DICCIONARIO: clave = ISBN, valor = datos del libro.
        self.libros = {}

        # MAPA: clave = categoría, valor = conjunto de ISBN de esa categoría.
        self.mapa_categorias = defaultdict(set)

    def registrar_libro(self, isbn, titulo, autor, categoria, anio):
        isbn = isbn.strip()
        titulo = titulo.strip()
        autor = autor.strip()
        categoria = categoria.strip().title()

        if not isbn or not titulo or not autor or not categoria:
            return False, "Todos los campos son obligatorios."

        if isbn in self.isbns:
            return False, f"El ISBN {isbn} ya se encuentra registrado."

        try:
            anio = int(anio)
        except ValueError:
            return False, "El año debe ser un número entero."

        self.isbns.add(isbn)
        self.libros[isbn] = {
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "anio": anio,
        }
        self.mapa_categorias[categoria].add(isbn)
        return True, f"Libro '{titulo}' registrado correctamente."

    def buscar_por_isbn(self, isbn):
        return self.libros.get(isbn.strip())

    def listar_libros(self):
        return [
            {"isbn": isbn, **self.libros[isbn]}
            for isbn in sorted(self.libros)
        ]

    def libros_por_categoria(self, categoria):
        categoria = categoria.strip().title()
        isbns = self.mapa_categorias.get(categoria, set())
        return [
            {"isbn": isbn, **self.libros[isbn]}
            for isbn in sorted(isbns)
        ]

    def reporte_estadistico(self):
        autores = {datos["autor"] for datos in self.libros.values()}
        anios = [datos["anio"] for datos in self.libros.values()]

        return {
            "Total de libros": len(self.libros),
            "ISBN únicos": len(self.isbns),
            "Total de autores": len(autores),
            "Libros por categoría": {
                categoria: len(isbns)
                for categoria, isbns in sorted(self.mapa_categorias.items())
            },
            "Año más antiguo": min(anios) if anios else "Sin datos",
            "Año más reciente": max(anios) if anios else "Sin datos",
        }


def cargar_datos_demo(biblioteca):
    datos = [
        ("978-84-376-0494-7", "Cien años de soledad", "Gabriel García Márquez", "Literatura", 1967),
        ("978-84-204-8297-2", "Don Quijote de la Mancha", "Miguel de Cervantes", "Clásicos", 1605),
        ("978-0-13-235088-4", "Clean Code", "Robert C. Martin", "Programación", 2008),
        ("978-1-59327-928-8", "Python Crash Course", "Eric Matthes", "Programación", 2019),
        ("978-0-262-03384-8", "Introduction to Algorithms", "Cormen et al.", "Computación", 2009),
    ]

    for libro in datos:
        biblioteca.registrar_libro(*libro)


def medir_rendimiento(n=10000):
    """Prueba sencilla del tiempo de inserción y búsqueda."""
    biblioteca = Biblioteca()

    inicio = perf_counter()
    for i in range(n):
        biblioteca.registrar_libro(
            f"978-{i:010d}",
            f"Libro {i}",
            f"Autor {i % 250}",
            f"Categoria {i % 20}",
            2000 + (i % 26),
        )
    tiempo_insercion = perf_counter() - inicio

    indices = [random.randrange(n) for _ in range(n)]
    inicio = perf_counter()
    for i in indices:
        biblioteca.buscar_por_isbn(f"978-{i:010d}")
    tiempo_busqueda = perf_counter() - inicio

    return {
        "registros": n,
        "tiempo_insercion_segundos": tiempo_insercion,
        "tiempo_busqueda_segundos": tiempo_busqueda,
    }
