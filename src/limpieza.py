
import pandas as pd


def normalizar_errores(df, columnas):
    resultado = df.copy()

    for columna in columnas:
        resultado[columna] = resultado[columna].replace(
            ["ERROR", "UNKNOWN"],
            pd.NA
        )

    return resultado


def recuperar_quantity(df):
    resultado = df.copy()

    columnas = [
        "Quantity",
        "Price Per Unit",
        "Total Spent"
    ]

    for columna in columnas:
        resultado[columna] = pd.to_numeric(
            resultado[columna],
            errors="coerce"
        )

    cantidad = resultado["Quantity"]
    precio = resultado["Price Per Unit"]
    total = resultado["Total Spent"]

    candidatas = (
        cantidad.isna()
        & precio.notna()
        & total.notna()
        & (precio > 0)
        & (total > 0)
    )

    calculadas = total.loc[candidatas] / precio.loc[candidatas]

    validas = (
        calculadas.gt(0)
        & calculadas.mod(1).eq(0)
    )

    indices_validos = calculadas.index[validas]

    resultado.loc[
        indices_validos, "Quantity"
    ] = calculadas.loc[indices_validos]

    return resultado


def recuperar_quantity_con_auditoria(df):
    resultado = recuperar_quantity(df)

    originales = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    recuperadas = (
        originales.isna()
        & resultado["Quantity"].notna()
    )

    indices = df.index[recuperadas]

    registro = pd.DataFrame({
        "Transaction ID": df.loc[
            indices, "Transaction ID"
        ].to_numpy(),

        "Column": "Quantity",

        "Original Value": df.loc[
            indices, "Quantity"
        ].to_numpy(),

        "New Value": resultado.loc[
            indices, "Quantity"
        ].to_numpy(),

        "Reason": (
            "Calculated from Total Spent / Price Per Unit"
        )
    })

    return resultado, registro
