# Cargar librerías necesarias
library(rpart)
library(dplyr)
library(caret)


create_folds <- function(dataset, k) {
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    indices <- seq_len(nrow(dataset))

    # Shuffles indices with random distribution
    # [4, 1, 9, 2, 7, 3, 10, 5, 8, 6]
    set.seed(123)
    shuffled_indices <- sample(indices)

    # Splits the indices in k equally sized folds
    # [[4, 1, 9, 2, 7], [3, 10, 5, 8, 6]]
    folds <- split(shuffled_indices, cut(seq_along(shuffled_indices), breaks = k, labels = FALSE))

    return(folds)
}


cross_validation <- function(dataset, k) {
    folds <- create_folds(dataset, k)

    # Sets where confusion matrix results are stores for each fold
    accuracies <- c()
    precisions <- c()
    sensitivities <- c()
    specificities <- c()

    for (i in seq_len(k)) {
        # [[Test], [Train], [Train], ..., [Train]]
        # The current fold is the test
        test_indices <- folds[[i]]

        # The remaining folds are for training
        train_indices <- setdiff(seq_len(nrow(dataset)), test_indices)

        # Given test and train indices, access test and train data
        test_data <- dataset[test_indices, ]
        train_data <- dataset[train_indices, ]

        # Trains the decision tree model with train data
        # The first argument specifies that the predicted variable
        # is `inclinacion_peligrosa`, and the remaining are the predictors
        model <- rpart(
            inclinacion_peligrosa ~ .,
            data = train_data,
            method = "class"
        )

        # Tests the obtained model with test data
        predictions <- predict(model, test_data, type = "class")

        # Calculates confusion matrix and extracts the metrics
        confusion_matrix <- confusionMatrix(as.factor(predictions), as.factor(test_data$inclinacion_peligrosa))
        accuracies <- c(accuracies, confusion_matrix$overall["Accuracy"])
        precisions <- c(precisions, confusion_matrix$byClass["Precision"])
        sensitivities <- c(sensitivities, confusion_matrix$byClass["Sensitivity"])
        specificities <- c(specificities, confusion_matrix$byClass["Specificity"])
    }

    # Calculates the mean and standard deviation for each metric
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

# 1. Loads dataset ---------------------------------------------------------
dataset <- read.csv("../../../data/arbolado-mendoza-dataset-train.csv")

print("Dataset columns")
names(dataset)

# 2. Cleans dataset --------------------------------------------------------
# 2.1 Removes irrelevant columns
clean_dataset <- dataset %>% select(-id, -ultima_modificacion, -seccion)


# 2.2 Filter the dataset by keeping only the categories that have more than
# the threshold occurrences
threshold <- 10
clean_dataset <- clean_dataset %>%
    group_by(especie) %>% # Group by the categorical column
    filter(n() >= threshold) %>% # Keep groups with more than 'threshold'
    ungroup()

# 2.3 Undersamples the majority class to ensure a balanced distribution
# Separate the dataset into two groups based on the value of
# 'inclinacion_peligrosa'
majority_class <- clean_dataset %>% filter(inclinacion_peligrosa == 0)
minority_class <- clean_dataset %>% filter(inclinacion_peligrosa == 1)

# Sample from the majority class to match the number of rows in the
# minority class
set.seed(123)
majority_class_sample <- majority_class %>% sample_n(nrow(minority_class))

# Combine the undersampled majority class and the full minority class
clean_dataset <- bind_rows(majority_class_sample, minority_class)

print("Showing summary -----------------------------------------------")
names(clean_dataset)
summary(clean_dataset)


metrics_summary <- cross_validation(clean_dataset, 10)
metrics_summary
