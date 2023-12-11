"""
Main


Daniela Buitrago, Kevin Ortega, Daniel Zapata
MIE - UTP
2023
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from figures import Cube, Room, LShape, LineShape
from controller import FigureController
from transformations import apply_transformation

def dibujar_cubo(cubo, ax):
    # Dibuja las aristas del cubo
    lines = []
    for i in range(4):
        line, = ax.plot([cubo[0, i], cubo[0, (i+1)%4]], [cubo[1, i], cubo[1, (i+1)%4]], [cubo[2, i], cubo[2, (i+1)%4]], color='b')
        lines.append(line)
        line, = ax.plot([cubo[0, i+4], cubo[0, (i+1)%4 + 4]], [cubo[1, i+4], cubo[1, (i+1)%4 + 4]], [cubo[2, i+4], cubo[2, (i+1)%4 + 4]], color='b')
        lines.append(line)
        line, = ax.plot([cubo[0, i], cubo[0, i+4]], [cubo[1, i], cubo[1, i+4]], [cubo[2, i], cubo[2, i+4]], color='b')
        lines.append(line)
    return lines

def dibujar_cuarto(cuarto, ax):
    # Dibuja las aristas del cuarto
    for i in range(4):
        ax.plot([cuarto[0, i], cuarto[0, (i+1)%4]], [cuarto[1, i], cuarto[1, (i+1)%4]], [cuarto[2, i], cuarto[2, (i+1)%4]], color='g')
        ax.plot([cuarto[0, i+4], cuarto[0, (i+1)%4 + 4]], [cuarto[1, i+4], cuarto[1, (i+1)%4 + 4]], [cuarto[2, i+4], cuarto[2, (i+1)%4 + 4]], color='g')
        ax.plot([cuarto[0, i], cuarto[0, i+4]], [cuarto[1, i], cuarto[1, i+4]], [cuarto[2, i], cuarto[2, i+4]], color='g')

def actualizar_cubo(cubo, lineas_cubo):
    idx = 0
    for i in range(4):
        lineas_cubo[idx].set_data([cubo[0, i], cubo[0, (i+1)%4]], [cubo[1, i], cubo[1, (i+1)%4]])
        lineas_cubo[idx].set_3d_properties([cubo[2, i], cubo[2, (i+1)%4]])
        idx += 1
        lineas_cubo[idx].set_data([cubo[0, i+4], cubo[0, (i+1)%4 + 4]], [cubo[1, i+4], cubo[1, (i+1)%4 + 4]])
        lineas_cubo[idx].set_3d_properties([cubo[2, i+4], cubo[2, (i+1)%4 + 4]])
        idx += 1
        lineas_cubo[idx].set_data([cubo[0, i], cubo[0, i+4]], [cubo[1, i], cubo[1, i+4]])
        lineas_cubo[idx].set_3d_properties([cubo[2, i], cubo[2, i+4]])
        idx += 1
    plt.draw()

def dibujar_lshape(lshape, ax):
    lines = []
    for i in range(4):  # Para cada uno de los 4 cubos
        for j in range(4):  # Para cada una de las 4 aristas en la base del cubo
            base = i * 8  # Base para los índices de columna del cubo actual
            # Dibujar aristas en la base del cubo
            line, = ax.plot([lshape.vertices[0, base + j], lshape.vertices[0, base + (j+1)%4]], 
                            [lshape.vertices[1, base + j], lshape.vertices[1, base + (j+1)%4]], 
                            [lshape.vertices[2, base + j], lshape.vertices[2, base + (j+1)%4]], color='r')
            lines.append(line)
            # Dibujar aristas en la parte superior del cubo
            line, = ax.plot([lshape.vertices[0, base + j + 4], lshape.vertices[0, base + (j+1)%4 + 4]], 
                            [lshape.vertices[1, base + j + 4], lshape.vertices[1, base + (j+1)%4 + 4]], 
                            [lshape.vertices[2, base + j + 4], lshape.vertices[2, base + (j+1)%4 + 4]], color='r')
            lines.append(line)
            # Dibujar aristas verticales
            line, = ax.plot([lshape.vertices[0, base + j], lshape.vertices[0, base + j + 4]], 
                            [lshape.vertices[1, base + j], lshape.vertices[1, base + j + 4]], 
                            [lshape.vertices[2, base + j], lshape.vertices[2, base + j + 4]], color='r')
            lines.append(line)
    return lines


def dibujar_lineshape(lineshape, ax):
    lines = []
    for i in range(3):  # Para cada uno de los 3 cubos
        for j in range(4):  # Para cada una de las 4 aristas en la base del cubo
            base = i * 8  # Base para los índices de columna del cubo actual
            # Dibujar aristas en la base del cubo
            line, = ax.plot([lineshape.vertices[0, base + j], lineshape.vertices[0, base + (j+1)%4]], 
                            [lineshape.vertices[1, base + j], lineshape.vertices[1, base + (j+1)%4]], 
                            [lineshape.vertices[2, base + j], lineshape.vertices[2, base + (j+1)%4]], color='g')
            lines.append(line)
            # Dibujar aristas en la parte superior del cubo
            line, = ax.plot([lineshape.vertices[0, base + j + 4], lineshape.vertices[0, base + (j+1)%4 + 4]], 
                            [lineshape.vertices[1, base + j + 4], lineshape.vertices[1, base + (j+1)%4 + 4]], 
                            [lineshape.vertices[2, base + j + 4], lineshape.vertices[2, base + (j+1)%4 + 4]], color='g')
            lines.append(line)
            # Dibujar aristas verticales
            line, = ax.plot([lineshape.vertices[0, base + j], lineshape.vertices[0, base + j + 4]], 
                            [lineshape.vertices[1, base + j], lineshape.vertices[1, base + j + 4]], 
                            [lineshape.vertices[2, base + j], lineshape.vertices[2, base + j + 4]], color='g')
            lines.append(line)
    return lines


def actualizar_lshape(lshape, lineas_lshape):
    idx = 0
    vertices_por_cubo = 8
    # Asumiendo que LShape tiene 4 cubos
    for num_cubo in range(4):
        inicio = num_cubo * vertices_por_cubo
        for j in range(4):  # 4 aristas en la base
            # Actualizar las aristas horizontales y verticales en la base del cubo
            lineas_lshape[idx].set_data([lshape.vertices[0, inicio + j], lshape.vertices[0, inicio + (j+1)%4]], 
                                        [lshape.vertices[1, inicio + j], lshape.vertices[1, inicio + (j+1)%4]])
            lineas_lshape[idx].set_3d_properties([lshape.vertices[2, inicio + j], lshape.vertices[2, inicio + (j+1)%4]])
            idx += 1

            # Actualizar las aristas horizontales y verticales en la parte superior del cubo
            lineas_lshape[idx].set_data([lshape.vertices[0, inicio + j + 4], lshape.vertices[0, inicio + (j+1)%4 + 4]], 
                                        [lshape.vertices[1, inicio + j + 4], lshape.vertices[1, inicio + (j+1)%4 + 4]])
            lineas_lshape[idx].set_3d_properties([lshape.vertices[2, inicio + j + 4], lshape.vertices[2, inicio + (j+1)%4 + 4]])
            idx += 1

            # Actualizar las aristas verticales que conectan la base y la parte superior
            lineas_lshape[idx].set_data([lshape.vertices[0, inicio + j], lshape.vertices[0, inicio + j + 4]], 
                                        [lshape.vertices[1, inicio + j], lshape.vertices[1, inicio + j + 4]])
            lineas_lshape[idx].set_3d_properties([lshape.vertices[2, inicio + j], lshape.vertices[2, inicio + j + 4]])
            idx += 1

def actualizar_lineshape(lineshape, lineas_lineshape):
    idx = 0
    vertices_por_cubo = 8
    for num_cubo in range(3):
        inicio = num_cubo * vertices_por_cubo
        for j in range(4):  # 4 aristas en la base
            # Actualizar las aristas horizontales y verticales en la base del cubo
            lineas_lineshape[idx].set_data([lineshape.vertices[0, inicio + j], lineshape.vertices[0, inicio + (j+1)%4]], 
                                           [lineshape.vertices[1, inicio + j], lineshape.vertices[1, inicio + (j+1)%4]])
            lineas_lineshape[idx].set_3d_properties([lineshape.vertices[2, inicio + j], lineshape.vertices[2, inicio + (j+1)%4]])
            idx += 1

            # Actualizar las aristas horizontales y verticales en la parte superior del cubo
            lineas_lineshape[idx].set_data([lineshape.vertices[0, inicio + j + 4], lineshape.vertices[0, inicio + (j+1)%4 + 4]], 
                                           [lineshape.vertices[1, inicio + j + 4], lineshape.vertices[1, inicio + (j+1)%4 + 4]])
            lineas_lineshape[idx].set_3d_properties([lineshape.vertices[2, inicio + j + 4], lineshape.vertices[2, inicio + (j+1)%4 + 4]])
            idx += 1

            # Actualizar las aristas verticales que conectan la base y la parte superior
            lineas_lineshape[idx].set_data([lineshape.vertices[0, inicio + j], lineshape.vertices[0, inicio + j + 4]], 
                                           [lineshape.vertices[1, inicio + j], lineshape.vertices[1, inicio + j + 4]])
            lineas_lineshape[idx].set_3d_properties([lineshape.vertices[2, inicio + j], lineshape.vertices[2, inicio + j + 4]])
            idx += 1

# Crear la figura y el cuarto
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=0, azim=0)
ax.set_axis_off()

# Crear figuras y controladores
cuarto = Room(5, 5, 5)
cubo = Cube(1)
lshape = LShape(1)
lineshape = LineShape(1)

controller_cubo = FigureController(cubo)
controller_lshape = FigureController(lshape)
controller_lineshape = FigureController(lineshape)


instrucciones = "Presiona 1 para controlar el cubo\nPresiona 2 para controlar LShape\nPresiona 3 para controlar LineShape"
ax.text2D(0.05, 0.95, instrucciones, transform=ax.transAxes, color='white', fontsize=10, bbox=dict(facecolor='red', alpha=0.5))



# Dibujar figuras
dibujar_cuarto(cuarto.vertices, ax)
lineas_cubo = dibujar_cubo(controller_cubo.figure.vertices, ax)
lineas_lshape = dibujar_lshape(controller_lshape.figure, ax)  # Pasar la instancia completa de LShape
lineas_lineshape = dibujar_lineshape(controller_lineshape.figure, ax)  # Pasar la instancia completa de LineShape



# Variable para rastrear la figura actualmente controlada
figura_actual = 'cubo'

def on_key(event):
    global controller_cubo, controller_lshape, controller_lineshape
    global lineas_cubo, lineas_lshape, lineas_lineshape
    global figura_actual

    # Cambiar la figura actualmente seleccionada.
    if event.key == '1':
        figura_actual = 'cubo'
    elif event.key == '2':
        figura_actual = 'lshape'
    elif event.key == '3':
        figura_actual = 'lineshape'

    # Mover la figura actualmente seleccionada.
    if figura_actual == 'cubo':
        controller_cubo.move_figure(event.key)
        actualizar_cubo(controller_cubo.figure.vertices, lineas_cubo)
    elif figura_actual == 'lshape':
        controller_lshape.move_figure(event.key)
        actualizar_lshape(controller_lshape.figure, lineas_lshape)
    elif figura_actual == 'lineshape':
        controller_lineshape.move_figure(event.key)
        actualizar_lineshape(controller_lineshape.figure, lineas_lineshape)

    plt.draw()


fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()