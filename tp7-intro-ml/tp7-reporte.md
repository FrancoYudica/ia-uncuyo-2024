## 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

### (a) The sample size n is extremely large, and the number of predictors p is small.

Un modelo de aprendizaje estadístico flexible va a ser mejor en este caso, debido a que se podrá ajustar mejor a los patrones entre los datos.

### (b) The number of predictors p is extremely large, and the number of observations n is small.

Probablemente rindan peor que los modelos inflexibles. Los modelos flexibles requieren gran cantidad de datos, pero este no es el caso, y es altamente probable que se genere _overfitting_. Probablemente un método inflexible obtenga mejores generalizaciones, evitando _overfitting_.

### (c) The relationship between the predictors and response is highly non-linear.

Un método flexible va a obtener mejores resultados. Los modelos flexibles son mejores en aquellas ocasiones donde se buscan capturar relaciones no lineales, siendo esta la debilidad de los modelos inflexibles.

### (d) The variance of the error terms, i.e. σ^2 = Var(ϵ), is extremely high.

Si hay mucha varianza en el error, entonces los datos van a ser extremadamente "ruidosos". Los modelos flexibles tienden sobreajustar el ruido en los datos, obteniendo peores generalizaciones. Un modelo inflexible tendrá un mejor rendimiento al suavizar el ruido.

## 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

### (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.

Regresión (El salario del CEO es una variable continua)
Estamos interesados en realizar inferencia. Buscamos entender las relaciones entre los predictores y el salario del CEO.

- **n**: 500 (firmas)
- **p**: 3 (profit, número de empleados, industria, el salario del CEO no porque es lo que queremos predecir)

### (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

Clasificación (Exito/Fracaso es una variable categórica)
Predicción: Se busca predecir si el producto nuevo va a tener éxito en función de los históricos sobre productos anteriores.
**n**: 20 (productos)
**p**: 13

### (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

Regresión (porcentaje de cambio en el cambio USD/Euro es continuo)
Predicción
**n**: 52 (cantidad de semanas de 2012)
**p**: 3

## 5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

### Métodos flexibles

#### Ventajas

- Pueden capturar patrones y relaciones no lineales.
- Se puede obtener un menor error
- Pueden rendir mejor en grandes conjuntos de datos

#### Desventajas

- Más propensos a sobreajustar (overfitting), especialmente en conjuntos de datos pequeños
- Presentan mayor varianza
- Requieren mayor cantidad de datos y recursos computacionales

### Métodos inflexibles

#### Ventajas

- Menos propensos a hacer sobreajustes, especialmente en los conjuntos de datos pequeños
- Menor varianza
- Fácil interpretación

#### Desventajas

- Puede pasar por alto patrones importantes debido al alto sesgo (bias)
- Dificultad al aplicarlos en relaciones complejas no lineale

## 6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are its disadvantages?

### Enfoque Paramétrico

Asume una forma específica para el modelo (por ejemplo, regresión lineal o logística). Número fijo de parámetros, independientemente del tamaño de los datos.

### Enfoque No Paramétrico

No hace suposiciones fuertes sobre la forma del modelo. El número de parámetros crece con el tamaño de los datos.

### Ventajas y desventajas de los modelos paramétricos

| **Aspecto**                 | **Ventajas**                                                   | **Desventajas**                                                               |
| --------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Simplicidad**             | Fácil de interpretar y entender                                | Puede pasar por alto relaciones complejas en los datos                        |
| **Cómputo**                 | Rápido y eficiente computacionalmente                          | Menos flexible, puede rendir mal con datos complejos                          |
| **Requerimientos de datos** | Funciona bien con conjuntos de datos pequeños                  | El rendimiento se ve afectado si el conjunto de datos es complejo o no lineal |
| **Riesgo de sobreajuste**   | Menor riesgo de sobreajuste debido a la simplicidad del modelo | Propenso al subajuste si las suposiciones son incorrectas                     |
| **Suposiciones**            | Fuerte base teórica, comportamiento predecible                 | Suposiciones rígidas pueden llevar a predicciones sesgadas o inexactas        |

## 7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

| Obs | X1  | X2  | X3  | Y     |
| --- | --- | --- | --- | ----- |
| 1   | 0   | 3   | 0   | Red   |
| 2   | 2   | 0   | 0   | Red   |
| 3   | 0   | 1   | 3   | Red   |
| 4   | 0   | 1   | 2   | Green |
| 5   | −1  | 0   | 1   | Green |
| 6   | 1   | 1   | 1   | Red   |

### Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.

#### (a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.

La distancia euclideana se calcula con la siguiente formula:
`Di(X1, X2, X3) = sqrt((X1-Xi1)² + (X2-Xi2)² + (X1-Xi1)²)`
Donde Xi representa el valor de las distints observaciones.

En nuestro caso, queremos predecir cuando `X1 = X2 = X3 = 0`, por lo tanto la función de distancia se reduce a: `Di(0, 0, 0) = sqrt(Xi1² + Xi2² + Xi1²)`

Luego, para cada una de las observaciones `i` se obtienen los siguientes resultados:

- `D1(0, 0, 0) = sqrt(0² + 3² + 0²) = 3`
- `D2(0, 0, 0) = sqrt(2² + 0² + 0²) = 2`
- `D3(0, 0, 0) = sqrt(0² + 1² + 3²) = sqrt(10) = 3.1622...`
- `D4(0, 0, 0) = sqrt(0² + 1² + 2²) = sqrt(5) = 2.2360...`
- `D5(0, 0, 0) = sqrt((-1)² + 0² + 1²) = sqrt(2) = 1.4142...`
- `D5(0, 0, 0) = sqrt(1² + 1² + 1²) = sqrt(3) = 1.7320...`

#### (b) What is our prediction with K = 1? Why?

Nuestra predicción será que para la entrada `(X1=0, X2=0, X3=0)`, se obtendrá `Y=Green`, debido a que la observación 5 toma como distancia euclidena 1.4142, siendo esta la más cercana a `K=1`.

#### (c) What is our prediction with K = 3? Why?

La observación más cercana a `K=3` según la distancia euclideana es la número 1, por lo tanto, el valor predecido para `(X1=0, X2=0, X3=0)` será `Y=Red`.

#### (d) If the Bayes decision boundary in this problem is highly non-linear, then would we expect the best value for K to be large or small? Why?

Cuando la frontera de decisión de Bayes es altamente no lineal, esperamos que la relación entre los predictores y la respuesta sea compleja.
En tales casos, se prefiere un valor pequeño de _K_ porque permite que el modelo capture patrones locales en los datos de manera más efectiva. Un _K_ grande suavizaría estos patrones locales, lo que podría simplificar en exceso la frontera de decisión y perder relaciones no lineales importantes.
Entonces, si la frontera de decisión es altamente no lineal, es probable que un _K_ pequeño rinda mejor.
