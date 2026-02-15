import pandas as pd

data_list = ['Juana', 'Pedro', 'Laura', 'Robert']
indice = ['Cuba', 'EEUU', 'España', 'Ecuador']

nacionalidad = pd.Series(index=indice, data=data_list)
print(nacionalidad)