import pandas as pd

convertir = pd.read_excel('01_pandas/datos.xlsx')

convertir.to_csv('01_pandas/datos.csv', index=None, header=True)

print(pd.read_csv('01_pandas/datos.csv'))