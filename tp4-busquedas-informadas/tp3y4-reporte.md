# Introducción
El objetivo de este proyecto es implementar distintos algoritmos de búsqueda no informada, definir medias de rendimiento y realizar comparativas de las distintas medidas y resultdos entre los algoritmos.
# Marco teórico y problema
Los algoritmos a implementar son BFS, DFS, UCS y A*, los cuales se pondrán a prueba en 30 entornos, donde cada entorno es una grilla cuadrada de 100x100 celdas. 
Existen 4 tipos de celda:
1. **Origen**: Celda inicial.
2. **Objetivo**: Celda que debe ser alcanzada por el agente.
3. **Congeldada**: Celda que el agente puede atravezar.
4. **Agujero**: Celda que el agente no puede atravezar.

El objetivo de los algoritmos es alcanzar la celda objetivo, partiendo de la celda origen.

Los algoritmos se pondrán a prueba en 30 entornos generados de manera pseudoaleatoria. Por cada entorno se ejecuan todos los algoritmos, asegurando que se pongan a prueba en entornos exáctamente iguales.

# Diseño experimental
# Análisis y resultados
## Cantidad de celdas exploradas
En el siguiente gráfico se presenta la variable de **celdas exploradas**, siendo esta la cantidad de celdas analizadas por cada algoritmo para poder encontrar el camino al objetivo.
![](images/all/explored_cells.png)
Es interesante observar que BFS y UCS funcionan de manera similar, debido a la función de costo seleccionada. El orden en el cuál se seleccionan los nodos a expandir en UCS no es el mismo que en BFS, pero también presenta un comportamiento similar de búsqueda de anchura.

## Cantidad de acciones tomadas
Los algoritmos generan un camino desde el punto de salida hacia el objetivo. En este contexto, la cantidad de acciones tomadas son las acciones que representan el camino para llegar a tal objetivo.
![](images/all/actions_count.png)
Se puede observar que BFS, UCS y A* toman la misma cantidad de acciones, esto se debe a que los tres algoritmos son **completos** y **óptimos**.

Además se puede observar que DFS es el que más acciones toma, y esto se debe a que DFS **no es óptimo**, pero si **completo**.

## Costo de las acciones tomadas

Este gráfico es muy parecido a el gráfico anterior, porque también se basa en las acciones para graficar, pero en lugar de graficar la cantidad de acciones, se grafica el costo total de las acciones tomadas para alcanzar el objetivo.

El costo de cada acción se calcula según su índice:
- Izquierda: 1
- Abajo: 2
- Derecha: 3
- Arriba: 4

![](images/all/actions_cost.png)
En este caso, DFS claramente toma un costo mayor, debido a que no es óptimo, a diferencia del resto los algoritmos que si lo son.
Tanto BFS, UCS y A* toman el mismo costo, a pesar de que en ciertas situaciones los algoritmos toman caminos distintos. Es interesante observar que esto se debe a la propia naturaleza del entorno rectangular. Independientemente del camino tomado, si el camino es óptimo entonces los costos van a coincidir.


## Tiempo tomado
A continuación grafico la variable del tiempo para los algoritmos.
![](images/all/time_taken.png)

DFS tiene muchas aplicaciones interesantes, pero no destaca por la búsqueda de caminos, por no ser óptimo. Esto significa que por cada nodo se van a generar ramificaciones, las cuales se alejan rápidamente del nodo inicial, siendo este el motivo principal por el cuál, en promedio, toma menos tiempo que BFS. BFS amplía los nodos cercanos primero, y a medida que la frontera se hace más grande, se recorre una menor cantidad de celdas. En definitiva BFS no es ideal, por lo menos temporalmente, cuando tenemos un objetivo lejano.
UCS toma una cantidad significativa de tiempo más que BFS, debido a que se debe ordenar la frontera constantemente, y la función de costo seleccionada no es ideal.


# Conclusión
