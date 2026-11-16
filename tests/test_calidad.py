
import pandas as pd
import numpy as np

from src.calidad import validar_ventas, resumen_calidad


def test_venta_correcta():
    df = pd.DataFrame({
        "Quantity": [2],
        "Price Per Unit": [3.0],
        "Total Spent": [6.0]
    })

    resultado = validar_ventas(df)

    assert all(resultado.values())


def test_cantidad_negativa():
    df = pd.DataFrame({
        "Quantity": [-2],
        "Price Per Unit": [3.0],
        "Total Spent": [-6.0]
    })

    resultado = validar_ventas(df)

    assert not resultado["cantidades_validas"]
    assert resultado["precios_validos"]


def test_precio_negativo():
    df = pd.DataFrame({
        "Quantity": [2],
        "Price Per Unit": [-3.0],
        "Total Spent": [-6.0]
    })

    resultado = validar_ventas(df)

    assert resultado["cantidades_validas"]
    assert not resultado["precios_validos"]
    assert resultado["totales_validos"]


def test_total_incorrecto():
    df = pd.DataFrame({
        "Quantity": [2],
        "Price Per Unit": [3.0],
        "Total Spent": [10.0]
    })

    resultado = validar_ventas(df)

    assert resultado["cantidades_validas"]
    assert resultado["precios_validos"]
    assert not resultado["totales_validos"]


def test_valores_faltantes():
    df = pd.DataFrame({
        "Quantity": [np.nan, 2],
        "Price Per Unit": [3.0, 4.0],
        "Total Spent": [np.nan, 8.0]
    })

    resultado = validar_ventas(df)

    assert all(resultado.values())


def test_resumen_calidad():
    df = pd.DataFrame({
        "Quantity": [2, 3, np.nan, 1],
        "Price Per Unit": [3.0, 2.0, 4.0, np.nan],
        "Total Spent": [6.0, 6.0, np.nan, np.nan]
    })

    resultado = resumen_calidad(df)

    assert resultado["total_transacciones"] == 4
    assert resultado["transacciones_completas"] == 2
    assert resultado["transacciones_incompletas"] == 2
    assert resultado["porcentaje_completitud_numerica"] == 50.0
