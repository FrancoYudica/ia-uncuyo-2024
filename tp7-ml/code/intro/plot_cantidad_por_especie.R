# Cargar las librerías necesarias
library(ggplot2)
library(dplyr)

# Leer el archivo CSV
dataset <- read.csv("../../data/arbolado-mendoza-dataset-train.csv")

# Verificar la estructura del conjunto de datos
str(dataset)

# Agrupar y contar la cantidad de elementos por especie
data_summary <- dataset %>%
  group_by(especie) %>%
  summarise(count = n(), .groups = "drop")

# Crear un gráfico de barras
plot <- ggplot(data_summary, aes(x = especie, y = count)) +
  geom_bar(stat = "identity", fill = "blue", color = "black") +  # Usar el conteo directamente
  labs(title = "Cantidad de árboles por especie", 
       x = "Especie", 
       y = "Cantidad de Elementos") +
  theme_minimal() +
  theme(
    panel.background = element_rect(fill = "white"),  # Fondo del panel blanco
    plot.background = element_rect(fill = "white"),  # Fondo del gráfico blanco
    axis.text.x = element_text(angle = 45, hjust = 1)  # Rotar etiquetas del eje x si es necesario
  )

ggsave("cantidad_arboles_por_especie.jpg", plot = plot, width = 10, height = 6)
