import pygame
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

WIDTH, HEIGHT = 400, 400 

ROWS = 3
COLS = 3
SQUARE_SIZE = WIDTH//COLS
THICKNESS = 10
positions = [[None]*3 for _ in range(3)]

font = pygame.font.SysFont("comicsans", 30)
screen = pygame.display.set_mode((HEIGHT, WIDTH))

def draw_lines():
    for i in range(1, ROWS):
        y = i*SQUARE_SIZE
        pygame.draw.line(screen, "black", (0, y), (WIDTH, y),THICKNESS)

    for i in range(1, COLS):
        x = i*SQUARE_SIZE
        pygame.draw.line(screen, "black", (x, 0), (x, HEIGHT), THICKNESS)


def get_mouse_pos():
    pos_x, pos_y = pygame.mouse.get_pos()
    pos_x = pos_x//SQUARE_SIZE
    pos_y = pos_y//SQUARE_SIZE
    return pos_x, pos_y  


def draw_pieces(x, y, turn):
    if turn % 2 == 0:
        pygame.draw.line(screen, "orange", (x*SQUARE_SIZE + SQUARE_SIZE*0.25, y* SQUARE_SIZE+SQUARE_SIZE*0.25), (x*SQUARE_SIZE + SQUARE_SIZE*0.75, y* SQUARE_SIZE+SQUARE_SIZE*0.75), THICKNESS+15)
        pygame.draw.line(screen, "orange", (x*SQUARE_SIZE + SQUARE_SIZE*0.25, y* SQUARE_SIZE+SQUARE_SIZE*0.75), (x*SQUARE_SIZE + SQUARE_SIZE*0.75, y* SQUARE_SIZE+SQUARE_SIZE*0.25), THICKNESS+15)
       
        positions[y][x] = "x"
    else:
        pygame.draw.circle(screen, "teal", (x*SQUARE_SIZE+SQUARE_SIZE//2, y*SQUARE_SIZE+SQUARE_SIZE//2,), SQUARE_SIZE/3)
        pygame.draw.circle(screen, "pink", (x*SQUARE_SIZE+SQUARE_SIZE//2, y*SQUARE_SIZE+SQUARE_SIZE//2,), SQUARE_SIZE*0.25)

        positions[y][x] = "o"



def check_row(positions):
    for row in positions:
        if row.count(row[0]) == len(row) and row[0] != None:
            return row[0]
            
        
def check_col(pos):
    for row in range(len(pos)):
        for col in range(len(pos[row])):
            ooo = pos[0][0], pos[1][0], pos[2][0]

            if None not in ooo:
                if "".join(ooo) == "ooo":
                    print(f"{pos[0][0]} won!")
                    winner = ooo[0]
                    return winner
                elif "".join(ooo) == "xxx":
                    print(f"{pos[0][0]} won!")
                    winner = ooo[0]
                    return winner
                
def check_diagonal(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            ooo = grid[0][0], grid[1][1], grid[2][2]

            if None not in ooo:
                if "".join(ooo) == "ooo":
                    return ooo[0] 
                elif "".join(ooo) == "xxx":
                    return ooo[0]
            ooo = grid[2][0], grid[1][1], grid[0][2]

            if None not in ooo:
                if "".join(ooo) == "ooo":
                    return ooo[0] 
                elif "".join(ooo) == "xxx":
                    return ooo[0]
            
    
            
    


def print_grid(positions):
    print()
    for col in range(len(positions[0])):
        for i, row in enumerate(positions):
            if i == 2:
                print(row[col])
            else:
                print(row[col], end=" | ")
    



def main():
    screen.fill("pink")
    draw_lines()

    turn = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = get_mouse_pos()
                turn += 1
                draw_pieces(x, y, turn)
                print_grid(positions)

                row_winner = check_row(positions)
                if row_winner:
                    winning_font = font.render(f"{row_winner} wins!", 1, "white")
                    screen.blit(winning_font, (WIDTH/2 - winning_font.get_width()/2, HEIGHT/2 - winning_font.get_height()/2))
                    pygame.display.update()
                    pygame.time.delay(500)
                    run = False        
                
                col_winner = check_col(positions)
                if col_winner:
                    #print(col)
                    winning_font = font.render(f"{col_winner} wins!", 1, "black")
                    screen.blit(winning_font, (WIDTH/2 - winning_font.get_width()/2, HEIGHT/2 - winning_font.get_height()/2))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    run = False    

                diag_winner = check_diagonal(positions)  
                if diag_winner:
                    winning_font = font.render(f"{diag_winner} wins!", 1, "black")
                    screen.blit(winning_font, (WIDTH/2 - winning_font.get_width()/2, HEIGHT/2 - winning_font.get_height()/2))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    run = False    
  
            


        pygame.display.update()

        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
