import pandas as pd

df = pd.read_csv('01_pandas/datos.csv')

print(df.iloc[1, 4])

print(df.iloc[2, :3])

print(df.loc[1, 'carrera'])


acepta = df.pop('acepta')
#time,carrera,acepta,positivo,negativo,edad,sexo,trabajo
df = df.aggregate(pd.Series(['1', '2', '3', '4'],
                         index=['time', 'carrera', 'acepta', 'positivo', 'negativo', 'edad', 'sexo', 'trabajo']))