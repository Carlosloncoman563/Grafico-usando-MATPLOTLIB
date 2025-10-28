#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TCID50/mL vs Días — Gráfico interactivo con auto-instalación y fallback de backend
-----------------------------------------------------------------------------------
- Auto-instala matplotlib (obligatorio) y pandas (opcional) si faltan.
- Importa matplotlib.pyplot de forma robusta (con fallback a backend 'Agg').
- Pide número de series, nombre, días (X) y valores (Y).
- Valida entradas, permite escala log10 en Y, y guarda PNG/CSV (si pandas).
- Ideal para Spyder.

Autor: Tú :)
"""

import sys
import subprocess
import importlib
from typing import List, Tuple

# ========================= Auto-instalación =========================
def ensure(package: str):
    """Asegura que 'package' esté importable. Si no, lo instala con pip y lo retorna."""
    try:
        return __import__(package)
    except ImportError:
        print(f"[Instalación] No se encontró '{package}'. Instalando…")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", package])
        except subprocess.CalledProcessError as e:
            print(f"✗ No se pudo instalar '{package}'. Error: {e}")
            print("   Instálalo manualmente y vuelve a ejecutar el script.")
            sys.exit(1)
        return __import__(package)

# matplotlib es obligatorio
matplotlib = ensure("matplotlib")

# Carga robusta de pyplot (evita AttributeError por lazy import/backends)
try:
    plt = importlib.import_module("matplotlib.pyplot")
except Exception as e:
    # Intento con backend no interactivo (útil si falta Qt en el entorno)
    try:
        matplotlib.use("Agg")  # Debe ser antes de importar pyplot
        plt = importlib.import_module("matplotlib.pyplot")
        print("ℹ No se pudo usar un backend interactivo. Usando 'Agg' (sin ventana). Se guardará PNG en disco.")
    except Exception as e2:
        print("✗ No se pudo cargar 'matplotlib.pyplot'. Si estás en Spyder/GUI, instala un backend Qt:")
        print("   pip install PyQt5   (o)   pip install PySide6")
        sys.exit(1)

# pandas es opcional (solo para CSV)
try:
    pd = ensure("pandas")
    HAS_PANDAS = True
except SystemExit:
    raise
except Exception:
    HAS_PANDAS = False

# ========================= Utilidades I/O =========================
def parse_numeric_list(texto: str) -> List[float]:
    """Convierte '1, 2.5, 3e4' -> [1.0, 2.5, 30000.0]. Admite espacios y notación científica."""
    piezas = [p.strip() for p in texto.split(",") if p.strip() != ""]
    vals = []
    for p in piezas:
        try:
            vals.append(float(p))
        except ValueError:
            raise ValueError(f"Valor no numérico: '{p}'. Usa puntos decimales y separa por comas.")
    if not vals:
        raise ValueError("Lista vacía. Ingresa al menos un valor.")
    return vals

def pedir_lista_numerica(prompt: str) -> List[float]:
    while True:
        try:
            txt = input(prompt).strip()
            return parse_numeric_list(txt)
        except Exception as e:
            print(f"✗ {e}\nIntenta nuevamente.\n")

def pedir_si_no(prompt: str, default: bool = True) -> bool:
    suf = "[S/n]" if default else "[s/N]"
    while True:
        ans = input(f"{prompt} {suf}: ").strip().lower()
        if ans == "" and default:
            return True
        if ans == "" and not default:
            return False
        if ans in ("s", "si", "sí", "y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Responde con 's' o 'n' por favor.")

def pedir_entero_positivo(prompt: str, minimo: int = 1) -> int:
    while True:
        ans = input(prompt).strip()
        try:
            n = int(ans)
            if n < minimo:
                print(f"Debe ser un entero ≥ {minimo}.")
                continue
            return n
        except ValueError:
            print("Ingresa un número entero válido.")

# ========================= Recolección de datos =========================
def recolectar_series() -> List[Tuple[str, List[float], List[float]]]:
    print("\n=== Configuración de series ===")
    n_series = pedir_entero_positivo("¿Cuántas series deseas graficar? (p. ej., 1, 2, 3...): ")

    series = []
    i = 1
    while i <= n_series:
        print(f"\n— Serie {i} —")
        nombre = input("Nombre de la serie (para la leyenda): ").strip() or f"Serie {i}"
        x = pedir_lista_numerica("Días (X), separados por comas (ej: 0,3,7,10): ")
        y = pedir_lista_numerica("TCID50/mL (Y), separados por comas (ej: 1e5,9.7e4,2.1e6,8.5e5): ")

        if len(x) != len(y):
            print(f"✗ Las longitudes no coinciden (X: {len(x)}, Y: {len(y)}). Vuelve a ingresar esta serie.")
            continue  # Repite misma serie

        if any(v <= 0 for v in y):
            print("✗ Todos los valores de TCID50/mL deben ser > 0 (especialmente si usarás escala log).")
            continue

        series.append((nombre, x, y))
        i += 1

    return series

# ========================= Lógica principal =========================
def main():
    print("\n====================================")
    print("  TCID50/mL vs Días — Generador de gráfico")
    print("====================================\n")

    titulo = input("Título del gráfico (opcional): ").strip()
    usar_log = pedir_si_no("¿Usar escala log10 en el eje Y?", default=True)
    marcar_puntos = pedir_si_no("¿Dibujar puntos (marcadores)?", default=True)
    unir_lineas = pedir_si_no("¿Unir los puntos con líneas?", default=True)
    mostrar_grid = pedir_si_no("¿Mostrar grilla?", default=True)

    series = recolectar_series()

    # Construcción del gráfico
    fig, ax = plt.subplots(figsize=(8, 5))
    for nombre, x, y in series:
        if unir_lineas and marcar_puntos:
            ax.plot(x, y, marker="o", linewidth=1.5, label=nombre)
        elif unir_lineas:
            ax.plot(x, y, linewidth=1.8, label=nombre)
        elif marcar_puntos:
            ax.plot(x, y, marker="o", linestyle="None", label=nombre)
        else:
            ax.plot(x, y, linestyle="None", label=nombre)

    ax.set_xlabel("Días")
    ax.set_ylabel("TCID50/mL")
    if titulo:
        ax.set_title(titulo)

    if usar_log:
        try:
            ax.set_yscale("log")
        except ValueError:
            print("Advertencia: No se pudo aplicar escala log; revisa que todos los Y sean > 0.")

    if mostrar_grid:
        ax.grid(True, which="both", linestyle="--", alpha=0.4)

    ax.legend(title="Series", loc="best")
    plt.tight_layout()

    # Guardado opcional
    if pedir_si_no("¿Guardar gráfico como PNG?", default=True):
        fname = input("Nombre de archivo PNG (sin extensión, ej: grafico_tcid50): ").strip() or "grafico_tcid50"
        salida_png = f"{fname}.png"
        fig.savefig(salida_png, dpi=300, bbox_inches="tight")
        print(f"✔ Gráfico guardado en: {salida_png}")

    # Exportar CSV opcional (si hay pandas)
    if HAS_PANDAS and pedir_si_no("¿Exportar los datos a CSV?", default=False):
        filas = []
        for nombre, x, y in series:
            for xi, yi in zip(x, y):
                filas.append({"Serie": nombre, "Dia": xi, "TCID50_por_mL": yi})
        df = pd.DataFrame(filas)
        fname_csv = input("Nombre de archivo CSV (sin extensión, ej: datos_tcid50): ").strip() or "datos_tcid50"
        salida_csv = f"{fname_csv}.csv"
        df.to_csv(salida_csv, index=False)
        print(f"✔ Datos exportados a: {salida_csv}")
    elif not HAS_PANDAS:
        print("ℹ 'pandas' no está disponible. Si quieres CSV: pip install pandas")

    print("\nMostrando gráfico…")
    try:
        plt.show()
    except Exception:
        # Si estamos en 'Agg', no hay ventana; ya guardamos PNG si elegiste hacerlo.
        pass

# ========================= Punto de entrada =========================
if __name__ == "__main__":
    main()
