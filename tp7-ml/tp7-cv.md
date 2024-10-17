Código de las funciones `create_folds` y `cross_validation`

```r
create_folds <- function(dataset, k) {
indices <- seq_len(nrow(dataset))

    # Shuffles indices with random distribution
    shuffled_indices <- sample(indices)

    # Splits the indices in k equally sized folds
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
```

Tabla con los resultados:
| Metric | Mean | Standard Deviation |
|----------------|------------|--------------------|
| Accuracy | 0.6740092 | 0.02386155 |
| Precision | 0.662479 | 0.02869295 |
| Sensitivity | 0.7096807 | 0.05152218 |
| Specificity | 0.6387386 | 0.03523508 |
