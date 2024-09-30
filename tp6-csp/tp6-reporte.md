## Ejercicio 1 - CSP para Sudoku
Para todo problema de CSP se debe definir el conjunto de variables, el dominio de cada varible y las restricciones.
 - X: Conjunto de variables. Van a haber tantas varaibles como dimensión del tablero, usualmente 9x9, 81 variables
 - D: El dominio inicial de las variables es [1, 2, ..., 8, 9]
 - C: Las restricciones son las siguientes:
    1. En cada fila, todos los números son únicos.
    2. En cada columna, todos los números son únicos.
    3. En cada bloque 3x3, todos los números son únicos.


Para resolverlo, se usa el algoritmo de consistencia de arcos, `ac3`. Es posible resolverlo mediante este algoritmo, debido a que sudoku es un problema de satisfacción de condiciones, y solamente existe una única configuración del tablero que satisface el problema.
El problema será resuelto cuando el dominio de cada una de las variables sea exáctamente 1.

En `ac3` existe el concepto de vecinos, que son nodos sobre los cuales se aplican las restricciones. En el caso de sudoku, las restricciones de un nodo se aplican sobre los otros nodos de la misma fila, misma columna y mismo bloque.
