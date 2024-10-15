# Cargar la librería ggplot2 (si es necesaria para otros gráficos futuros)
library(ggplot2)

# Leer el archivo CSV
dataset <- read.csv("../../../data/arbolado-mendoza-dataset-train.csv")

# Verificar la estructura del conjunto de datos
str(dataset)

# Asegurarse de que la variable 'circ_tronco_cm' sea numérica
dataset$circ_tronco_cm <- as.numeric(dataset$circ_tronco_cm)

# Categorizar la variable 'circ_tronco_cm' en la nueva variable 'circ_tronco_cm_cat'
dataset$circ_tronco_cm_cat <- cut(
    dataset$circ_tronco_cm,
    breaks = c(0, 75, 150, 225, Inf), # Definir los intervalos
    labels = c("bajo", "medio", "alto", "muy alto"), # Definir las etiquetas
    right = FALSE # Intervalos cerrados por la izquierda (incluye el límite inferior)
)

# Verificar los resultados
head(dataset)

# Contar cuántos árboles caen en cada categoría
table(dataset$circ_tronco_cm_cat)

# Guardar el dataset actualizado en un nuevo archivo CSV (opcional)
write.csv(dataset, "arbolado-mendoza-dataset-circ_tronco_cm-train.csv", row.names = FALSE)

# Crear un gráfico de barras para visualizar la distribución de 'circ_tronco_cm_cat'
plot <- ggplot(dataset, aes(x = circ_tronco_cm_cat)) +
    geom_bar(fill = "lightblue", color = "black") + # Crear barras con colores personalizados
    labs(
        title = "Distribución de las Categorías de circ_tronco_cm",
        x = "Categoría de circ_tronco_cm",
        y = "Frecuencia"
    ) +
    theme_minimal(base_size = 15) + # Mantener un fondo blanco con un tamaño de fuente mayor
    theme(
        panel.background = element_rect(fill = "white"), # Fondo del panel blanco
        plot.background = element_rect(fill = "white"), # Fondo del gráfico blanco
        axis.text.x = element_text(angle = 0, hjust = 0.5) # Etiquetas del eje x centradas
    )

ggsave("distribucion_circ_tronco_cm_cat.png", plot = plot, width = 8, height = 5)
