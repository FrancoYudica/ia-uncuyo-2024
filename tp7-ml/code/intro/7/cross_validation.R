# Cargar librerías necesarias
library(rpart)
library(dplyr) # Para manipulación de datos
library(caret) # Para las métricas y cálculos de rendimiento


create_folds <- function(dataset, k) {
    # Obtener los índices del dataframe
    indices <- seq_len(nrow(dataset))

    # Mezclar los índices para asegurar una distribución aleatoria
    set.seed(123)
    shuffled_indices <- sample(indices)

    # Dividir los índices en k folds de tamaño aproximadamente igual
    folds <- split(shuffled_indices, cut(seq_along(shuffled_indices), breaks = k, labels = FALSE))

    # Crear una lista con nombres apropiados para cada fold
    fold_list <- lapply(seq_len(k), function(i) folds[[i]])
    # names(fold_list) <- paste0("Fold", seq_len(k))

    return(fold_list)
}


# Función de validación cruzada
cross_validation <- function(dataset, k) {
    # Elimina el atributo de ultima_modificacion
    dataset <- dataset %>% select(-ultima_modificacion)

    # Filter out rows where the 'especie' has levels that are not in the training data
    dataset <- dataset %>%
        filter(especie %in% levels(dataset$especie))


    # Crear los folds
    folds <- create_folds(dataset, k)

    # Inicializar vectores para almacenar las métricas de cada fold
    accuracies <- c()
    precisions <- c()
    sensitivities <- c()
    specificities <- c()

    # Loop sobre cada fold
    for (i in seq_len(k)) {
        # Obtener los índices de entrenamiento y test para el fold actual
        test_indices <- folds[[i]]
        train_indices <- setdiff(seq_len(nrow(dataset)), test_indices)

        # Dividir el dataset en conjunto de entrenamiento y test
        train_data <- dataset[train_indices, ]
        test_data <- dataset[test_indices, ]

        # Entrenar el modelo de árbol de decisión en los datos de entrenamiento
        model <- rpart(inclinacion_peligrosa ~ ., data = train_data, method = "class")

        # Hacer predicciones en los datos de test
        predictions <- predict(model, test_data, type = "class")

        # Calcular la matriz de confusión
        confusion_matrix <- confusionMatrix(as.factor(predictions), as.factor(test_data$inclinacion_peligrosa))

        # Extraer las métricas
        accuracies <- c(accuracies, confusion_matrix$overall["Accuracy"])
        precisions <- c(precisions, confusion_matrix$byClass["Precision"])
        sensitivities <- c(sensitivities, confusion_matrix$byClass["Sensitivity"])
        specificities <- c(specificities, confusion_matrix$byClass["Specificity"])
    }

    # Calcular la media y desviación estándar de cada métrica
    metrics_summary <- list(
        accuracy_mean = mean(accuracies),
        accuracy_sd = sd(accuracies),
        precision_mean = mean(precisions),
        precision_sd = sd(precisions),
        sensitivity_mean = mean(sensitivities),
        sensitivity_sd = sd(sensitivities),
        specificity_mean = mean(specificities),
        specificity_sd = sd(specificities)
    )

    return(metrics_summary)
}

dataset <- read.csv("../../../data/arbolado-mendoza-dataset-train.csv")


# Ejemplo de uso con un dataframe llamado 'dataset'
metrics_summary <- cross_validation(dataset, 4)

# Mostrar los resultados
metrics_summary
