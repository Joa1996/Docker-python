import pandas as pd 

# Obtenemos la ruta del archivo desde la variable de entorno
ruta ='./data/File.csv'

df=pd.read_csv(ruta,header=0)
df.loc['Total',:] = df.sum(axis=0)# Sumamos Total
df.to_csv('./data/SalidaArchivoTransformado.csv')
print('Proceso Finalizado usando Docker')