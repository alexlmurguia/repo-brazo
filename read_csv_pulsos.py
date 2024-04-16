# En este código se importa un archivo csv, el cual contiene
# los pulsos generados tomando en cuenta el tiempo de muestreo
# Estos pulsos se convierten a RPM y se genera un csv con dichos datos

# Se importan librerias
import pandas as pd

# Se lee el archivo csv 
df = pd.read_csv("datos_open_loop2.csv")
# Se guardan los datos de la columna pulsos en una variable llamada igual
pulsos = df["pulsos"]

r = pulsos.size
RPM = list() # Lista en donde se guardaran los cálculos de RPM
T = 0.008 # Tiempo de muestreo con el que se capturaron los datos

# Para cada valor de pulso...
for i in range(r):
    
    pulso = pulsos[i]
    
    # formula para calcular las RPM en dicho segundo
    valor = ((pulso/T)*60)/540
 
    RPM.append(valor)
    
# Se guarda la lista de RPM en un archivo csv
dic = {"RPM": RPM}
df = pd.DataFrame(dic)
df.to_csv('OLSint.csv')


