import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Definir rutas relativas estrictas
ruta_base = os.path.dirname(os.path.abspath(__file__))
ruta_datos = os.path.join(ruta_base, "..", "datos", "clima.csv")
ruta_resultados_img = os.path.join(ruta_base, "..", "resultados", "evolucion_temperatura_belfast.png")
ruta_resultados_txt = os.path.join(ruta_base, "..", "resultados", "indicadores_belfast.txt")

# Asegurar que exista la carpeta /resultados
os.makedirs(os.path.dirname(ruta_resultados_img), exist_ok=True)

# 2. Importar el archivo CSV y procesar fechas
df = pd.read_csv(ruta_datos)
df['Fecha'] = pd.to_datetime(df['Fecha'])

# 3. Calcular los indicadores requeridos de Belfast
temp_promedio_max = df['Temperatura_Max'].mean()
temp_promedio_min = df['Temperatura_Min'].mean()
max_absoluta = df['Temperatura_Max'].max()
min_absoluta = df['Temperatura_Min'].min()
promedio_precipitaciones = df['Precipitacion'].mean()

# 4. Guardar los indicadores en un archivo de texto
with open(ruta_resultados_txt, "w", encoding="utf-8") as f:
    f.write("=== INDICADORES CLIMÁTICOS DE BELFAST ===\n")
    f.write(f"Temperatura Máxima Absoluta: {max_absoluta} °C\n")
    f.write(f"Temperatura Mínima Absoluta: {min_absoluta} °C\n")
    f.write(f"Promedio de Temperaturas Máximas: {temp_promedio_max:.2f} °C\n")
    f.write(f"Promedio de Temperaturas Mínimas: {temp_promedio_min:.2f} °C\n")
    f.write(f"Promedio Mensual de Precipitaciones: {promedio_precipitaciones:.2f} mm\n")

# 5. Generar el gráfico de la evolución de la temperatura
plt.figure(figsize=(10, 5))
plt.plot(df['Fecha'], df['Temperatura_Max'], marker='o', color='red', label='Máxima Mensual')
plt.plot(df['Fecha'], df['Temperatura_Min'], marker='s', color='blue', label='Mínima Mensual')

plt.title('Evolución de las Temperaturas en Belfast')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.grid(True, linestyle='--')
plt.legend()

# 6. Guardar automáticamente el gráfico en la carpeta /resultados
plt.savefig(ruta_resultados_img, bbox_inches='tight')
plt.close()

print("¡Procesamiento completo! El gráfico y los indicadores se guardaron en /resultados")
