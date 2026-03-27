import pandas as pd

deportes_validos = {
    "Atletismo" : "atletismo",
    "Atletismo" : "ATLETISMO",
    "Boxeo" : "boxeo",
    "Boxeo" : "BOXEO",
    "Natacion" : "natacion",
    "Natacion" : "natació",
    "Natacion" : "Natació",
    "Natacion" : "NATACION",
    "Natacion" : "natación",
    "Natacion" : "NATACIÓN",
    "Voleibol" : "voleibol",
    "Volleyball" : "voleibol",
    "voleibol" : "VOLEIBOL",
    "voleibol" : "volleyball",
    "Tenis" : "tenis",
    "Tenis" : "Tennis",
    "Tenis" : "TENIS",
    "tenis" : "tennis",
    "Futbol" : "futbol",
    "Futbol" : "FUTBOL",
    "Futbol" : "fútbol",
    "Futbol" : "FÚTBOL",
    "Futbol" : "Fútbol",
    "Ciclismo" : "ciclismo",
    "Ciclismo" : "CICLISMO",
    "Ciclismo" : "ciclismo",
    "Baloncesto" : "baloncesto",
    "Baloncesto" : "BALONCESTO",
    "Baloncesto" : "Basketball",
    "Baloncesto" : "basketball",
    "Rugby" : "rugby",
    "Rugby" : "RUGBY",

}

#limpiar_deportistas(df)

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()

    #normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower().str.strip()

    df["deporte"] = (
        df["deporte"]
        .str.strip()
        .str.lower()
        .map(deportes_validos)
    )

    #Convertir peso_kg a float, reemplazar coma por punto

    for col in ["peso_kg"]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .pipe(pd.to_numeric, errors="coerce")

        )

    #Convertir columnas numéricas
    for col in ["edad", "altura_cm", "frecuencia_cardiaca_bpm"]:
        df[col] = df[col].pipe(pd.to_numeric, errors="coerce")

    #eliminar filas duplicadas
    df = df.drop_duplicates()

    #Detectar y eliminar outliers en peso_kg y horas_entrenamiento usando el método IQR
    for col in ["peso_kg", "horas_entrenamiento_semana"]:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        df = df[(df[col] >= limite_inferior) & (df[col] <= limite_superior)]

    #Imputar los valores nulos restantes con la media de cada columna numérica.
    for col in ["edad", "altura_cm", "frecuencia_cardiaca_bpm"]:
        df[col] = df[col].fillna(df[col].mean())

    return df
