library(dplyr)

# Reads data set
dataset <- read.csv("../../data/arbolado-mza-dataset.csv")

set.seed(123)

# Calculates the size of the validation data set (20%)
validation_size <- round(0.2 * nrow(dataset))

# Samples indices corresponding to the validation data
# If indices are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Then validation indices could be [1, 8] (20%)
validation_indices <- sample(1:nrow(dataset), validation_size)

# Splits the validation data and the train data
validation_data <- dataset[validation_indices, ]
train_data <- dataset[-validation_indices, ]

# Stores results
write.csv(validation_data, "../../data/arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
write.csv(train_data, "../../data/arbolado-mendoza-dataset-train.csv", row.names = FALSE)


print("Validation and train data generated successfully!\n")


