import numpy as np
import matplotlib.pyplot as plt
from figures import Cube, LShape, LineShape
from controller import FigureController
from transformations import translation_matrix, rotation_matrix, apply_transformation

def perspective_projection_matrix(near, far, fov, aspect):
    """
    Crea una matriz de proyección en perspectiva.
    
    near: Plano de recorte cercano
    far: Plano de recorte lejano
    fov: Campo de visión vertical, en grados
    aspect: Razón de aspecto, que es width/height de la ventana de visualización
    """
    f = 1.0 / np.tan(np.radians(fov) / 2)
    return np.array([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
        [0, 0, -1, 0]
    ])

# Función para proyectar los vértices de una figura
def project_vertices(vertices, projection_matrix):
    # Transformar vértices a coordenadas homogéneas (añadir una fila de unos)
    vertices_homogeneous = np.vstack((vertices, np.ones((1, vertices.shape[1]))))
    # Aplicar la matriz de proyección
    projected = projection_matrix @ vertices_homogeneous
    # Normalizar las coordenadas homogéneas
    projected /= projected[3, :]
    # Retornar las coordenadas x e y proyectadas
    return projected[0:2, :]
    


# Función para dibujar una figura en el plot
def draw_figure(ax, figure, edges, color='black'):
    for edge in edges:
        start, end = edge
        # Suponiendo que figure.vertices es un array de NumPy
        # con las coordenadas en la forma (x, y, z, w)
        projected_start = project_vertices(figure.vertices[:, start], projection_matrix)
        projected_end = project_vertices(figure.vertices[:, end], projection_matrix)
        ax.plot([projected_start[0], projected_end[0]],
                [projected_start[1], projected_end[1]], color=color)

## Creación de figuras
cube = Cube(side_length=1)
lshape = LShape(side_length=1)
line_shape = LineShape(side_length=1)


# Creación de controladores para cada figura
cube_controller = FigureController(cube)
lshape_controller = FigureController(lshape)
line_shape_controller = FigureController(line_shape)


# Obtener las aristas usando los controladores específicos de la figura
cube_edges = cube_controller.get_edges()
lshape_edges = lshape_controller.get_edges()
line_shape_edges = line_shape_controller.get_edges()



# Configuración de la ventana de visualización
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')

# Proyección en perspectiva
fov = 90
aspect_ratio = 1  # Cambiar según la forma de la ventana de visualización
near = 0.1
far = 100
projection_matrix = perspective_projection_matrix(near, far, fov, aspect_ratio)

# Dibujar figuras en el plot
draw_figure(ax, cube, cube_edges, 'blue')
draw_figure(ax, lshape, lshape_edges, 'red')
draw_figure(ax, line_shape, line_shape_edges, 'green')

# Configuración de los límites del plot
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Función para manejar eventos del teclado

def on_key(event):
    # Usamos el controlador adecuado dependiendo de la figura que queremos mover
    if event.key in ['w', 'a', 's', 'd', 'q', 'e']:
        cube_controller.move_figure(event.key)
    elif event.key in ['i', 'j', 'k', 'l']:
        lshape_controller.move_figure(event.key)
    # Agrega aquí más controles para diferentes figuras y teclas

    # Redibujar todas las figuras con sus nuevas posiciones
    ax.cla()  # Limpia el eje actual
    draw_figure(ax, cube, cube_controller.figure.edges, 'blue')
    draw_figure(ax, lshape, lshape_controller.figure.edges, 'red')
    draw_figure(ax, line_shape, line_shape_controller.figure.edges, 'green')
    plt.draw()

# Conectar el evento del teclado
fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
