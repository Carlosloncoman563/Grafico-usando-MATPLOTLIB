Este script en Python permite crear de forma interactiva un gráfico que muestra la evolución de títulos virales expresados como TCID₅₀/mL a lo largo del tiempo (en días).
Está diseñado para ser utilizado en laboratorios de virología o microbiología que requieran visualizar resultados de infectividad o comparar diferentes tratamientos, condiciones experimentales o cepas en cultivo celular.
El programa guía al usuario paso a paso mediante una interfaz de consola, solicitando:
El número de series o tratamientos a graficar.
El nombre de cada serie (que aparecerá en la leyenda).
Los valores de tiempo (días) para el eje X.
Los valores de TCID₅₀/mL para el eje Y (pueden incluir notación científica, e.g., 1e5).
Opciones de formato del gráfico:
Escala lineal o logarítmica en Y (log10, ideal para datos TCID₅₀).
Inclusión de puntos, líneas o ambos.
Activar o no la grilla.
Posibilidad de guardar el gráfico en formato PNG con resolución de 300 dpi.
Exportar los datos ingresados a CSV (si pandas está disponible).
Además, el script incluye un sistema de auto-instalación automática de dependencias, asegurando que pueda ejecutarse incluso en entornos limpios o recién configurados.
