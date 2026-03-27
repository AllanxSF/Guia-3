import pandas as pd

#Resumen_datos(df): total de deportistas, promedio de rendimiento, edad promedio
def resumen_datos(df: pd.DataFrame) -> pd.DataFrame:
    resumen = {
        "total_deportistas": len(df),
        "promedio_rendimiento": df["rendimiento_score"].mean(),
        "edad_promedio": df["edad"].mean()
    }
    return pd.DataFrame([resumen])

#Promedio_por_deporte(df): promedio de rendimiento agrupado por disciplina.
def promedio_por_deporte(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("deporte")["rendimiento_score"].mean().reset_index()

#Deportistas_destacados(df): filtrar deportistas con rendimiento_score mayor al umbral(7.0)
def deportistas_destacados(df: pd.DataFrame, umbral: float = 7.0) -> pd.DataFrame:
    return df[df["rendimiento_score"] > umbral]