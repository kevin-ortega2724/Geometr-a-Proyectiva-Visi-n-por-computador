"""
Main de prueba


Daniela Buitrago, Kevin Ortega, Daniel Zapata
MIE - UTP
2023
"""

from main import Cube, Room, LShape, LineShape, FigureController, dibujar_cuarto, dibujar_cubo, \
    dibujar_lshape, dibujar_lineshape, actualizar_cubo, actualizar_lshape, actualizar_lineshape
import matplotlib.pyplot as plt

# Configura la visualización 3D y la interacción del usuario aquí

def main():
    # Crear la figura y el cuarto
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=0, azim=0)
    ax.set_axis_off()

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
    lineas_lshape = dibujar_lshape(controller_lshape.figure, ax)
    lineas_lineshape = dibujar_lineshape(controller_lineshape.figure, ax)

    # Variable para rastrear la figura actualmente controlada
    figura_actual = 'cubo'

    def on_key(event):
        nonlocal controller_cubo, controller_lshape, controller_lineshape
        nonlocal lineas_cubo, lineas_lshape, lineas_lineshape
        nonlocal figura_actual

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
    #plt.show()

if __name__ == "__main__":
    main()
