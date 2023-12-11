"""
Este módulo es la implementación del control de teclas


Daniela Buitrago, Kevin Ortega, Daniel Zapata
MIE - UTP
2023
"""
from transformations import translation_matrix, rotation_matrix, apply_transformation
from figures import Cube, LShape, LineShape
import numpy as np

class FigureController:
    def __init__(self, figure, initial_position=None):
        self.figure = figure
        if initial_position is not None:
            self.set_initial_position(initial_position)

    def is_within_bounds(self, transformed_vertices, room_dimensions):
        """Comprueba si la figura está dentro de los límites del cuarto."""
        x, y, z = room_dimensions
        within_x = (transformed_vertices[:, 0] >= 0) & (transformed_vertices[:, 0] <= x)
        within_y = (transformed_vertices[:, 1] >= 0) & (transformed_vertices[:, 1] <= y)
        within_z = (transformed_vertices[:, 2] >= 0) & (transformed_vertices[:, 2] <= z)
        return np.all(within_x) & np.all(within_y) & np.all(within_z)

    def set_initial_position(self, position):
        # Crear la matriz de transformación para la posición inicial
        matrix = translation_matrix(*position)
        # Aplica la transformación a los vértices de la figura
        transformed_vertices = apply_transformation(self.figure.vertices, matrix)
        self.figure.vertices = transformed_vertices

    def move_figure_to(self, position):
        """Mueve la figura a una nueva posición dada por una lista de coordenadas."""
        # Crear la matriz de transformación para mover la figura a la nueva posición
        matrix = translation_matrix(*position)
        # Aplica la transformación a los vértices de la figura
        self.move_figure(matrix)

    def move_figure(self, command):
        """Aplica un comando de movimiento o rotación a la figura."""
        # Definir los comandos y sus correspondientes acciones
        commands = {
            'w': ('translate', 'z', 1),
            'x': ('translate', 'z', -1),
            'a': ('translate', 'x', -1),
            'd': ('translate', 'x', 1),
            'e': ('translate', 'y', 1),
            'b': ('translate', 'y', -1),
            'u': ('rotate', 'x', 5),
            'j': ('rotate', 'x', -5),
            'i': ('rotate', 'y', 5),
            'n': ('rotate', 'y', -5),
            'p': ('rotate', 'z', 5),
            'm': ('rotate', 'z', -5),
        }

        if command in commands:
            action, axis, value = commands[command]
            if action == 'translate':
                matrix = translation_matrix(value if axis == 'x' else 0,
                                            value if axis == 'y' else 0,
                                            value if axis == 'z' else 0)
            elif action == 'rotate':
                matrix = rotation_matrix(axis, value)

            # Aplica la transformación solo a los vértices de la figura
            transformed_vertices = apply_transformation(self.figure.vertices, matrix)
            self.figure.vertices = transformed_vertices  # Actualiza solo los vértices


    def rotate_figure_90_degrees(self, axis):
        """Rota la figura 90 grados alrededor del eje especificado."""
        rotation_angle = np.radians(90)
        matrix = rotation_matrix(axis, rotation_angle)

        transformed_vertices = apply_transformation(self.figure.vertices, matrix)
        self.figure.vertices = transformed_vertices