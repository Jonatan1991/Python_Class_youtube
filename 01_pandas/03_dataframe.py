import pandas as pd

data = {'Nombre':['Maria', 'Jose', 'David', 'Ivan'], 
        'Carrera': ['Auditoria', 'Informatica', 'Derecho', 'Idiomas'],
        'Correo': ['maria@fma.com', 'jose@dms.cu', 'david@gmail.com', 'ivan@sdsd.org']}

estudiantes = pd.DataFrame(data)

print(estudiantes)

df = pd.DataFrame([['Maria', 27], ['Jose', 30], ['Ana', 36], ['David', 22]],
                  columns=['NOMBRE', 'EDAD'])

print(df)