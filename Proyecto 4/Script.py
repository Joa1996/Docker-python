import pandas as pd 
import os #importamos la libreria "os" para usar las variables de entorno, en nuestro caso
#es la variabl de entorno de file_value
# Obtenemos la ruta del archivo desde la variable de entorno
value=os.environ.get('file_value') #Obtenemos la variable de entorno
ruta =f'./data/{value}'

df=pd.read_csv(ruta,header=0)
df.loc['Total',:] = df.sum(axis=0)# Sumamos Total
df.to_csv('./data/SalidaArchivoTransformado.csv')
print('Proceso Finalizado usando Docker')