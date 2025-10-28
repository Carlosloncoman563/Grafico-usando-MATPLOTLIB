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
🧬 Script: Generador interactivo de gráficos TCID₅₀/mL vs Días
Este script permite graficar de forma interactiva los valores de infectividad expresados como TCID₅₀/mL a lo largo del tiempo (en días), comparando distintos tratamientos o condiciones experimentales.
⚙️ Requisitos previos
El script puede instalar sus dependencias automáticamente, pero si prefieres instalarlas tú mismo, ejecuta en tu terminal o consola de Spyder:
pip install matplotlib pandas
✅ Python 3.8 o superior es recomendado.
💻 Funciona en entornos: Spyder, VSCode, Jupyter Notebook o terminal.
🚀 Instrucciones de uso
1. Ejecutar el script
Abre el script en Spyder o en cualquier entorno Python y ejecútalo (F5 o python tcid50_interactivo.py).
El programa mostrará una serie de preguntas interactivas en la consola.
2. Ingreso de datos
Durante la ejecución, el script solicitará información paso a paso:
Título del gráfico (opcional).
Tipo de escala (lineal o logarítmica en el eje Y).
Si se desean puntos, líneas, y grilla.
Número de series a graficar (por ejemplo, distintos tratamientos o replicados).
Para cada serie:
Nombre de la serie (para la leyenda).
Lista de días separados por comas (ejemplo: 0,3,7,10).
Lista de valores de TCID₅₀/mL separados por comas (ejemplo: 1e3,9.7e3,2.1e4,8.5e4).
⚠️ Importante:
Usa punto decimal (1.5e5, no coma decimal).
La cantidad de puntos en X e Y debe ser la misma.
Todos los valores de Y deben ser positivos si se usará escala logarítmica.
3. Generación del gráfico
El script:
Crea el gráfico de TCID₅₀/mL vs Días con etiquetas, título y leyenda.
Aplica escala log₁₀ si se selecciona.
Muestra el gráfico directamente o lo guarda como archivo de imagen.
Ejemplo visual:
(imagen referencial, no incluida)
4. Guardar resultados
Al final, el programa pregunta si deseas:
Guardar el gráfico en formato PNG (300 dpi).
Exportar los datos ingresados a un archivo CSV (requiere pandas).
Los archivos se guardan en el mismo directorio donde se ejecuta el script.
🧩 Dependencias y bibliotecas utilizadas
Paquete	Función principal
matplotlib	Generación y personalización del gráfico.
pandas	Exportación opcional de los datos a formato CSV.
importlib, subprocess, sys	Instalación automática de dependencias.
typing	Tipado de datos (para legibilidad y documentación).
🧠 Consejos de uso
Si usas Spyder, verifica que el backend gráfico sea Automatic o Qt5 en:
Tools → Preferences → IPython Console → Graphics.
Si aparece un mensaje de error del tipo “no display name or backend”, instala:
pip install PyQt5
Para datasets grandes o repetitivos, puedes adaptar el script para leer los valores desde un archivo .csv en lugar de ingresarlos manualmente.
📘 Créditos
Autor:
Carlos Loncoman Pardo — Universidad Austral de Chile
Laboratorio: VirionLab, Instituto de Bioquímica y Microbiología
Descripción:
Script educativo y práctico para visualizar curvas de infectividad viral (TCID₅₀/mL) en el tiempo, aplicable en estudios de virología experimental, cultivo celular y bioensayos antivirales.
