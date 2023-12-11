import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Función para dibujar un paralelepípedo (cuarto)
def draw_parallelepiped(ax, origin, dimensions):
    # Desempaquetar origen y dimensiones
    ox, oy, oz = origin
    dx, dy, dz = dimensions

    # Crear los puntos de las esquinas del paralelepípedo
    points = np.array([[0, 0, 0], [dx, 0, 0], [dx, dy, 0], [0, dy, 0],
                       [0, 0, dz], [dx, 0, dz], [dx, dy, dz], [0, dy, dz]]) + [ox, oy, oz]

    # Definir los bordes del paralelepípedo
    edges = [[points[i] for i in [0, 1, 2, 3, 0, 4, 5, 6, 7, 4, 5, 1, 2, 6, 7, 3]]]
    
    # Dibujar los bordes
    ax.add_collection3d(Poly3DCollection(edges, linewidths=1, edgecolors='r', alpha=.25))

# Configuración del gráfico
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el cuarto
draw_parallelepiped(ax, origin=[-2, -2, -2], dimensions=[4, 4, 4])

# Configurar límites y mostrar
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_zlim([-4, 4])
plt.show()
