import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def crear_cubo(lado):
    # Define los vértices de un cubo centrado en el origen
    mitad = lado / 2
    vertices = np.array([
        [-mitad, -mitad, -mitad, 1],
        [ mitad, -mitad, -mitad, 1],
        [ mitad,  mitad, -mitad, 1],
        [-mitad,  mitad, -mitad, 1],
        [-mitad, -mitad,  mitad, 1],
        [ mitad, -mitad,  mitad, 1],
        [ mitad,  mitad,  mitad, 1],
        [-mitad,  mitad,  mitad, 1]
    ])
    return vertices.T  # Transponer para obtener la forma 4xN
def crear_cuarto(ancho, largo, alto):
    # Define los vértices de un cuarto paralelepípedo
    x = ancho / 2
    y = largo / 2
    z = alto / 2
    vertices = np.array([
        [-x, -y, -z, 1],
        [ x, -y, -z, 1],
        [ x,  y, -z, 1],
        [-x,  y, -z, 1],
        [-x, -y,  z, 1],
        [ x, -y,  z, 1],
        [ x,  y,  z, 1],
        [-x,  y,  z, 1]
    ])
    return vertices.T

def matriz_traslacion(dx, dy, dz):
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])

def matriz_rotacion(eje, angulo):
    c, s = np.cos(np.radians(angulo)), np.sin(np.radians(angulo))
    if eje == 'x':
        return np.array([
            [1, 0,  0, 0],
            [0, c, -s, 0],
            [0, s,  c, 0],
            [0, 0,  0, 1]
        ])
    elif eje == 'y':
        return np.array([
            [ c, 0, s, 0],
            [ 0, 1, 0, 0],
            [-s, 0, c, 0],
            [ 0, 0, 0, 1]
        ])
    elif eje == 'z':
        return np.array([
            [c, -s, 0, 0],
            [s,  c, 0, 0],
            [0,  0, 1, 0],
            [0,  0, 0, 1]
        ])

def aplicar_transformacion(figura, matriz):
    return np.dot(matriz, figura)



def visualizar(figura, cuarto):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()

    # Dibuja el cubo
    for i in range(4):
        # Dibuja las aristas inferiores y superiores
        ax.plot([figura[0, i], figura[0, (i+1)%4]], [figura[1, i], figura[1, (i+1)%4]], [figura[2, i], figura[2, (i+1)%4]], color='b')
        ax.plot([figura[0, i+4], figura[0, (i+1)%4 + 4]], [figura[1, i+4], figura[1, (i+1)%4 + 4]], [figura[2, i+4], figura[2, (i+1)%4 + 4]], color='b')
        # Dibuja las aristas verticales
        ax.plot([figura[0, i], figura[0, i+4]], [figura[1, i], figura[1, i+4]], [figura[2, i], figura[2, i+4]], color='b')

    # Dibuja el cuarto
    for i in range(4):
        # Dibuja las aristas inferiores y superiores del cuarto
        ax.plot([cuarto[0, i], cuarto[0, (i+1)%4]], [cuarto[1, i], cuarto[1, (i+1)%4]], [cuarto[2, i], cuarto[2, (i+1)%4]], color='g')
        ax.plot([cuarto[0, i+4], cuarto[0, (i+1)%4 + 4]], [cuarto[1, i+4], cuarto[1, (i+1)%4 + 4]], [cuarto[2, i+4], cuarto[2, (i+1)%4 + 4]], color='g')
        # Dibuja las aristas verticales del cuarto
        ax.plot([cuarto[0, i], cuarto[0, i+4]], [cuarto[1, i], cuarto[1, i+4]], [cuarto[2, i], cuarto[2, i+4]], color='g')



    plt.show()





