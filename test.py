import pygame

pygame.init()

# colors

white=(255,255,255)
red=(255,0,0)
balck=(0,0,0)

# Creating window
gameWindow=pygame.display.set_mode((900,600))
pygame.display.set_caption("Snake Don Hai")


#game specefic variables
exit_game=False # if some one wants to exit pygame
game_over=False # when game is over for a player

#creating a game loop-- this loops continues until game is running,fncn:: ex: it continosly takes input form the users
while not exit_game:
    for event in pygame.event.get():
        print(event) # this will capture all the event done by user


        if event.type==pygame.QUIT:
            exit_game=True

        
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:

                print('You have pressend the right key')

        if event.type==pygame.KEYUP:
            if event.key ==pygame.K_RIGHT: 
                print('You have released the right key')
    gameWindow.fill(white)
    pygame.display.update() # every time you change the display

pygame.quit()
quit()