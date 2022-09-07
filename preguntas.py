"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""

archivo = open("data.csv", "r").readlines()

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    archivo = open("data.csv", "r").readlines()
    sumaCol2 = 0
    for row in archivo:
      sumaCol2 += int(row[2])

    return sumaCol2


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      if row[0] in dic:
        dic[row[0]] += 1
      else:
        dic[row[0]] = 1
    ListaDeItems = list(dic.items())
    ListaDeItems.sort()
    return ListaDeItems


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      if row[0] in dic:
        dic[row[0]] += int(row[2])
      else:
        dic[row[0]] = int(row[2])
    ListaDeItems = list(dic.items())
    ListaDeItems.sort()
    return ListaDeItems


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      row = row.split('\t')
      fecha = row[2].split('-')
      if fecha[1] in dic:
        dic[fecha[1]] += 1
      else:
        dic[fecha[1]] = 1
    ListaDeItems = list(dic.items())
    ListaDeItems.sort()

    return ListaDeItems


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      if row[0] in dic:
        mayor = dic[row[0]][0]
        menor = dic[row[0]][1]
        if int(mayor) < int(row[2]):
          dic[row[0]][0] = int(row[2])
        if int(menor) > int(row[2]):
          dic[row[0]][1] = int(row[2])
      else:
        dic[row[0]] = [int(row[2]),int(row[2])]
    ListaDeItems = list(dic.items())
    ListaDeItems.sort()
    respuesta = []

    for i in range(len(ListaDeItems)):
      x = (ListaDeItems[i][0],ListaDeItems[i][1][0],ListaDeItems[i][1][1])
      respuesta.append(x)
    return respuesta


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      row = row.split('\t')
      row = row[-1].split(',')
      element = row[-1].replace('\n', '')
      row.pop()
      row.append(element)
      for i in row:
        splited = i.split(':')
        if splited[0] in dic:
          mayor = dic[splited[0]][1]
          menor = dic[splited[0]][0]
          if int(mayor) < int(splited[1]):
            dic[splited[0]][1] = int(splited[1])
          if int(menor) > int(splited[1]):
            dic[splited[0]][0] = int(splited[1])
        else:
          dic[splited[0]] = [int(splited[1]),int(splited[1])]

    ListaDeItems = list(dic.items())
    ListaDeItems.sort()
    respuesta = []

    for i in range(len(ListaDeItems)):
        x = (ListaDeItems[i][0],ListaDeItems[i][1][0],ListaDeItems[i][1][1])
        respuesta.append(x)
    return respuesta


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      if int(row[2]) in dic:
        lista = dic[int(row[2])].copy()
        lista.append(row[0])
        dic[int(row[2])] = lista.copy()
      else:
        dic[int(row[2])] = [row[0]]
      
    ListaDeItems = list(dic.items())
    ListaDeItems.sort(key=lambda x: (x[0]), reverse=False)


    return ListaDeItems 


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      if int(row[2]) in dic:
        lista = dic[int(row[2])].copy()
        if not(row[0] in lista):
          lista.append(row[0])
          dic[int(row[2])] = lista.copy()
      else:
        dic[int(row[2])] = [row[0]]
      
    ListaDeItems = list(dic.items())
    ListaDeItems.sort(key=lambda x: (x[0],x[1].sort()), reverse=False)

    return ListaDeItems


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      row = row.split('\t')
      row = row[-1].split(',')
      element = row[-1].replace('\n', '')
      row.pop()
      row.append(element)
      for element in row:
        splited = element.split(':')
        if splited[0] in dic:
          dic[splited[0]] += 1
        else:
          dic[splited[0]] = 1
    dic2 = {}
    listaOrdenada = sorted(list(dic.items()))
    for i in listaOrdenada:
      dic2[i[0]] = i[1]

    return dic2


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    archivo = open("data.csv", "r").readlines()
    Respuesta = []
    for row in archivo:
  
      row = row.replace("\n","")
      row = row.split("\t")
      col1 = row[0]
      col4 = row[3]
      col5 = row[4]
      tabla_util = []
      tabla_util.append(col1)
      tabla_util.append(col4)
      tabla_util.append(col5)
      
      cantidadCol4 = len(tabla_util[1].split(","))
      cantidadCol5 = len(tabla_util[2].split(","))
      Respuesta.append((tabla_util[0], cantidadCol4, cantidadCol5))

    return Respuesta


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    archivo = open("data.csv", "r").readlines()
    dic = {}
    for row in archivo:
      row = row.replace("\n","")
      row = row.split("\t")
      col2 = row[1]
      col4 = row[3]
      tabla_util = []
      tabla_util.append(col2)
      tabla_util.append(col4)
      
      for i in tabla_util[1][::2]:
        if i in dic: 
          dic[i] = int(dic[i]) + int(tabla_util[0])
        else:
          dic[i] = int(tabla_util[0])

      dic2 = {}
      listaOrdenada = sorted(list(dic.items()))
      for i in listaOrdenada:
        dic2[i[0]] = i[1]
    return dic2


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    archivo = open("data.csv", "r").readlines()
    dic = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}
    for row in archivo:

      row = row.replace("\n","")
      row = row.split("\t")
      col1 = row[0]
      col5 = row[4]
      tabla_util = []
      tabla_util.append(col1)
      tabla_util.append(col5)
      elementos = (tabla_util[1].split(','))
      sum = 0
      for i in elementos:
        x = i.split(':')
        sum += int(x[1])
      dic[tabla_util[0]] += sum

    return dic
