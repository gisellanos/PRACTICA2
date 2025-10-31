
#1
import csv
import json
from datetime import datetime
from collections import defaultdict
import os
#2
carpeta_script = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_entrada = os.path.join(carpeta_script, "actividad_2.csv")
carpeta_salida = os.path.join(carpeta_script, "salida")
os.makedirs(carpeta_salida, exist_ok=True)
#3
conteo_por_dia_semana = defaultdict(int)
conteo_por_campeon = defaultdict(int)
conteo_fines_de_semana = defaultdict(int)
entrenamientos_por_dia_y_campeon = defaultdict(lambda: defaultdict(int))
#4
fecha_minima = None
fecha_maxima = None
total_registros = 0
#5
with open(ruta_archivo_entrada, newline='', encoding='utf-8') as archivo:
    lector_csv = csv.DictReader(archivo)
    for fila in lector_csv:
        total_registros += 1
#6
        fecha_entrenamiento = datetime.strptime(fila["timestamp"], "%Y-%m-%d %H:%M")
        dia_semana = fecha_entrenamiento.strftime("%A")
        nombre_campeon = fila["campeon"]

        if fecha_minima is None or fecha_entrenamiento < fecha_minima:
            fecha_minima = fecha_entrenamiento
        if fecha_maxima is None or fecha_entrenamiento > fecha_maxima:
            fecha_maxima = fecha_entrenamiento

        conteo_por_dia_semana[dia_semana] += 1
        conteo_por_campeon[nombre_campeon] += 1
        entrenamientos_por_dia_y_campeon[dia_semana][nombre_campeon] += 1

        if dia_semana in ["Saturday", "Sunday"]:
            conteo_fines_de_semana[nombre_campeon] += 1
#7
dias_entre_entrenamientos = (fecha_maxima - fecha_minima).days if fecha_minima and fecha_maxima else 0

maximo_numero_sesiones = max(conteo_por_dia_semana.values()) if conteo_por_dia_semana else 0
dias_con_mas_sesiones = [dia for dia, cantidad in conteo_por_dia_semana.items() if cantidad == maximo_numero_sesiones]

campeon_con_mas_entrenamientos = max(conteo_por_campeon, key=conteo_por_campeon.get) if conteo_por_campeon else "Ninguno"
campeon_con_mas_fines_de_semana = max(conteo_fines_de_semana, key=conteo_fines_de_semana.get) if conteo_fines_de_semana else "Ninguno"

cantidad_semanas = (dias_entre_entrenamientos / 7) or 1
promedio_por_dia = {dia: round(cant / cantidad_semanas, 2) for dia, cant in conteo_por_dia_semana.items()}
#8
ruta_csv_salida = os.path.join(carpeta_salida, "entrenamientos_por_campeon.csv")
ranking_campeones = sorted(conteo_por_campeon.items(), key=lambda x: x[1], reverse=True)

with open(ruta_csv_salida, "w", newline='', encoding="utf-8") as salida_csv:
    escritor_csv = csv.writer(salida_csv)
    escritor_csv.writerow(["campeon", "cantidad_entrenamientos"])
    for campeon, cantidad in ranking_campeones:
        escritor_csv.writerow([campeon, cantidad])

entrenamientos_por_dia_y_campeon = {dia: dict(campeones) for dia, campeones in entrenamientos_por_dia_y_campeon.items()}
#9
resumen = {
    "total_registros": total_registros,
    "dias_entrenamiento_primero_y_ultimo": dias_entre_entrenamientos,
    "dias_mas_sesiones": dias_con_mas_sesiones,
    "campeon_mas_entreno": campeon_con_mas_entrenamientos,
    "campeon_fines_de_semana": campeon_con_mas_fines_de_semana,
    "promedio_por_dia": promedio_por_dia,
    "entrenamientos_por_dia": entrenamientos_por_dia_y_campeon
}

ruta_json_salida = os.path.join(carpeta_salida, "resumen.json")
with open(ruta_json_salida, "w", encoding="utf-8") as salida_json:
    json.dump(resumen, salida_json, indent=4, ensure_ascii=False)
#10
print("RESULTADOS")
print("-" * 50)
print(f"Total de registros: {total_registros}")
print(f"Días con más sesiones: {dias_con_mas_sesiones} ({maximo_numero_sesiones} sesiones)")
print(f"Días entre primer y último entrenamiento: {dias_entre_entrenamientos}")
print(f"Campeón que más entrenó: {campeon_con_mas_entrenamientos}")
print(f"Promedio de entrenamientos por día: {promedio_por_dia}")
print(f"Campeón que más entrena los fines de semana: {campeon_con_mas_fines_de_semana}")
print("\nArchivos generados en la carpeta 'salida':")
print(" - entrenamientos_por_campeon.csv")
print(" - resumen.json")