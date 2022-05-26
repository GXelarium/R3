import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

def plot3d(u,v='N',w='N'):

    # Creación del espacio
    fig = plt.figure()
    grafica = fig.add_subplot(111,projection='3d')
    grafica.view_init(35, 25)

    # Etiqueta de los ejes
    grafica.set_xlabel('eje x')
    grafica.set_ylabel('eje y')
    grafica.set_zlabel('eje z')
    grafica.legend()

    # Graficar los puntos en el espacio
        
    # Vector cero
    origen = np.zeros([3])

    # vector u
    if (len(u) == 2):
        grafica.view_init(270, 360)
        u.append(0)
    [x,y,z] = u
    grafica.scatter(x,y,z, c ='blue', marker = 'o')
    
    # 0 -> u
    linea = np.concatenate(([origen],[u]), axis = 0)
    x = linea[:,0]
    y = linea[:,1]
    z = linea[:,2]
    grafica.plot(x,y,z)


    if (v != 'N'):
        if (len(v) == 2):
            v.append(0)
        # vector v
        [x,y,z] = v
        grafica.scatter(x,y,z, c ='yellow', marker = 'o')
        
        # 0 -> v
        linea = np.concatenate(([origen],[v]), axis = 0)
        x = linea[:,0]
        y = linea[:,1]
        z = linea[:,2]
        grafica.plot(x,y,z)

    if  (w != 'N'):
        if (len(w) == 2):
            w.append(0)
        # vector w
        [x,y,z] = w
        grafica.scatter(x,y,z, c ='green', marker = 'o')

        # 0 -> w
        linea = np.concatenate(([origen],[w]), axis = 0)
        x = linea[:,0]
        y = linea[:,1]
        z = linea[:,2]
        grafica.plot(x,y,z)

    
    # Mostrar gráfica
    plt.show()
    
