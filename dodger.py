import pygame
import random
import time
import os
pygame.font.init()

clock = pygame.time.Clock()
fps = 60
width, height = 800, 500

bg = pygame.image.load(os.path.join("starry_image.jpg"))
bg = pygame.transform.scale(bg, (width, height))

screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont("Arial", 30)

player_height = 40
player_width = 30
player_vel = 8

star_height = 20
star_width = 10
star_vel = 3

max_lives = 5

def draw(player, stars, elapsed_time, lives):
    screen.blit(bg, (0,0))

    time_text = font.render(f"time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (10, 10))

    lives_text = font.render(f"lives: {lives}", 1, "white")
    screen.blit(lives_text, (width - lives_text.get_width() - 10, 10))


    pygame.draw.rect(screen, "pink", player)

    for star in stars:
        pygame.draw.rect(screen, "red", star)



    pygame.display.update()

    


 
def main():
    lives = max_lives
    player = pygame.Rect(width/2, height - player_height, player_width, player_height)

    start_time = time.time()

    star_add_increment = 2000
    star_count = 0

    stars = []

    run = True 
    while run:
        star_count += clock.tick(fps)

        elapsed_time = time.time() - start_time

        if star_count > star_add_increment: 
            for _ in range(4):            
                ran_x = random.randint(0, width-star_width)
                star = pygame.Rect(ran_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)   
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0: # LEFT
                player.x -= player_vel

        if keys[pygame.K_RIGHT] and player.x < width - player_width: # RIGHT
            player.x += player_vel


        for star in stars[:]:  
            star.y += star_vel
            if star.y > height:
                stars.remove(star)

            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                lives -= 1
                


        draw(player, stars, elapsed_time, lives)
       
        if lives <= 0:
            lost_text = font.render("You Lost!", 1, "white")
            time_text = font.render(f"You lasted for {round(elapsed_time)} seconds", 1, "white")

            screen.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2) )
            screen.blit(time_text, (width/2 - time_text.get_width()/2, height/2 + lost_text.get_height() + 10) )

            pygame.display.update()
            pygame.time.delay(2000)

            main()



  
        
    pygame.quit()

if __name__ == "__main__":
    main()
