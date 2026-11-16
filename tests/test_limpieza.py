
import pandas as pd

from src.limpieza import normalizar_errores


def test_normalizar_errores():
    original = pd.DataFrame({
        "Item": ["Coffee", "ERROR", "UNKNOWN"]
    })

    resultado = normalizar_errores(
        original,
        ["Item"]
    )

    assert resultado["Item"].isna().sum() == 2

    assert resultado.loc[0, "Item"] == "Coffee"

    assert original.loc[1, "Item"] == "ERROR"


from src.limpieza import (
    recuperar_quantity,
    recuperar_quantity_con_auditoria
)


def test_recupera_quantity_valida():
    df = pd.DataFrame({
        "Quantity": [None],
        "Price Per Unit": [3],
        "Total Spent": [12]
    })

    resultado = recuperar_quantity(df)

    assert resultado.loc[0, "Quantity"] == 4


def test_no_recupera_quantity_decimal():
    df = pd.DataFrame({
        "Quantity": [None],
        "Price Per Unit": [3],
        "Total Spent": [10]
    })

    resultado = recuperar_quantity(df)

    assert pd.isna(resultado.loc[0, "Quantity"])


def test_no_modifica_quantity_existente():
    df = pd.DataFrame({
        "Quantity": [2],
        "Price Per Unit": [3],
        "Total Spent": [12]
    })

    resultado = recuperar_quantity(df)

    assert resultado.loc[0, "Quantity"] == 2


def test_auditoria_quantity():
    df = pd.DataFrame({
        "Transaction ID": ["TXN_001", "TXN_002"],
        "Quantity": [None, None],
        "Price Per Unit": [3, 3],
        "Total Spent": [12, 10]
    })

    resultado, registro = (
        recuperar_quantity_con_auditoria(df)
    )

    assert resultado.loc[0, "Quantity"] == 4
    assert pd.isna(resultado.loc[1, "Quantity"])

    assert len(registro) == 1
    assert registro.iloc[0]["Transaction ID"] == "TXN_001"
    assert registro.iloc[0]["New Value"] == 4
