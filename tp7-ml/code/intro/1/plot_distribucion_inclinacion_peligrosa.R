# Cargar las librerías necesarias
library(ggplot2)
library(dplyr)

# Leer el archivo CSV
dataset <- read.csv("../../data/arbolado-mendoza-dataset-train.csv")

# Verificar la estructura del conjunto de datos
str(dataset)

# Agrupar y contar la cantidad de inclinaciones peligrosas
data_summary <- dataset %>%
  group_by(inclinacion_peligrosa) %>%
  summarise(count = n(), .groups = "drop")

# Cambiar los valores de inclinacion_peligrosa a etiquetas más comprensibles
data_summary$inclinacion_peligrosa <- ifelse(data_summary$inclinacion_peligrosa == 1, "Peligrosa", "No Peligrosa")

# Calcular proporciones para el gráfico de torta
data_summary <- data_summary %>%
  mutate(fraction = count / sum(count), 
         ymax = cumsum(fraction), 
         ymin = c(0, head(ymax, n=-1)))

# Crear el gráfico de torta
plot <- ggplot(data_summary, aes(ymax = ymax, ymin = ymin, xmax = 4, xmin = 3, fill = inclinacion_peligrosa)) +
  geom_rect() +
  coord_polar(theta = "y") +  # Cambiar a coordenadas polares
  labs(title = "Distribución de la Variable Inclinación Peligrosa", 
       fill = "Inclinación Peligrosa") +
  theme_void(base_size = 15) +  # Tema vacío y aumentar el tamaño base de la fuente
  theme(
    plot.background = element_rect(fill = "white"),  # Fondo del gráfico blanco
    legend.position = "right"  # Posición de la leyenda
  )

# Guardar el gráfico como imagen PNG
ggsave("distribucion_inclinacion_peligrosa_torta.png", plot = plot, width = 8, height = 5)

