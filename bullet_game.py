import pygame
pygame.font.init()

width, height = 800, 500

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((width, height))
border_width = 15

player_width, player_height = 50, 50

vel = 10

bullet_width = 20
bullet_height = 10
max_bullets = 5
bullet_vel = 9

lives = 7

font = pygame.font.SysFont("comicsans", 30)


def draw(left, right, right_bullets, left_health, right_health):
    left_font = font.render(f"Health:{left_health}", 1, "blue")
    right_font = font.render(f"Health:{right_health}", 1, "blue")
    screen.blit(left_font, (0 + 10, 5))
    screen.blit(right_font, (width - right_font.get_width() - 10, 5))


    pygame.draw.line(screen, "black", (width/2 - border_width/2, 0), (width/2 - border_width/2, height), border_width)

    pygame.draw.rect(screen, 'blue', left)
    pygame.draw.rect(screen, 'green', right)

    for bullet in left_bullets:
        pygame.draw.rect(screen, "red", bullet)
        bullet.x += bullet_vel
        if bullet.x > width + bullet_width:
            left_bullets.remove(bullet)

        if pygame.Rect.colliderect(bullet, right):
            left_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))



    for bullet in right_bullets:
        pygame.draw.rect(screen, "red", bullet)

        bullet.x -= bullet_vel
        if bullet.x < 0 - bullet_width:
            right_bullets.remove(bullet)
        elif bullet.colliderect(left):
            right_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(pygame.USEREVENT + 2))

        




def move_players(keys, left, right):
    # LEFT PLAYER
    if keys[pygame.K_w] and left.y > 0: # UP
        left.y -= vel
   
    if keys[pygame.K_s]and left.y < height - player_height: # DOWN
        left.y += vel
    
    if keys[pygame.K_d] and left.x < width/2 - player_width - border_width: # RIGHT
        left.x += vel
   
    if keys[pygame.K_a] and left.x > 0: # LEFT
        left.x -= vel

    # RIGHT PLAYER
    if keys[pygame.K_UP] and right.y > 0: # UP
        right.y -= vel
   
    if keys[pygame.K_DOWN]and right.y < height - player_height: # DOWN
        right.y += vel
    
    if keys[pygame.K_RIGHT] and right.x < width - player_height: # RIGHT
        right.x += vel
   
    if keys[pygame.K_LEFT] and right.x > width/2: # LEFT
        right.x -= vel


def make_bullets(keys, left_bullets, right_bullets):
    if keys[pygame.K_SPACE] and len(left_bullets) < max_bullets:
        bullet = pygame.Rect(left.x + player_width, left.y + player_height/2 - bullet_height/2, bullet_width, bullet_height)
        left_bullets.append(bullet)

    
    if keys[pygame.K_RSHIFT] and len(right_bullets) < max_bullets:
        bullet = pygame.Rect(right.x - bullet_width, right.y + player_height/2 - bullet_height/2, bullet_width, bullet_height)
        right_bullets.append(bullet)

    
    return left_bullets, right_bullets



left = pygame.Rect(200, 200, player_width, player_height)
right = pygame.Rect(600, 200, player_width, player_height)
left_bullets = []
right_bullets = []

left_health = lives
right_health = lives

run = True
while run:
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            make_bullets(keys, left_bullets, right_bullets)

        if event.type == pygame.USEREVENT + 1: # RIGHT HIT
            right_health -= 1
            if right_health == 0:
                winning_messege = font.render("Left won!", 1, "black")
                screen.blit(winning_messege, (width/2 - winning_messege.get_width()/2, height/2 - winning_messege.get_height()/2))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False

        if event.type == pygame.USEREVENT + 2: # LEFT HIT
            left_health -= 1
            if left_health == 0:
                winning_messege = font.render("Right won!", 1, "black")
                screen.blit(winning_messege, (width/2 - winning_messege.get_width()/2, height/2 - winning_messege.get_height()/2))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False






    keys = pygame.key.get_pressed()
    move_players(keys, left, right)

    draw(left, right, right_bullets, left_health, right_health)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
