# Cargar la librería ggplot2
library(ggplot2)

# Leer el archivo CSV
dataset <- read.csv("../../data/arbolado-mendoza-dataset-train.csv")

# Asegurarse de que la variable 'circ_tronco_cm' es numérica
dataset$circ_tronco_cm <- as.numeric(dataset$circ_tronco_cm)

# Crear el histograma de la variable circ_tronco_cm
plot <- ggplot(dataset, aes(x = circ_tronco_cm)) +
    geom_histogram(binwidth = 5, fill = "blue", color = "black", alpha = 0.7) + # Ajusta el binwidth según sea necesario
    labs(
        title = "Histograma de la Circunferencia del Tronco (cm)",
        x = "Circunferencia del Tronco (cm)",
        y = "Frecuencia"
    ) +
    theme_minimal(base_size = 15) + # Mantener fondo blanco y aumentar el tamaño base de la fuente
    theme(
        panel.background = element_rect(fill = "white"), # Fondo del panel blanco
        plot.background = element_rect(fill = "white") # Fondo del gráfico blanco
    )

# Guardar el gráfico como imagen PNG
ggsave("histograma_circ_tronco_cm.png", plot = plot, width = 8, height = 5)
