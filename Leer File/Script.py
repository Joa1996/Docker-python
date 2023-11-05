import csv

# Obtenemos la ruta del archivo desde la variable de entorno
ruta = '/app/Leer.txt'

with  open(ruta, encoding='latin1') as csvarchivo:
      entrada=csv.reader(csvarchivo)
      for reg in entrada: #Recorremos todos las filas del csv y los imprimimos
          print(reg)
csvarchivo.close()

print('Probando Archivo')

