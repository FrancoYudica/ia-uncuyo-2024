# Cargar las librerías necesarias
library(ggplot2)
library(dplyr)

# Leer el archivo CSV
dataset <- read.csv("../../data/arbolado-mendoza-dataset-train.csv")

# Verificar la estructura del conjunto de datos
str(dataset)

# Agrupar y contar la cantidad total de árboles y las inclinaciones peligrosas por especie
data_summary <- dataset %>%
  group_by(especie) %>%
  summarise(
    total_trees = n(),  # Total de árboles por especie
    dangerous_inclination = sum(inclinacion_peligrosa == 1),  # Cantidad de inclinaciones peligrosas
    .groups = "drop"
  )

# Calcular la proporción de inclinaciones peligrosas
data_summary <- data_summary %>%
  mutate(proporcion = dangerous_inclination / total_trees)

# Crear un gráfico de barras
plot <- ggplot(data_summary, aes(x = especie, y = proporcion)) +
  geom_bar(stat = "identity", fill = "blue", color = "black") +  # Usar el conteo directamente
  labs(title = "Proporción de Inclinaciones Peligrosas por Especie", 
       x = "Especie", 
       y = "Proporción de Inclinaciones Peligrosas") +
  theme_minimal() +
  theme(
    panel.background = element_rect(fill = "white"),  # Fondo del panel blanco
    plot.background = element_rect(fill = "white"),  # Fondo del gráfico blanco
    axis.text.x = element_text(angle = 45, hjust = 1)  # Rotar etiquetas del eje x si es necesario
  )

ggsave("proporcion_inclinaciones_por_especie.jpg", plot = plot, width = 10, height = 6)
