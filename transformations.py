"""
Este módulo aplica las transformaciones


Daniela Buitrago, Kevin Ortega, Daniel Zapata
MIE - UTP
2023
"""
import numpy as np

def translation_matrix(dx, dy, dz):
    """Crea una matriz de traslación."""
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])

def rotation_matrix(axis, angle):
    """Crea una matriz de rotación alrededor de un eje específico."""
    angle = np.radians(angle)
    c, s = np.cos(angle), np.sin(angle)

    if axis == 'x':
        return np.array([
            [1, 0,  0, 0],
            [0, c, -s, 0],
            [0, s,  c, 0],
            [0, 0,  0, 1]
        ])
    elif axis == 'y':
        return np.array([
            [ c, 0, s, 0],
            [ 0, 1, 0, 0],
            [-s, 0, c, 0],
            [ 0, 0, 0, 1]
        ])
    elif axis == 'z':
        return np.array([
            [c, -s, 0, 0],
            [s,  c, 0, 0],
            [0,  0, 1, 0],
            [0,  0, 0, 1]
        ])

def apply_transformation(figure, matrix):
    """Aplica una transformación matricial a una figura."""
    return np.dot(matrix, figure)