import pandas as pd

df = pd.read_csv('01_pandas/ModalidadVirtual.csv')

#print(df)

print(df['carrera'][1])

#filtrar los datos por edad
filtrar = df['edad'] > 23
df_filtrar = df[filtrar]

print(df_filtrar)

#-------------------------------------

print(df.tail(10))
print(df.head(10))