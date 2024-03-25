import pygame
import random
import os

pygame.init()
pygame.mixer.init()

# colors

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

# Creating window
gameWindow=pygame.display.set_mode((900,600))
pygame.display.set_caption("Snake Don Hai")
pygame.display.update()


img=pygame.image.load('image.png')
img=pygame.transform.scale(img,(900,600)).convert_alpha()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)



def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list ,snake_size):
    for x,y in snk_list:

        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game=False

    pygame.mixer.music.load('bg.mp3')
    pygame.mixer.music.play() 
    while not exit_game:
        gameWindow.fill((233,220,229))
        gameWindow.blit(img,(0,0))
       
        text_screen("Welcomes to Snakes",black,250,270)
        text_screen("Press Space to PLAY!",black,250,500)
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('food.mp3')
                    pygame.mixer.music.play()

                    gameloop()

        pygame.display.update()
        clock.tick(30)




# game loop
def gameloop():

    if (not os.path.exists("highscore.txt")):
        with open('highscore.txt','w') as f:
            f.write("0")

    with open("highscore.txt",'r') as f:
        highscore=f.read()


#game specefic variables

    score=0

    hardness=5
    exit_game=False
    game_over=False 

    snake_x=10
    snake_y=10

    velocity_x=0
    velocity_y=0

    snake_size=10

    snk_list=[]
    snk_lenght=1

    food_x=random.randint(25,900/2)
    food_y=random.randint(25,600/2)


    

    fps=30

    while not exit_game:

        if game_over:
            with open("highscore.txt",'w') as f:
                f.write(str(highscore))
            gameWindow.fill((233,220,229))
  
            text_screen("Game Over! Press Enter to Continue",red,100,270)
            for event in pygame.event.get(): 


                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:

                    if event.key==pygame.K_RETURN:
                        welcome()

        
        
        else:



            for event in pygame.event.get(): 


                if event.type==pygame.QUIT:
                    exit_game=True
                
                if event.type == pygame.KEYDOWN:

                    if event.key==pygame.K_RIGHT:
                        velocity_x=hardness
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-1*hardness
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        velocity_y=-1*hardness
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=hardness
                        velocity_x=0

                    if event.key==pygame.K_q:
                        score=score+1
                        

            snake_x=snake_x+ velocity_x
            snake_y=snake_y+ velocity_y

            if abs(snake_x-food_x)<12 and abs(snake_y-food_y)<12:
                score=score+1
                snk_lenght+=3
                food_x=random.randint(25,900/2)
                food_y=random.randint(25,600/2)
                pygame.mixer.music.load('food.mp3')
                pygame.mixer.music.play()
            if score*10>int(highscore):
                highscore=score*10


            gameWindow.fill(white)
  
            text_screen(f'Score::{score*10}  High Score::{highscore}',red,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenght:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>900 or snake_y<0 or snake_y>600:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow,black,snk_list,snake_size)



        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


if __name__=='__main__':
    welcome()