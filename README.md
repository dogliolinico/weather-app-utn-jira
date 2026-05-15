# App Weather UTN - Belfast 2025 (ID: AWTOE2026)

Solución automatizada y reproducible para el procesamiento, análisis estadístico y visualización de variables meteorológicas de Belfast durante 2025. 

## 📊 Estructura del Repositorio
* `/datos/clima.csv`: Dataset origen con los registros meteorológicos.
* `/scripts/analisis_datos.py`: Script lógico de procesamiento automatizado.
* `/resultados/`: Carpeta con las métricas (`.txt`) y el gráfico (`.png`) exportados.
* `AWTOE2026_Analisis_Climatico.ipynb`: Cuaderno de validación en Google Colab.

## 🚀 Instalación y Ejecución
Para asegurar el funcionamiento de las **rutas relativas**, ejecute en orden desde su terminal:

```bash
pip install pandas matplotlib
cd scripts
python analisis_datos.py
```

## 👥 Gobernanza y Trazabilidad (Jira)
El desarrollo simula un flujo ágil integrado mediante commits trazables:
* **Hugo (`AWTOE2026-1`):** Inicialización de arquitectura y gobernanza del proyecto.
* **Paco (`AWTOE2026-3`):** Desarrollo del script funcional y gráficos en rama `feature`.
* **Luis (`AWTOE2026-2`):** Control de calidad, revisión por pares en Pull Request y Merge a `main`.
