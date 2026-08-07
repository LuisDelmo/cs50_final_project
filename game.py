import sys, pygame
import numpy as np


def initialize_game():
    pygame.init()

    size = width, height = 900, 900

    screen = pygame.display.set_mode(size)
    lives = 3

    return screen, lives


def load_numbers_images():
    numbers_map = {}
    c_numbers_map = {}

    for number in range(1,10):
        this_number = pygame.image.load(f'images\\numbers\\{number}.png').convert()
        this_number = pygame.transform.scale_by(this_number, 0.3)
        numbers_map[number] = this_number

        c_this_number = pygame.image.load(f'images\\clues_nums\\{number}_c.png')
        c_this_number = pygame.transform.scale_by(c_this_number, 0.3)
        c_numbers_map[number] = c_this_number

    return numbers_map, c_numbers_map


#size_num = 48,48
def rect_numbers(numx,numbers_map):

    rect_num_map = {}
    for number_index in numbers_map.keys():
        if number_index >= 5:
            n_x,n_y = 225+numx*(number_index-5)*2,800
        else:
            n_x,n_y = 275+numx*(number_index-1)*2,750

        rect_num_map[number_index] = pygame.Rect(n_x,
                                                n_y,
                                                numx,
                                                numx)
    return rect_num_map

def draw_nums(screen,numbers_map,rect_num_map):

    for number_index in numbers_map.keys():
        n_x ,n_y ,_ ,_ = rect_num_map[number_index]
        screen.blit(numbers_map[number_index],(n_x,n_y))


def generate_grid():
    grid_x = 125
    grid_y = 70
    cell_size = 70

    cells = {}
    rect_cells = {}

    for row in range(9):
        for col in range(9):
            x = grid_x + col * cell_size
            y = grid_y + row * cell_size

            cells[(row, col)] = (x+12.5,y+12.5)

            rect_cells[(row, col)] = pygame.Rect(
                x,
                y,
                cell_size,
                cell_size
            )

    return cells, rect_cells



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
        if event.button == 1:
            m_x, m_y = event.pos
            cm_x, cm_y = (m_x - 125 ) // 70, (m_y - 70 ) // 70
        
            if 0 <= cm_x <= 8 and 0 <= cm_y <= 8:
                # this_grid = cells[(cm_x, cm_y)]
                # print(cm_x, cm_y)
                return (cm_y, cm_x)

    return None

def draw_clues(screen,board,c_numbers_map,cells):
    empty_count = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row,col] == 0:
                empty_count += 1
                continue

            screen.blit(c_numbers_map[board[row,col]],cells[(row,col)])
    if empty_count == 81:
        return False
    return True



def game_loop(name,generate_board,solve):

    screen, lives = initialize_game()
    select_empty_cell = False
    select_num = False
    font = pygame.font.Font(None, 50)

    numbers_map, c_numbers_map = load_numbers_images()
    size_num = numx,numy = numbers_map[1].get_height(), numbers_map[1].get_width()
    cells, rect_cell = generate_grid()
    

    rect_num_map = rect_numbers(numx=numx,numbers_map=numbers_map)

    board = generate_board(name)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            click_coord = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m_x, m_y = event.pos
                    cm_x, cm_y = (m_x - 125 ) // 70, (m_y - 70 ) // 70

                    select_num = False
                    if 0 <= cm_x <= 8 and 0 <= cm_y <= 8:
                        click_coord = cm_y, cm_x
                    for num_index in rect_num_map:
                        rect_num = rect_num_map[num_index]
                        if rect_num.collidepoint(event.pos):
                            select_num = (num_index,{
                                    'surface' : screen,
                                    'color' : 'Blue',
                                    'width' : 5,
                                    'rect' : rect_num})



        screen.fill('white')

        draw_grid(screen=screen)
        
        #draw num
        draw_nums(screen,numbers_map,rect_num_map)
        lives_text = font.render(f'Lives: {lives}',True,'Green')
        screen.blit(lives_text)

        empty_board = draw_clues(screen,board,c_numbers_map,cells)

        if click_coord is not None:
            
            if board[click_coord] == 0:
                select_empty_cell = (click_coord,{
                        'surface' : screen,
                        'color' : 'Blue',
                        'width' : 5,
                        'rect' : rect_cell[click_coord]})
            else:
                select_empty_cell = False

        if select_empty_cell is not False:
            pygame.draw.rect(**select_empty_cell[1])
            if select_num is not False:
                pygame.draw.rect(**select_num[1])

                cell_index = select_empty_cell[0]
                this_number = select_num[0]
                next_board_state = np.copy(board)
                next_board_state[cell_index] = this_number

                solved = solve(next_board_state,fastest=True)

                if solved is None:
                    lives -= 1
                else:
                    board[cell_index] = this_number

                select_empty_cell = False
                select_num = False

        if lives <= 0:
            board = solve(board=board,fastest=True)
            text_surface = font.render("You lost", True, 'Red')
            screen.blit(text_surface)

        if not empty_board:
            screen.fill('white')
            won = font.render("You WON", True, 'Green')
            screen.blit(won)


        pygame.display.flip()



if __name__ == '__main__':
    game_loop()
