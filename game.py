import sys, pygame
import asyncio
from project import generate_board


def initialize_game():
    pygame.init()

    size = width, height = 900, 900

    screen = pygame.display.set_mode(size)

    return screen


def load_numbers_images():
    numbers_map = {}
    c_numbers_map = {}

    for number in range(1,10):
        this_number = pygame.image.load(f'images\\numbers\\{number}.png').convert()
        this_number = pygame.transform.scale_by(this_number, 0.3)
        numbers_map[number] = this_number

        c_this_number = pygame.image.load(f'images\\clues_nums\\{number}_c.png').convert()
        c_this_number = pygame.transform.scale_by(c_this_number, 0.3)
        c_numbers_map[number] = this_number

    return numbers_map, c_numbers_map


#size_num = 48,48
def draw_numbers(numx,numbers_map,screen):
    
    for number_index in numbers_map.keys():
            if number_index >= 5:
                n_x,n_y = 225+numx*(number_index-5)*2,800
            else:
                n_x,n_y = 275+numx*(number_index-1)*2,750
            screen.blit(numbers_map[number_index],(n_x,n_y))

def generate_grid():
    grid_x = 125
    grid_y = 70
    cell_size = 70

    cells = {}
    cells_pos = {}

    for row in range(9):
        for col in range(9):
            x = grid_x + col * cell_size
            y = grid_y + row * cell_size

            cells[(row, col)] = pygame.Rect(
                x,
                y,
                cell_size,
                cell_size
            )

            cells_pos[((x,y),(x,y))] = (row, col)
    return cells

cells = generate_grid()

def draw_grid(screen):

    grid_x = 125
    grid_y = 70
    cell_size = 70
    grid_size = cell_size * 9

    for line in range(10):
        color = "red" if line % 3 == 0 else "black"

        line_y = grid_y + cell_size * line
        line_x = grid_x + cell_size * line

        pygame.draw.line(
            screen,
            color,
            (grid_x, line_y),
            (grid_x + grid_size, line_y),
            width=2
        )

        pygame.draw.line(
            screen,
            color,
            (line_x, grid_y),
            (line_x, grid_y + grid_size),
            width=2
        )

def get_click_cell(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        m_x, m_y = event.pos
        cm_x, cm_y = (m_x - 125 ) // 70, (m_y - 70 ) // 70
    
        if 0 <= cm_x <= 8 and 0 <= cm_y <= 8:
            this_grid = cells[(cm_x, cm_y)]
            return this_grid

def game_loop():

    screen = initialize_game()

    numbers_map, c_numbers_map = load_numbers_images()
    size_num = numx,numy = numbers_map[1].get_height(), numbers_map[1].get_width()
    size_grid = g_x,g_y = (500,500)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            get_click_cell(event)

        screen.fill('white')

        draw_grid(screen=screen)
        draw_numbers(numx=numx,numbers_map=numbers_map,screen=screen)
        
        pygame.display.flip()



if __name__ == '__main__':
    game_loop()
