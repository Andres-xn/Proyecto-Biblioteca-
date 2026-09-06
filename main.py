from biblioteca import Biblioteca, cargar_datos_demo, medir_rendimiento


def mostrar_libro(libro, isbn=None):
    if isbn is None:
        isbn = libro.get("isbn", "")

    print("\n" + "-" * 50)
    print(f"ISBN: {isbn}")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Categoría: {libro['categoria']}")
    print(f"Año: {libro['anio']}")
    print("-" * 50)


def mostrar_catalogo(biblioteca):
    libros = biblioteca.listar_libros()

    print("\n========== CATÁLOGO GENERAL ==========")
    if not libros:
        print("No existen libros registrados.")
        return

    for libro in libros:
        mostrar_libro(libro)

    print(f"Total de libros: {len(libros)}")


def buscar_libro(biblioteca):
    isbn = input("Ingrese el ISBN: ").strip()
    libro = biblioteca.buscar_por_isbn(isbn)

    if libro:
        mostrar_libro(libro, isbn)
    else:
        print("Libro no encontrado.")


def consultar_categoria(biblioteca):
    categoria = input("Ingrese la categoría: ").strip()
    libros = biblioteca.libros_por_categoria(categoria)

    print(f"\n===== LIBROS DE LA CATEGORÍA: {categoria.title()} =====")
    if not libros:
        print("No existen libros registrados en esa categoría.")
        return

    for libro in libros:
        print(f"- {libro['titulo']} | {libro['autor']} | ISBN: {libro['isbn']}")


def mostrar_reporte(biblioteca):
    reporte = biblioteca.reporte_estadistico()

    print("\n========== REPORTE ESTADÍSTICO ==========")
    print(f"Total de libros: {reporte['Total de libros']}")
    print(f"ISBN únicos: {reporte['ISBN únicos']}")
    print(f"Total de autores: {reporte['Total de autores']}")
    print(f"Año más antiguo: {reporte['Año más antiguo']}")
    print(f"Año más reciente: {reporte['Año más reciente']}")

    print("\nLibros por categoría:")
    categorias = reporte["Libros por categoría"]
    if categorias:
        for categoria, cantidad in categorias.items():
            print(f"- {categoria}: {cantidad}")
    else:
        print("Sin categorías registradas.")


def registrar_libro(biblioteca):
    print("\n========== REGISTRAR LIBRO ==========")
    isbn = input("ISBN: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoría: ")
    anio = input("Año de publicación: ")

    _, mensaje = biblioteca.registrar_libro(
        isbn, titulo, autor, categoria, anio
    )
    print(mensaje)


def mostrar_estructuras(biblioteca):
    print("\n========== ESTRUCTURAS DE DATOS ==========")
    print("\n1. CONJUNTO DE ISBN:")
    print(biblioteca.isbns)

    print("\n2. DICCIONARIO DE LIBROS:")
    for isbn, datos in biblioteca.libros.items():
        print(f"{isbn}: {datos}")

    print("\n3. MAPA DE CATEGORÍAS:")
    for categoria, isbns in biblioteca.mapa_categorias.items():
        print(f"{categoria}: {isbns}")


def prueba_rendimiento():
    print("\n========== PRUEBA DE RENDIMIENTO ==========")
    print("Procesando 10.000 registros...")
    resultado = medir_rendimiento(10000)

    print(f"Registros procesados: {resultado['registros']}")
    print(
        "Tiempo de inserción: "
        f"{resultado['tiempo_insercion_segundos']:.6f} segundos"
    )
    print(
        "Tiempo de búsqueda: "
        f"{resultado['tiempo_busqueda_segundos']:.6f} segundos"
    )


def main():
    biblioteca = Biblioteca()
    cargar_datos_demo(biblioteca)

    while True:
        print("\n============================================")
        print("   SISTEMA DE REGISTRO DE LIBROS - UEA")
        print("============================================")
        print("1. Registrar un libro")
        print("2. Mostrar catálogo completo")
        print("3. Buscar libro por ISBN")
        print("4. Consultar libros por categoría")
        print("5. Mostrar reporte estadístico")
        print("6. Mostrar conjuntos, mapas y diccionarios")
        print("7. Ejecutar prueba de tiempo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_libro(biblioteca)
        elif opcion == "2":
            mostrar_catalogo(biblioteca)
        elif opcion == "3":
            buscar_libro(biblioteca)
        elif opcion == "4":
            consultar_categoria(biblioteca)
        elif opcion == "5":
            mostrar_reporte(biblioteca)
        elif opcion == "6":
            mostrar_estructuras(biblioteca)
        elif opcion == "7":
            prueba_rendimiento()
        elif opcion == "8":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
