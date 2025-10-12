import pygame
import random
 
pygame.init()
score =0
FONT = pygame.font.SysFont("Arial", 34)

# FONT = pygame.font.Font(None, 36)  

WIDTH, HEIGHT=600,600 
CELL = 10 ####   
game_screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE GAME")
clock = pygame.time.Clock() #####

snake_x, snake_y = WIDTH//2, HEIGHT//2
change_x,change_y = CELL, 0  ###

snake_body=[(snake_x,snake_y)]
food_x, food_y = random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL)
game_over=False


def reset_game():
    global snake_x, snake_y, change_x, change_y, food_x, food_y, snake_body, score, game_over
    snake_x, snake_y =  WIDTH// 2, HEIGHT // 2
    change_x, change_y = CELL, 0

    snake_body = [(snake_x, snake_y)]
    food_x, food_y = random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL)
    
    score = 0
    game_over = False  # Restart flag


def show_game_over():
    """Non-blocking Game Over screen"""
    game_screen.fill((0, 0, 0))
    text = FONT.render("GAME OVER! Press SPACE to Restart", True, (255, 255, 255))
    game_screen.blit(text, (WIDTH // 6, HEIGHT // 2))
    pygame.display.update()

def display_snake_and_food():
    global score,snake_x,snake_y,food_x,food_y,change_x,change_y,game_over

    if game_over:
        
        show_game_over()
        return
    
  
#move snake
    snake_x+=change_x
    snake_y+=change_y
    

    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        game_over = True
        return


# collision with itself
    snake_body.append((snake_x,snake_y))
    if (snake_x, snake_y) in snake_body[:-1]:
      game_over = True
      return
    

#food collision

    if (snake_x, snake_y) == (food_x, food_y):
       score += 1   
       food_x,food_y = random.randrange(0,WIDTH,CELL),random.randrange(0,HEIGHT,CELL)
    else:
        del snake_body[0]
        

        
    game_screen.fill((0,0,0))
    pygame.draw.rect(game_screen, (255,0,0) ,(food_x,food_y,CELL,CELL))
    for (x, y) in snake_body:  
        pygame.draw.ellipse(game_screen,(255,255,255),[x,y,CELL,CELL]) 

    score_text = FONT.render(f"Score: {score}", True, (255, 255, 255))
    game_screen.blit(score_text, (15, 15))  # Draw score at top-left
    pygame.display.update()


def game_loop():
    global change_x, change_y, game_over
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



            if event.type == pygame.KEYDOWN:

                if game_over and event.key == pygame.K_SPACE:
                    reset_game()
                elif not game_over:
                    if event.key == pygame.K_LEFT and change_x == 0:
                        change_x, change_y = -CELL, 0
                    
                    
                    elif event.key == pygame.K_RIGHT and change_x == 0:
                      change_x, change_y = CELL, 0
                 
                    elif event.key == pygame.K_UP and change_y == 0:
                      change_x, change_y = 0,-CELL
                    
                    elif event.key == pygame.K_DOWN and change_y == 0:
                      change_x, change_y = 0,CELL
                   
        display_snake_and_food()
        clock.tick(10)
    
    pygame.quit()
#game_loop()
import asyncio

async def main():
    game_loop()

asyncio.run(main())

