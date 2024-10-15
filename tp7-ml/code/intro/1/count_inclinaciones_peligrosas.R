# Cargar la librería dplyr
library(dplyr)

# Leer el archivo CSV
dataset <- read.csv("../../data/arbolado-mendoza-dataset-train.csv")

# Verificar la estructura del conjunto de datos
str(dataset)

# Contar la cantidad de inclinaciones peligrosas (1) y no peligrosas (0)
data_summary <- dataset %>%
  group_by(inclinacion_peligrosa) %>%
  summarise(count = n(), .groups = "drop")

# Cambiar los valores de inclinacion_peligrosa a etiquetas más comprensibles
data_summary$inclinacion_peligrosa <- ifelse(data_summary$inclinacion_peligrosa == 1, "Peligrosa", "No Peligrosa")

# Mostrar el resultado
print(data_summary)
