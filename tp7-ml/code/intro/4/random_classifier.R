# Cargar la librería ggplot2 (si es necesaria para otros gráficos futuros)
library(ggplot2)
library(dplyr)

# Leer el archivo CSV
dataset <- read.csv("../../../data/arbolado-mendoza-dataset-train.csv")

add_random_prediction_prob <- function(dataset) {
    # Añade una nueva columna 'prediction_prob' con valores aleatorios entre 0 y 1
    dataset$prediction_prob <- runif(nrow(dataset), min = 0, max = 1)
    return(dataset)
}

random_classifier <- function(dataset) {
    random_prediction_prob_dataset <- add_random_prediction_prob(dataset)

    # Categorizar la variable 'prediction_prob' en la nueva variable 'prediction_class'
    random_prediction_prob_dataset$prediction_class <- cut(
        random_prediction_prob_dataset$prediction_prob,
        breaks = c(0, 0.5, 1.0), # Definir los intervalos
        labels = c("0", "1"), # Las etiquetas deben ser cadenas de caracteres
        right = FALSE # Intervalos cerrados por la izquierda (incluye el límite inferior)
    )

    # Devolver el dataset modificado
    return(random_prediction_prob_dataset)
}

dataset_prediction_class <- random_classifier(dataset)

# Calcular las métricas utilizando dplyr
results <- dataset_prediction_class %>% summarise(
    True_Positives = sum(inclinacion_peligrosa == 1 & prediction_class == 1), # Árboles con inclinación peligrosa correctamente predichos (TP)
    True_Negatives = sum(inclinacion_peligrosa == 0 & prediction_class == 0), # Árboles sin inclinación peligrosa correctamente predichos (TN)
    False_Positives = sum(inclinacion_peligrosa == 0 & prediction_class == 1), # Árboles sin inclinación peligrosa predichos incorrectamente como peligrosos (FP)
    False_Negatives = sum(inclinacion_peligrosa == 1 & prediction_class == 0) # Árboles con inclinación peligrosa predichos incorrectamente como no peligrosos (FN)
)

# Ver los resultados
print(results)
