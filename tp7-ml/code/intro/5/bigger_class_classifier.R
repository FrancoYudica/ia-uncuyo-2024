library(dplyr)
library(caret)

biggerclass_classifier <- function(dataset, target_column) {
    # Step 1: Identify the majority class in the target column
    bigger_class <- dataset %>%
        count(!!sym(target_column)) %>% # Count occurrences of each class
        arrange(desc(n)) %>% # Sort by count in descending order
        slice(1) %>% # Select the most frequent class
        pull(!!sym(target_column)) # Extract the class value

    # Step 2: Create a new column 'prediction_class' and assign the bigger class to all rows
    dataset$prediction_class <- bigger_class

    return(dataset) # Return the updated dataset with the prediction_class column
}

dataset <- read.csv("../../../data/arbolado-mendoza-dataset-train.csv")
dataset_with_predictions <- biggerclass_classifier(dataset, "inclinacion_peligrosa")

# Calcular las métricas utilizando dplyr
results <- dataset_with_predictions %>% summarise(
    True_Positives = sum(inclinacion_peligrosa == 1 & prediction_class == 1), # Árboles con inclinación peligrosa correctamente predichos (TP)
    True_Negatives = sum(inclinacion_peligrosa == 0 & prediction_class == 0), # Árboles sin inclinación peligrosa correctamente predichos (TN)
    False_Positives = sum(inclinacion_peligrosa == 0 & prediction_class == 1), # Árboles sin inclinación peligrosa predichos incorrectamente como peligrosos (FP)
    False_Negatives = sum(inclinacion_peligrosa == 1 & prediction_class == 0) # Árboles con inclinación peligrosa predichos incorrectamente como no peligrosos (FN)
)

# Ver los resultados
print(results)
