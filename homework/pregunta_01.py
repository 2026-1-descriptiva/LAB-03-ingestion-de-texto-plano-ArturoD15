"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

#leemos el archivo
def leer_archivo():
  with open("files/input/clusters_report.txt", "r") as f:
    lineas = f.readlines()
  #quitamos el \r que se alcanza a dectetar al final del txt
    lineas = [linea.replace("\r", "") for linea in lineas]
  return lineas

def extraer_datos(lineas):
  clusters = []
  cantidades = []
  porcentajes = []
  keywords_list = []
  #Eliminamos los espacios en blanco al principio o final de la linea
  for linea in lineas:
    stripped = linea.strip()
    if not stripped:
      continue
   #Dividimos el string de la linea en una lista     
    partes = stripped.split()
        
    # Línea de nuevo cluster: empieza con número (diferenciacion de cada lista)
    if partes[0].isdigit():
      clusters.append(partes[0])
      cantidades.append(partes[1])
      porcentajes.append(partes[2].replace(",", "."))
    # Todo lo que queda después del porcentaje son keywords
      keywords = " ".join(partes[4:])
      keywords_list.append(keywords)
        
    # Línea de continuación de keywords, no hay problema si colocamos partes [0] en este ejercicio
    elif keywords_list and not partes[0][0].isdigit():
      keywords_list[-1] += " " + stripped

  return clusters, cantidades, porcentajes, keywords_list

def limpieza_keywords(texto):
#dividimos las palabras por cada (,) OJO no cada palabra y dejamos solo un espacio no varios espacios.
  partes = texto.split(",")
  partes = [" ".join(espacio.split()) for espacio in partes]
  partes = [ultimo_espacio for ultimo_espacio in partes if ultimo_espacio.strip()]
 #utilizamos el strip(".") para eleminar el punto final de las palabras claves en cada lista  
  return ", ".join(partes).strip(".")

def pregunta_01():
  lineas = leer_archivo()
  clusters, cantidades, porcentajes, keywords_list = extraer_datos(lineas)
  keywords_limpias = [limpieza_keywords(k) for k in keywords_list]
# convertimos el archivo limpio en DataFrame
  df = pd.DataFrame({
  "cluster": clusters,
  "cantidad_de_palabras_clave": cantidades,
  "porcentaje_de_palabras_clave": porcentajes,
  "principales_palabras_clave": keywords_limpias
  })
# Convertir los tipos de datos (clusters, cantidad de palabras clave int) (porcentaje en float)
  df["cluster"] = df["cluster"].astype(int)
  df["cantidad_de_palabras_clave"] = df["cantidad_de_palabras_clave"].astype(int)
  df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].astype(float)
  return df

"""
Construya y retorne un dataframe de Pandas a partir del archivo
'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

- El dataframe tiene la misma estructura que el archivo original.
- Los nombres de las columnas deben ser en minusculas, reemplazando los
espacios por guiones bajos.
- Las palabras clave deben estar separadas por coma y con un solo
espacio entre palabra y palabra.


"""
