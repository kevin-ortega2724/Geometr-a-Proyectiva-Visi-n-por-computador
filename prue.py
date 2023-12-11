import pygame
import pygame_projective

# Define las figuras que se pueden usar
FIGURES = ["cube", "triangle", "rectangle"]

# Define las reglas de juego
def detect_collisions(board):
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i].collides_with(board[j]):
                # El juego termina cuando dos bloques se tocan
                global game_over
                game_over = True

# Define la clase Block
class Block:

    def __init__(self, position, size, shape):
        self.position = position
        self.size = size
        self.shape = shape

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        self.shape = shape

    def collides_with(self, other_block):
        # Usa la biblioteca pygame_projective para detectar colisiones
        projection = pygame_projective.project_point(self.position, self.size, self.shape)
        other_projection = pygame_projective.project_point(other_block.position, other_block.size, other_block.shape)
        return pygame_projective.point_in_polygon(projection, other_projection)

# Define la clase Board
class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)

    def get_blocks(self):
        return self.blocks

# Define la función para generar un nuevo tablero de juego
def generate_new_board(width, height, num_blocks):
    board = Board(width, height)
    for i in range(num_blocks):
        block_type = random.choice(FIGURES)
        block_size = random.randint(1, 5)
        block_position = (random.randint(0, width), random.randint(0, height))
        block = Block(block_position, block_size, block_type)
        board.add_block(block)
    return board

# Define la función para dibujar el tablero de juego
def draw_board(board, screen):
    for block in board.get_blocks():
        projection = pygame_projective.project_block(block.position, block.size, block.shape)
        pygame_projective.draw_block(screen, projection)

# Define la función principal
def main():
    # Inicializa Pygame
    pygame.init()

    # Crea la pantalla
    screen = pygame.display.set_mode((640, 480))

    # Crea el tablero de juego
    board = generate_new_board(640, 480, 20)

    # Inicializa el bucle de juego
    game_over = False
    while not game_over:
        # Actualiza la posición y la rotación de los bloques
        for block in board.get_blocks():
            block.position = pygame.mouse.get_pos()
            block.rotation = pygame.mouse.get_rotation()

        # Detecta colisiones entre bloques
        detect_collisions(board.get_blocks())

        # Dibuja el tablero de juego
        draw_board(board, screen)

        # Actualiza la pantalla
        pygame.display.update()

    # Termina Pygame
    pygame.quit()

# Llama a la función principal
if __name__ == "__main__":
    main()
