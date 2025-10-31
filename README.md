

 ¿Qué hace este programa?

A partir del archivo `actividad_2.csv`, el programa procesa cada registro de entrenamiento y obtiene información como:

- 📅 El total de entrenamientos registrados.  
- 📈 Qué días de la semana se entrenó más.  
- 🏆 Qué campeón realizó más sesiones de entrenamiento.  
- 🕒 Cuántos días pasaron entre el primer y último entrenamiento.  
- 📊 El promedio semanal de entrenamientos por día.  
- 🏖️ Qué campeón entrena más los fines de semana.  

Los resultados se muestran por pantalla y se guardan automáticamente en dos archivos dentro de la carpeta `salida`:

- `entrenamientos_por_campeon.csv` → ranking con cantidad de entrenamientos por campeón.  
- `resumen.json` → resumen general con datos clave del análisis.

---

## ⚙️ Estructura del código

El programa está dividido en secciones bien definidas para una lectura clara y ordenada:

### Importación de librerías
Se utilizan las librerías estándar de Python:
- `csv` y `json` → para leer y escribir archivos.
- `datetime` → para procesar fechas y horas.
- `collections.defaultdict` → para contar datos fácilmente.
- `os` → para manejar rutas de archivos y carpetas.

### Definición de rutas
El programa detecta automáticamente la carpeta donde se ejecuta y crea una carpeta de salida llamada **`salida`** si no existe.  
Esto asegura que los archivos generados se guarden correctamente junto al script.

###  Variables y estructuras de datos
Se crean varios diccionarios para almacenar y contar información:
- `conteo_por_dia_semana`: número de entrenamientos por día.  
- `conteo_por_campeon`: entrenamientos totales de cada campeón.  
- `conteo_fines_de_semana`: entrenamientos por campeón en sábados y domingos.  
- `entrenamientos_por_dia_y_campeon`: combinaciones de día y campeón.  

También se guardan las fechas mínima y máxima para calcular el rango total analizado.

### Lectura y procesamiento del CSV
El programa recorre cada fila del archivo CSV (`actividad_2.csv`) y obtiene:
- La fecha y hora (`timestamp`).
- El nombre del campeón (`campeon`).

A partir de estos datos, se actualizan los conteos y se registran las fechas inicial y final.

###  Cálculos y estadísticas
Una vez procesados todos los datos, el programa calcula:
- Días entre el primer y último entrenamiento.  
- Día(s) de la semana con más sesiones.  
- Campeón con más entrenamientos.  
- Campeón más activo los fines de semana.  
- Promedio semanal de entrenamientos por día.

Estos datos permiten tener una visión clara del rendimiento y la frecuencia de las actividades.

### Generación de archivos de salida
Se crean dos archivos automáticos en la carpeta `salida`:
- **`entrenamientos_por_campeon.csv`** → ranking de campeones ordenado por cantidad de sesiones.  
- **`resumen.json`** → datos generales y estadísticas del análisis en formato legible.

###  Salida en consola
Por último, el programa muestra los resultados más importantes directamente en pantalla, como:
- Total de registros procesados.  
- Día con más sesiones.  
- Campeón con más entrenamientos.  
- Promedio de entrenamientos por día.  
- Campeón con más actividad los fines de semana.
