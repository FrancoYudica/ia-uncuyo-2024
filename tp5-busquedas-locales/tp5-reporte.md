- La cantidad máxima de estados para todos los algoritmos es 800
- En simulated annealing la función de schedule es `s(t) = 100 * pow(0.95, t)`
# Tiempos de ejecucion

![](images/execution_time/box&whiskers_queen_count=4.png)
![](images/execution_time/box&whiskers_queen_count=8.png)
![](images/execution_time/box&whiskers_queen_count=10.png)
![](images/execution_time/box&whiskers_queen_count=12.png)
![](images/execution_time/box&whiskers_queen_count=15.png)

# Estados atravesados
![](images/traversed_states/box&whiskers_queen_count=4.png)
![](images/traversed_states/box&whiskers_queen_count=8.png)
![](images/traversed_states/box&whiskers_queen_count=10.png)
![](images/traversed_states/box&whiskers_queen_count=12.png)
![](images/traversed_states/box&whiskers_queen_count=15.png)

# Valores de H
Las siguientes imágenes no fueron seleccionadas aleatoriamente, sinó que son los casos más cercanos al óptimo global, minimizando la cantidad de estados explorados
![](images/h_values/hill_climb/queen_count=12.png)
![](images/h_values/simulated_annealing/queen_count=12.png)
![](images/h_values/genetic/queen_count=12.png)
