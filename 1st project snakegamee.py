import pygame
import random
 
pygame.init()
score =0
font = pygame.font.Font(None, 36) 

width,height=600,600     
game_screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNAKE GAME")
snake_x,snake_y=width//2,height//2
change_x,change_y=0, 0
food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)
clock=pygame.time.Clock()
snake_body=[(snake_x,snake_y)]
game_over=False


def reset_game():
    global snake_x, snake_y, change_x, change_y, food_x, food_y, snake_body, score, game_over
    snake_x, snake_y = width // 2, height // 2
    change_x, change_y = 0, 0
    food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)
    snake_body = [(snake_x, snake_y)]
    score = 0
    game_over = False  # Restart flag  
def display_snake_and_food():
    global score,snake_x,snake_y,food_x,food_y,change_x,change_y,game_over

    if game_over:
     reset_gamee()
     return 
    
    game_screen.fill((0,0,0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    game_screen.blit(score_text, (10, 10))  

    
    snake_x=(snake_x+change_x)
    snake_y=(snake_y+change_y)
    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        print("GAME OVER - HIT BORDER")
        game_over=True
        return
        
    if (snake_x, snake_y) in snake_body[:-1]:  
      print("GAME OVER - HIT SELF")#self out
      game_over=True
      return
    snake_body.append((snake_x,snake_y))
    if(food_x==snake_x and food_y==snake_y):
          score += 1   #we can change score card rom 10-1
          food_x,food_y=random.randrange(0,width,10),random.randrange(0,height,10)
    else:
        del snake_body[0]
        

    pygame.draw.rect(game_screen,(255,0,0),[food_x,food_y,10,10])
    for (x, y) in snake_body:  
        pygame.draw.ellipse(game_screen,(255,255,255),[x,y,10,10]) 
     
    pygame.display.update()
def reset_gamee():
    global game_over
    game_screen.fill((0, 0, 0))
    text = font.render("Game Over! Press SPACE to Restart", True, (255, 255, 255))
    game_screen.blit(text, (width // 6, height // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    waiting = False

def game_loop():
    global change_x, change_y, game_over
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and change_x == 0:
                    change_x = -10
                    change_y = 0
                elif event.key == pygame.K_RIGHT and change_x == 0:
                    change_x = 10
                    change_y = 0
                elif event.key == pygame.K_UP and change_y == 0:
                    change_x = 0
                    change_y = -10
                elif event.key == pygame.K_DOWN and change_y == 0:
                    change_x = 0
                    change_y = 10
        
        display_snake_and_food()
        clock.tick(10)
    
    pygame.quit()
game_loop()



