## Árbol de decisión con Id3 discreto

Tras implementar el algoritmo Id3, he obtenido el siguiente árbol de decisión:

```python
decision_tree = {
    'outlook': {
        'overcast': 'yes',
        'rainy': {
            'windy': {
                False: 'yes',
                True: 'no'
            }
        },
        'sunny': {
            'humidity': {
                'high': 'no',
                'normal': 'yes'
            }
        }
    }
}
```

Se puede observar que no hay overfitting, debido a que el árbol no detalla explícitamente a todas las obervaciones, y en las distintas ramificaciones no se consideran todos los atributos.

La interpretación del árbol sería la siguiente:

- Si está nublado, se juega.
- Si está lloviendo y no hay viento, se juega.
- Si está soleado y no hay mucha humedad se juega.

Con este árbol, he obtenido un 100% de **accuracy** o **exactitud**, lo cuál significa que el árbol predice correctamente a todas las obervaciones. Nótese que las obervaciones con las cuáles evalué, son las mismas del entrenamiento.

## Id3 con valores reales

Los datos reales requieren estrategias distintas a los discretos para poder construir árboles de decisión efectivamente.

### Discretización en puntos de corte

La estrategia más común para manejar datos continuos es dividir el dominio de los valores reales en intervalos, identificando un "punto de corte" (threshold) que maximice alguna métrica de separación como la ganancia de información.

### Agrupación en intervalos (Binning)

Otra estrategia es dividir los valores continuos en intervalos predefinidos o dinámicos antes de construir el árbol. Este proceso se llama binning, y puede ser supervisado (basado en la variable objetivo) o no supervisado (simplemente dividiendo el rango de valores).

- **Binning no supervisado**: Divide el rango de un atributo continuo en intervalos iguales o según la distribución de los datos (por ejemplo, cuantiles).
- **Binning supervisado**: Los intervalos se seleccionan para maximizar alguna métrica supervisada (como la ganancia de información) utilizando la variable de salida.

### Árboles de regresión

Si tratamos de predecir resultados numéricos, entonces necesitamos un árbol de regresión en lugar de uno de clasificación. Un árbol de regresioń tiene en cada hoja una función lineal sobre algún subconjunto de valores numéricos reales, en lugar de un solo valor.
