import numpy as np
import pandas as pd
## caherine eileen huerta rascon NC = 0072
## datos matriz 4 x 3
datos_alumnos = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas 
# y almacenar la variable df (dataframe)
print("------Datos a partir de una matriz 4x3-------")
df=pd.DataFrame(datos_alumnos,columns=["iq","marcas","paquetes"])
print(df)

# datos a partir de un diccionario
dic_alumnos = {
    "nombre":["andresini","alonsini","mati","pedrini","michelin"],
    "califa":[70,67,90,80,100],
    "edad":[67,+81,25,53,10],
}
print("----Datos a partir de un dicionario 4x3----")
estudiantes = pd.DataFrame(dic_alumnos)
print(estudiantes)
print("catherine eileen huerta rascon NC = 0072")