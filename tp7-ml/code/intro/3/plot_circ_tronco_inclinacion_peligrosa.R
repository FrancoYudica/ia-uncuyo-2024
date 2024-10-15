# Grafica dos histogramas, uno que solo considera a las circunferencias de arboles
# peligrosos y otro histograma con la circunferencia de los arboles no peligrosos

# Cargar la librería ggplot2
library(ggplot2)

# Leer el archivo CSV
dataset <- read.csv("../../data/arbolado-mendoza-dataset-train.csv")

# Verificar la estructura del conjunto de datos
str(dataset)

# Asegurarse de que las variables 'circ_tronco_cm' y 'inclinacion_peligrosa' sean numéricas
dataset$circ_tronco_cm <- as.numeric(dataset$circ_tronco_cm)
dataset$inclinacion_peligrosa <- as.numeric(dataset$inclinacion_peligrosa)

# Filtrar los datos para inclinación peligrosa (1) y no peligrosa (0)
data_peligrosa <- subset(dataset, inclinacion_peligrosa == 1)
data_no_peligrosa <- subset(dataset, inclinacion_peligrosa == 0)

# Crear el histograma para inclinación peligrosa
plot_peligrosa <- ggplot(data_peligrosa, aes(x = circ_tronco_cm)) +
    geom_histogram(binwidth = 5, fill = "red", color = "black", alpha = 0.7) +
    labs(
        title = "Histograma de circ_tronco_cm (Inclinación Peligrosa)",
        x = "circ_tronco_cm",
        y = "Frecuencia"
    ) +
    theme_minimal(base_size = 15) +
    theme(
        panel.background = element_rect(fill = "white"),
        plot.background = element_rect(fill = "white")
    )

# Crear el histograma para inclinación no peligrosa
plot_no_peligrosa <- ggplot(data_no_peligrosa, aes(x = circ_tronco_cm)) +
    geom_histogram(binwidth = 5, fill = "blue", color = "black", alpha = 0.7) +
    labs(
        title = "Histograma de circ_tronco_cm (Inclinación No Peligrosa)",
        x = "circ_tronco_cm",
        y = "Frecuencia"
    ) +
    theme_minimal(base_size = 15) +
    theme(
        panel.background = element_rect(fill = "white"),
        plot.background = element_rect(fill = "white")
    )

# Guardar los gráficos como imágenes PNG
ggsave("histograma_circ_tronco_cm_peligrosa.png", plot = plot_peligrosa, width = 8, height = 5)
ggsave("histograma_circ_tronco_cm_no_peligrosa.png", plot = plot_no_peligrosa, width = 8, height = 5)
