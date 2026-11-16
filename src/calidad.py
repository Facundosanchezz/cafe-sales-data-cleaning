
import numpy as np
import pandas as pd


def validar_ventas(df):
    cantidad = df["Quantity"]
    precio = df["Price Per Unit"]
    total = df["Total Spent"]

    cantidades_validas = (
        cantidad.dropna().gt(0).all()
        and cantidad.dropna().mod(1).eq(0).all()
    )

    precios_validos = precio.dropna().gt(0).all()

    completos = df[
        ["Quantity", "Price Per Unit", "Total Spent"]
    ].notna().all(axis=1)

    totales_validos = np.isclose(
        total.loc[completos],
        cantidad.loc[completos] * precio.loc[completos],
        rtol=0,
        atol=0.01
    ).all()

    return {
        "cantidades_validas": cantidades_validas,
        "precios_validos": precios_validos,
        "totales_validos": totales_validos
    }


def resumen_calidad(df):
    columnas_numericas = [
        "Quantity",
        "Price Per Unit",
        "Total Spent"
    ]

    completos = (
        df[columnas_numericas]
        .notna()
        .all(axis=1)
    )

    return {
        "total_transacciones": len(df),
        "transacciones_completas": int(completos.sum()),
        "transacciones_incompletas": int((~completos).sum()),
        "porcentaje_completitud_numerica": round(
            completos.mean() * 100, 2
        ) if len(df) else 0.0,
        "faltantes_por_columna": df.isna().sum().to_dict()
    }
