library(rpart)
library(caret)
library(readr)
library(dplyr)
library(ranger)
library(pROC)


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


# 1. LOADS DATASETS ------------------------------------------------------------
raw_dataset_train <- read.csv(
    "../../data/arbolado-mendoza-dataset-train.csv"
)
raw_dataset_validation <- read.csv(
    "../../data/arbolado-mendoza-dataset-validation.csv"
)

raw_dataset_test <- read.csv(
    "../../data/arbolado-mza-dataset-test.csv"
)


# 2. CLEANS DATASETS -----------------------------------------------------------
dataset_train <- raw_dataset_train %>%
    select(-id, -ultima_modificacion, -nombre_seccion)
dataset_validation <- raw_dataset_validation

# 3. UNDERSAMPLING -------------------------------------------------------------
majority_class <- dataset_train %>% filter(inclinacion_peligrosa == 0)
minority_class <- dataset_train %>% filter(inclinacion_peligrosa == 1)
print(paste("Majority class row count:", nrow(majority_class)))
print(paste("Minority class row count:", nrow(minority_class)))

# Ensure equal counts by undersampling the majority class
majority_undersampled <- majority_class %>% sample_n(nrow(minority_class))

# Combine undersampled majority with minority class
merged_dataset <- rbind(minority_class, majority_undersampled)
print(paste("Merged dataset row count:", nrow(merged_dataset)))

# 4. TRAINS THE MODEL WITH RANDOM FOREST ---------------------------------------
# The predicted attribute is "inclinacion_peligrosa" and the remaining "." are
# the predictors, used to predict "inclinacion_peligrosa"
rf_model <- ranger(
    inclinacion_peligrosa ~ .,
    data = merged_dataset
)

# 5. EVALUATES MODEL WITH VALIDATION TEST --------------------------------------
print("Evaluating model over validation dataset:")
show_confusion_matrix(rf_model, dataset_validation)
show_auc(rf_model, dataset_validation)

# 6. PREDICT ON TEST SET WITH THE GENERATED MODEL ------------------------------
predictions <- predict(rf_model, raw_dataset_test)$predictions

# 7. Create submission file. This map the ID of the ID to the prediction -------
submission <- data.frame(
    id = raw_dataset_test$id,
    inclinacion_peligrosa = predictions
)
write_csv(submission, "arbolado-mza-dataset-submission.csv")
