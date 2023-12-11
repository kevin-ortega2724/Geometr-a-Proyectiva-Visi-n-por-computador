"""
Crea 3 figuras a partir del un cubo, cuyos vértices son de refrencia


Daniela Buitrago, Kevin Ortega, Daniel Zapata
MIE - UTP
2023
"""
import numpy as np

class Cube:
    def __init__(self, side_length):
        self.vertices = self._create_cube(side_length)

    @staticmethod
    def _create_cube(side_length):
        half = side_length / 2
        vertices = np.array([
            [-half, -half, -half, 1],
            [half, -half, -half, 1],
            [half, half, -half, 1],
            [-half, half, -half, 1],
            [-half, -half, half, 1],
            [half, -half, half, 1],
            [half, half, half, 1],
            [-half, half, half, 1]
        ])
        return vertices.T  # Transponer para obtener la forma 4xN
    def get_edges(self):
        # Define las aristas del cubo a partir de los vértices
        edges = [(0, 1), (1, 2), (2, 3), (3, 0),
                 (4, 5), (5, 6), (6, 7), (7, 4),
                 (0, 4), (1, 5), (2, 6), (3, 7)] #Esto se borra.
        return edges
class Room:
    def __init__(self, width, length, height):
        self.vertices = self._create_room(width, length, height)

    @staticmethod
    def _create_room(width, length, height):
        x = width / 2
        y = length / 2
        z = height / 2
        vertices = np.array([
            [-x, -y, -z, 1],
            [x, -y, -z, 1],
            [x, y, -z, 1],
            [-x, y, -z, 1],
            [-x, -y, z, 1],
            [x, -y, z, 1],
            [x, y, z, 1],
            [-x, y, z, 1]
        ])
        return vertices.T

class LShape:
    def __init__(self, side_length):
        self.side_length = side_length
        self.vertices = self._create_lshape()
        #self.transformation_matrix = np.identity(4)

    def _create_lshape(self):
        # Crea la forma de "L" a partir de 4 cubos
        cubes = []
        for i in range(3):
            # Tres cubos alineados verticalmente
            cube = Cube(self.side_length)
            cube_vertices = cube.vertices + np.array([[0], [i * self.side_length], [0], [0]])
            cubes.append(cube_vertices)

        # El cuarto cubo a la derecha del tercer cubo
        cube = Cube(self.side_length)
        cube_vertices = cube.vertices + np.array([[self.side_length], [2 * self.side_length], [0], [0]])
        cubes.append(cube_vertices)

        # Unir los vértices de los cuatro cubos
        lshape_vertices = np.concatenate(cubes, axis=1)
        return lshape_vertices
    def get_edges(self):
        # Define las aristas de la figura en forma de L a partir de los vértices
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 5)]
        return edges

class LineShape:
    def __init__(self, side_length):
        self.side_length = side_length
        self.vertices = self._create_lineshape()
        #self.transformation_matrix = np.identity(4)

    def _create_lineshape(self):
        # Crea una línea a partir de 3 cubos alineados horizontalmente
        cubes = []
        for i in range(3):
            cube = Cube(self.side_length)
            cube_vertices = cube.vertices + np.array([[i * self.side_length], [0], [0], [0]])
            cubes.append(cube_vertices)

        # Unir los vértices de los tres cubos
        lineshape_vertices = np.concatenate(cubes, axis=1)
        return lineshape_vertices
    def get_edges(self):
        # Define las aristas de la figura en forma de línea a partir de los vértices
        edges = [(0, 1), (1, 2), (2, 3)]
        return edges
    
class Sphere:
    def __init__(self, radius, center=[0, 0, 0]):
        self.radius = radius
        self.center = center
        self.vertices = self._create_sphere()

    def _create_sphere(self):
        # Genera los vértices para una esfera
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = self.center[0] + self.radius * np.cos(u) * np.sin(v)
        y = self.center[1] + self.radius * np.sin(u) * np.sin(v)
        z = self.center[2] + self.radius * np.cos(v)
        return x, y, z