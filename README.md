# Sistema de registro de libros - Guía de Práctica N.° 3

Proyecto desarrollado en Python para registrar, organizar y consultar libros de una biblioteca utilizando **conjuntos, mapas y diccionarios**.

## Estructuras de datos utilizadas

- **Conjunto (`set`)**: almacena los ISBN y evita que se registren ISBN duplicados.
- **Diccionario (`dict`)**: relaciona cada ISBN con los datos completos del libro.
- **Mapa de categorías (`defaultdict(set)`)**: relaciona cada categoría con los ISBN de los libros que pertenecen a ella.

## Funciones del sistema

1. Registrar un libro.
2. Mostrar el catálogo completo.
3. Buscar un libro por ISBN.
4. Consultar libros por categoría.
5. Mostrar un reporte estadístico.
6. Mostrar directamente las estructuras de datos utilizadas.
7. Ejecutar una prueba de tiempo con 10.000 registros.
8. Salir del sistema.

## Requisitos

- Python 3.9 o superior.
- Visual Studio Code.
- Extensión de Python para Visual Studio Code.

No se necesitan librerías externas.

## Ejecución

Abrir esta carpeta en Visual Studio Code y ejecutar:

```bash
python main.py
```

En Windows también puede funcionar:

```bash
py main.py
```

## Agente de IA

Para apoyar la organización del código, documentación y revisión de la solución se utilizó ChatGPT de OpenAI. El porcentaje declarado en el informe debe corresponder al uso real que el estudiante haga del código y a las modificaciones realizadas personalmente.
