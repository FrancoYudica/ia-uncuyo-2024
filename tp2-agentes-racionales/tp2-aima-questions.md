## Considere una version modificada del entorno de la aspiradora donde el agente es penalizado por cada movimiento

### ¿Puede un agente reflexivo simple ser perfectamente racional en este escenario?
Interpretando el concepto de "perfectamente racional" como un agente que logra resolver el problema minimizando la función de desempeño, el agente reflexivo simple no podría serlo en este caso. Esto se debe a que el simple hecho de agregar penalizaciones no brindaría información adicional que permita modificar el comportamiento del agente para lograr el mejor resultado posible. De igual manera, el agente se moverá constantemente, lo que haría que, en la mayoría de los casos, el rendimiento resulte negativo.

### ¿Y si fuera un agente reflexivo con estado?
El agente podría almacenar la posición de las casillas por las que pasó, pero no podría saber cuáles son las casillas sucias hasta que pase por todas ellas. Por lo tanto, no podría ser perfectamente racional.

### ¿Y si conoce cuales son las casillas sucias y limpias del entorno?
En este caso, sí se lograría un agente racional, tal que solo pase por las casillas que están sucias. Además, si no es posible que pase solo por casillas sucias, entonces la función de penalización va a actuar, degradando el rendimiento de aquellos agentes que no optimicen los caminos para realizar la limpieza.

## Considere ahora una versión modificada donde el las características del entorno tales como el tamaño y el porcentaje de suciedad son desconocidos.

### ¿Puede un agente reflexivo simple ser perfectamente racional?
No puede ser perfectamente racional. Los agentes reflexivos simples solo conocen su estado actual y toman decisiones en función de ese estado. Es imposible realizar un algoritmo perfectamente racional dadas las restricciones de los agentes reflexivos simples.

### ¿Puede un agente aleatorio superar en términos de rendimiento a un agente reflexivo simple?
En general, no es posible, y esto lo hemos comprobado empíricamente a través de los resultados obtenidos en este proyecto. Pero cabe aclarar que ninguno de los dos es perfectamente racional, y es por este motivo que hay casos, simulaciones en específico, donde el agente aleatorio presenta mejores resultados que un reflexivo simple. Sin embargo, esto no se cumple cuando analizamos la media de los rendimientos, la cual nos dice que los agentes reflexivos simples son mejores que los aleatorios.

### ¿Podrías diseñar un entorno donde el agente aleatorio tenga un mal rendimiento?
En este caso, podemos usar dos parámetros: el porcentaje de suciedad y el tamaño del entorno. Si queremos minimizar la función de rendimiento, que tiene como resultado la cantidad de casillas limpiadas, entonces basta con hacer el entorno lo más pequeño posible. Pero también podríamos hacer el entorno muy grande, con un porcentaje de suciedad bajo, esperando que las casillas sucias queden en el lado opuesto del agente.

### ¿Puede un agente reflexivo con estados superar un agente reflexivo simple?
El agente reflexivo con estados podría almacenar información sobre las casillas por las que pasó previamente. Por este motivo, resulta posible desarrollar un algoritmo que optimice los movimientos, de tal modo que se evite pasar por casillas previas.