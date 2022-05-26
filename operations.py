import math
import plots as plt

# Función principal
def operation(lecture: str):
    # Variables auxiliares
    u = []
    v = []
    op = ''
    aux = lecture.find(")")
    
    # Guarda el primer vector
    du = lecture[1:aux]
    u = svector(du)

    # Guarda el segundo vector y el operador
    if aux+1 != len(lecture):
        dv = lecture[aux + 3:-1]
        v = svector(dv)

        op = lecture[aux+1]

    
    res = resultado(op,u,v)
    
    return res



# Guarda las cadenas en listas
def svector (text: str):
    tam = len(text)
    vector = []
    aux = [i for i in range (tam) if text[i] == ','] # Lista con los índices de las comas en los vectores

    # Guarda cada valor númerico en la lista vector 
    for j in range(len(aux)):
        if j == 0:
            vector.append(float(text[:aux[j]]))
        else:
            vector.append(float(text[aux[j-1] + 1 :aux[j]]))
    # Guarda el último valor numérico
    l = aux.pop()
    if l+1 == tam - 1:
        vector.append(float(text[-1:]))
    else:
        vector.append(float(text[l+1:]))
    
    return vector



def resultado(operador: str, vector_1: list, vector_2: list):
    
    if operador == '+':
      print(f"u = {vector_1} -> azul")
      print(f"v = {vector_2} -> amarrillo")
      res = suma(vector_1, vector_2)
      print(f"u+v = {res} -> verde\n\n\n")

      plt.plot3d(vector_1, vector_2, res)
    
    elif operador == '-':
      print(f"u = {vector_1} -> azul")
      print(f"v = {vector_2} -> amarrillo")
      res = resta(vector_1, vector_2)
      print(f"u-v = {res} -> verde\n\n\n")

      plt.plot3d(vector_1, vector_2, res)      
    
    elif operador == 'x' or operador == 'X':
      print(f"u = {vector_1} -> azul")
      print(f"v = {vector_2} -> amarrillo")
      res = prod_vect(vector_1, vector_2)
      print(f"uxv = {res} -> verde\n\n\n")

      plt.plot3d(vector_1,vector_2,res)
    
    elif operador == '*' or operador == '.':
      print(f"u = {vector_1} -> azul")
      print(f"v = {vector_2} -> amarrillo")
      res = prod_punto(vector_1, vector_2)
      print(f"u*v = {res}\n\n\n")

      plt.plot3d(vector_1,vector_2)

    elif operador == ',':
      print(f"u = {vector_1} -> azul")
      print(f"v = {vector_2} -> amarrillo")
      res = angle(vector_1, vector_2)
      print(f"angulo(u,v) = {res}")
      res = distance(vector_1,vector_2)
      print(f"d(u,v) = {res}\n\n\n")

      plt.plot3d(vector_1,vector_2)
    
    elif operador == '' or vector_2 == []:
      print(f"u = {vector_1} -> azul")
      res = norma(vector_1)
      print(f"|u| = {res}\n\n\n")
      
      plt.plot3d(vector_1)

# Suma de Vectores
def suma(u: list, v: list):
    res = []
    for i in range(len(v)):
        aux = u[i] + v[i]
        res.append(aux)
    
    return res


# Resta de vectores
def resta(u: list, v: list):
  res = []
  for i in range(len(u)):
    res.append(u[i]-v[i])
  
  return res


# Producto interno de vectores
def prod_punto(u: list, v: list):
  res = 0.0
  for i in range(len(u)):
    res += u[i] * v[i]
  
  return res


# Producto vectorial en R3
def prod_vect(u: list, v: list):
  res = []
  aux = u[1] * v[2] - u[2] * v[1]
  res.append(aux)
  aux = u[0] * v[2] - u[2] * v[0]
  res.append(-aux)
  aux = u[0] * v[1] - u[1] * v[0]
  res.append(aux)

  return res

# Norma de un vector
def norma(u: list):
  res = math.sqrt((prod_punto(u,u)))
  
  return res


# Ángulo entre vectores
def angle(u: list, v: list):
  num = prod_punto(u,v)
  dem = norma(u) * norma(v)
  div = num/dem
  res = math.acos(div)

  return res


# Distancia entre dos vectores
def distance(u: list, v: list):
    aux = resta(u,v)
    res = norma(aux)

    return res