# Función para dibujar el cubo
def dibujar_cubo(cubo, ax):
    lines = []
    for i in range(4):
        # Dibuja las aristas inferiores y superiores del cubo
        line, = ax.plot([cubo[0, i], cubo[0, (i+1)%4]], [cubo[1, i], cubo[1, (i+1)%4]], [cubo[2, i], cubo[2, (i+1)%4]], color='b')
        lines.append(line)
        line, = ax.plot([cubo[0, i+4], cubo[0, (i+1)%4 + 4]], [cubo[1, i+4], cubo[1, (i+1)%4 + 4]], [cubo[2, i+4], cubo[2, (i+1)%4 + 4]], color='b')
        lines.append(line)
        # Dibuja las aristas verticales del cubo
        line, = ax.plot([cubo[0, i], cubo[0, i+4]], [cubo[1, i], cubo[1, i+4]], [cubo[2, i], cubo[2, i+4]], color='b')
        lines.append(line)
    return lines

# Función para dibujar el cuarto
def dibujar_cuarto(cuarto, ax):
    for i in range(4):
        # Dibuja las aristas inferiores y superiores del cuarto
        ax.plot([cuarto[0, i], cuarto[0, (i+1)%4]], [cuarto[1, i], cuarto[1, (i+1)%4]], [cuarto[2, i], cuarto[2, (i+1)%4]], color='g')
        ax.plot([cuarto[0, i+4], cuarto[0, (i+1)%4 + 4]], [cuarto[1, i+4], cuarto[1, (i+1)%4 + 4]], [cuarto[2, i+4], cuarto[2, (i+1)%4 + 4]], color='g')
        # Dibuja las aristas verticales del cuarto
        ax.plot([cuarto[0, i], cuarto[0, i+4]], [cuarto[1, i], cuarto[1, i+4]], [cuarto[2, i], cuarto[2, i+4]], color='g')

# Función para actualizar la posición del cubo
def actualizar_cubo(cubo, lineas_cubo):
    idx = 0
    for i in range(4):
        # Actualiza las aristas inferiores y superiores del cubo
        lineas_cubo[idx].set_data([cubo[0, i], cubo[0, (i+1)%4]], [cubo[1, i], cubo[1, (i+1)%4]])
        lineas_cubo[idx].set_3d_properties([cubo[2, i], cubo[2, (i+1)%4]])
        idx += 1
        lineas_cubo[idx].set_data([cubo[0, i+4], cubo[0, (i+1)%4 + 4]], [cubo[1, i+4], cubo[1, (i+1)%4 + 4]])
        lineas_cubo[idx].set_3d_properties([cubo[2, i+4], cubo[2, (i+1)%4 + 4]])
        idx += 1
        # Actualiza las aristas verticales del cubo
        lineas_cubo[idx].set_data([cubo[0, i], cubo[0, i+4]], [cubo[1, i], cubo[1, i+4]])
        lineas_cubo[idx].set_3d_properties([cubo[2, i], cubo[2, i+4]])
        idx += 1
    plt.draw()

# Crear la figura y el cuarto
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()
cuarto = crear_cuarto(5, 5, 5)
dibujar_cuarto(cuarto, ax)

# Crear y dibujar el cubo
posicion_inicial_cubo = [1, 1, 1]  # Posición inicial del cubo
cubo = crear_cubo(1)
cubo = aplicar_transformacion(cubo, matriz_traslacion(*posicion_inicial_cubo))
lineas_cubo = dibujar_cubo(cubo, ax)

# Manejador de eventos de teclado
def on_key(event):
    global cubo
    comando = event.key
    # Convertir pulsaciones de teclado en comandos de movimiento
    movimiento = {
        'w': ('z', 1), 's': ('z', -1),
        'a': ('x', -1), 'd': ('x', 1),
        'e': ('y', 1), 'q': ('y', -1),
        'u': ('rx', 5), 'j': ('rx', -5),
        'i': ('ry', 5), 'k': ('ry', -5),
        'o': ('rz', 5), 'l': ('rz', -5),
    }
    if comando in movimiento:
        eje, valor = movimiento[comando]
        if eje in ['x', 'y', 'z']:
            cubo = aplicar_transformacion(cubo, matriz_traslacion(valor if eje == 'x' else 0,
                                                                  valor if eje == 'y' else 0,
                                                                  valor if eje == 'z' else 0))
        elif eje in ['rx', 'ry', 'rz']:
            cubo = aplicar_transformacion(cubo, matriz_rotacion(eje[1], valor))
        actualizar_cubo(cubo, lineas_cubo)

fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()




