import pandas as pd
import os

carpeta = "datos"
todos_los_datos = []

for archivo in os.listdir(carpeta):
    if archivo.endswith(".xlsx"):
        ruta = os.path.join(carpeta, archivo)
        df = pd.read_excel(ruta)
        df["Hotel"] = archivo.replace(".xlsx", "")
        todos_los_datos.append(df)

consolidado = pd.concat(todos_los_datos, ignore_index=True)

# Mostrar datos consolidados
print("=== DATOS POR HOTEL ===")
print(consolidado.to_string(index=False))

# Resumen por mes
resumen = consolidado.groupby("Mes").agg(
    Ingresos_totales=("Ingresos", "sum"),
    Habitaciones_vendidas_total=("Habitaciones_vendidas", "sum")
).reset_index()

print("\n=== RESUMEN POR MES ===")
print(resumen.to_string(index=False))

# Guardar todo en un Excel con dos hojas
with pd.ExcelWriter("reporte_consolidado.xlsx") as writer:
    consolidado.to_excel(writer, sheet_name="Por hotel", index=False)
    resumen.to_excel(writer, sheet_name="Resumen", index=False)

print("\nReporte guardado en reporte_consolidado.xlsx")