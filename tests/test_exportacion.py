
import pandas as pd
import pytest


def preparar_dataframe():
    return pd.DataFrame({
        "Transaction ID": ["TXN_001", "TXN_002"],
        "Item": pd.Series(["Coffee", pd.NA], dtype="string"),
        "Quantity": [2.0, 1.0],
        "Price Per Unit": [2.0, 3.0],
        "Total Spent": [4.0, 3.0],
        "Payment Method": pd.Series(
            ["Cash", pd.NA], dtype="string"
        ),
        "Location": pd.Series(
            ["In-store", pd.NA], dtype="string"
        ),
        "Transaction Date": pd.to_datetime([
            "2023-01-01", "2023-01-02"
        ])
    })


def leer_csv(ruta):
    return pd.read_csv(
        ruta,
        dtype={
            "Transaction ID": "object",
            "Item": "string",
            "Payment Method": "string",
            "Location": "string"
        },
        parse_dates=["Transaction Date"]
    )


def test_exportacion_conserva_datos(tmp_path):
    df = preparar_dataframe()
    ruta = tmp_path / "ventas.csv"

    df.to_csv(ruta, index=False)
    recuperado = leer_csv(ruta)

    pd.testing.assert_frame_equal(
        df,
        recuperado,
        check_dtype=True
    )


def test_detecta_modificacion(tmp_path):
    df = preparar_dataframe()
    ruta = tmp_path / "ventas.csv"

    df.to_csv(ruta, index=False)
    recuperado = leer_csv(ruta)

    recuperado.loc[0, "Total Spent"] = 9999

    with pytest.raises(AssertionError):
        pd.testing.assert_frame_equal(
            df,
            recuperado,
            check_dtype=True
        )
