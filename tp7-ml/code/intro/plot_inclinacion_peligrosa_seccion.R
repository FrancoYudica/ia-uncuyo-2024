# Cargar la librería ggplot2
library(ggplot2)
library(dplyr)  # Para manipulación de datos

# Leer el archivo CSV
dataset <- read.csv("../../data/arbolado-mendoza-dataset-train.csv")

# Verificar la estructura del conjunto de datos
str(dataset)
print(names(dataset))
# Asegúrate de que la variable inclinación_peligrosa es un factor
dataset$inclinacion_peligrosa <- as.factor(dataset$inclinacion_peligrosa)

# Filtrar los datos para quedarnos solo con inclinaciones peligrosas = 1
dataset_filtered <- dataset %>%
  filter(inclinacion_peligrosa == 1)

# Agrupar y contar las inclinaciones peligrosas por seccion
data_summary <- dataset_filtered %>%
  group_by(nombre_seccion, inclinacion_peligrosa) %>%
  summarise(count = n(), .groups = "drop")

# Crear un gráfico de barras
plot <- ggplot(data_summary, aes(x = nombre_seccion, y = count, fill = inclinacion_peligrosa)) +
  geom_bar(stat = "identity", position = "dodge") +  # Usar "dodge" para mostrar barras lado a lado
  labs(title = "Inclinaciones Peligrosas por Sección", 
       x = "Especie", 
       y = "Cantidad de Inclinaciones Peligrosas por seccion") +
  theme_minimal() +
  theme(
    panel.background = element_rect(fill = "white"),  # Fondo del panel blanco
    plot.background = element_rect(fill = "white"),  # Fondo del gráfico blanco
    axis.text.x = element_text(angle = 45, hjust = 1)  # Rotar etiquetas del eje x si es necesario
  )

ggsave("inclinacion_peligrosa_seccion.jpg", plot = plot, width = 10, height = 6)
