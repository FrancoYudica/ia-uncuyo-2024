## Preprocesamiento

### Eliminación de variables

Para reducir la cantidad de datos ingresados al algoritmo y evitar relacionar datos sin sentido, eliminé las siguientes variables:

- **id**: El ID es simplemente un atributo para identificar al árbol, cuyo valor no tiene ninguna relación con su peligrosidad.
- **ultima_modificacion**: Se refiere a la fecha actualización de los contenidos de la fila en la base de datos.
- **nombre_sección**: Considero que saber la sección a la que pertenece un árbol es importante, pero decido eliminar el nombre_sección debido a que existe otro atributo que provee la misma información, **sección**, pero a diferencia de **nombre_sección**, este es un entero.

### Undersampling

Nos encontramos frente a un conjunto de datos altamente desbalanceado, donde el 88.79% de los árboles no son peligrosos. Por este motivo, decidí balancear los valores de la clase _inclinacion_peligrosa_, y lo hice con **undersampling**, lo cuál me dio los mejores resultados.

## Resultados sobre el conjunto de validación

| Metric          | Value  |
| --------------- | ------ |
| **Accuracy**    | 0.6803 |
| **Precision**   | 0.9478 |
| **Sensitivity** | 0.6770 |
| **Specificity** | 0.7061 |
| **AUC Score**   | 0.7573 |

De los resultados se puede observar que:

- La **precision** es alta (0.9478), lo que indica que cuando se hace una predicción positiva (`inclinacion_peligrosa=1`), es correcta el 95% de las veces.

- La **sensitivity** nos dice que el modelo detectó exitosamente el 68% de los casos positivos (`inclinacion_peligrosa=1`).

- La **specificity** nos dice que el modelo detectó exitosamente el 71% de los casos negativos (`inclinacion_peligrosa=0`).

## Resultados obtenidos en Kaggle

![](images/b/submission_results_public_leaderboard.png)
Coun un `AUC = 0.76793` en la tabla pública.
Se puede observar que el _AUC_ obtenido es similar al calculado previamente sobre el conjunto de datos de validación, `Validation AUC = 0.7573`

## Descripción del algoritmo

```r
# Load
raw_dataset_train <- read.csv("../../data/arbolado-mendoza-dataset-train.csv")
raw_dataset_validation <- read.csv("../../data/arbolado-mendoza-dataset-validation.csv")
raw_dataset_test <- read.csv("../../data/arbolado-mza-dataset-test.csv")

# Clean
dataset_train <- raw_dataset_train %>% select(-id, -ultima_modificacion, -nombre_seccion)
dataset_validation <- raw_dataset_validation
```

Lo primero, es cargar los conjuntos de datos, y limpiar o eliminar atributos que no voy a utilizar. Se puede observar que se eliminan los atributos únicamente en el conjunto de entrenamiento, debido a que este será el conjunto con el cuál se entrenará el modelo.

```r
majority_class <- dataset_train %>% filter(inclinacion_peligrosa == 0)
minority_class <- dataset_train %>% filter(inclinacion_peligrosa == 1)

# Ensure equal counts by undersampling the majority class
majority_undersampled <- majority_class %>% sample_n(nrow(minority_class))

# Combine undersampled majority with minority class
merged_dataset <- rbind(minority_class, majority_undersampled)
```

Para poder aplicar undersampling, encuentro la clase mayoriataria y minoritaria. Luego selecciono igual cantidad de filas igual a las de la clase minoritaria sobre la clase mayoritaria, y finalmente mezclo los conjuntos de datos. De esta forma el conjunto de datos final tiene una distribución equitativa de las clases.

```r
rf_model <- ranger(
    inclinacion_peligrosa ~ .,
    data = merged_dataset
)
```

Utilizo el algoritmo **random forest** de la librería ranger para obtener el modelo. Nótese que se especifica que la varible a predecir es _inclinación_peligrosa_ y las restantes son las predictoras.

```r
show_confusion_matrix <- function(model, dataset) {
    predictions <- predict(model, dataset)$predictions
    # Maps predictions in range [0, 1] to binary values, the threshold is 50%
    binary_predictions <- ifelse(predictions >= 0.5, 1, 0)
    confusion_matrix <- confusionMatrix(
        as.factor(binary_predictions),
        as.factor(dataset$inclinacion_peligrosa)
    )
    metrics_summary <- c(
        accuracy = confusion_matrix$overall["Accuracy"],
        precision = confusion_matrix$byClass["Precision"],
        sensitivity = confusion_matrix$byClass["Sensitivity"],
        specificity = confusion_matrix$byClass["Specificity"]
    )
    print(metrics_summary)
}

show_auc <- function(model, dataset) {
    predictions <- predict(model, dataset)$predictions

    # AUC is calculated using the predicted probabilities and the true labels
    auc <- roc(dataset$inclinacion_peligrosa, predictions)$auc
    print(paste("AUC Score:", auc))
}

show_confusion_matrix(rf_model, dataset_validation)
show_auc(rf_model, dataset_validation)
```

Se definen dos funciones, una para calcular las métricas de la matriz de confusión, y la otra para calcular el AUC.
Posteriormente, se miestran por pantalla los resultados del modelo sobre el conjunto de validación.

```R
predictions <- predict(rf_model, raw_dataset_test)$predictions

submission <- data.frame(id = raw_dataset_test$id, inclinacion_peligrosa = predictions)

write_csv(submission, "arbolado-mza-dataset-submission.csv")
```

Finalmente, se realizan las predicciones sobre el conjunto de datos de test y se crea y guarda un data frame que mapea los ID de los árboles a los resultados predecidos:

| id  | inclinacion_peligrosa |
| --- | --------------------- |
| 1   | 0.2700222775795118    |
| 2   | 0.29827375524246785   |
| 4   | 0.16302061726523812   |
| ... | ...                   |
