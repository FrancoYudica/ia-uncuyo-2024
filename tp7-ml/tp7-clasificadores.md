## Punto 4 - Clasificador aleatorio

Tras clasificar aleatoriamente la peligrosidad de los árboles, se obtuvieron los siguientes resultados:

|                   | Predicho positivo | Predicho negativo                   |                       |
| ----------------- | ----------------- | ----------------------------------- | --------------------- |
| **Real positivo** | 1423              | 1438                                | Sensibilidad: 0.4973  |
| **Real Negativo** | 11293             | 11376                               | Especificidad: 0.5018 |
|                   | Precisión: 0.1119 | Valor negativo predictivo: 0.0.8878 | Exactitud: 0.5013     |

## Punto 5 - Clasificador por clase mayoritaria

|                   | Predicho positivo | Predicho negativo                 |                    |
| ----------------- | ----------------- | --------------------------------- | ------------------ |
| **Real positivo** | 0                 | 2861                              | Sensibilidad: 0.0  |
| **Real negativo** | 0                 | 22669                             | Especificidad: 1.0 |
|                   | Precisión: N/A    | Valor predictivo negativo: 0.8879 | Exactitud: 0.8879  |

Debido a que la clase mayoritaria es la de no peligrosos, todos los árboles sin inclinación peligrosa fueron correctamente predichos como no peligrosos.
La "Precisión" no se puede calcular (es indefinida o "N/A") cuando no hay predicciones positivas, y por eso no se puede mostrar un valor válido.
Además, la exactitud y el valor negativo predictivo coinciden con el porcentaje de árboles sin inclinación peligrosa,
