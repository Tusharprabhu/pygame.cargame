import pygame
from pygame.locals import *
import random
import sys
import time

pygame.init()


def game_main():
    
    size= width,height= (1200,800)
    road_w= int(width/1.5)
    roadmark_w= int(width/80)
    t=time.sleep(0.5)

    red= (255,0,0)
    TEXTCOLOR = (255, 255, 255)
    black= (0,0,0)
    green=(60,220,0)
    white = (255,255,255)
    

    screen=pygame.display.set_mode(size,RESIZABLE)
    pygame.display.set_caption("tushar's car game")
    #screen color
    screen.fill(green)
    
    secs=0
    mins=0
    hours=0
    game_done=True
    font=pygame.font.Font ('freesansbold.ttf', 32)
    # text=font.render("{}".format (mins), True, (255, 255, 255), (0, 0, 0))


    right_lane= width/2+road_w/4
    left_lane= width/2-road_w/4
    middle_lane= width/2 

    def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    def terminate():
        pygame.quit()
        sys.exit()

    def waitForPlayerToPressKey():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: #escape quits
                        terminate()
                    return
    
    def game_over():
        game_restart_font = pygame.font.Font('freesansbold.ttf',100)
        screen.fill(black)
        display_game_over= game_restart_font.render("Wasted!!",True,red,black)
        screen.blit(display_game_over,((width / 3) - 50,(height / 3)))
        drawText('Press any key to start the game.', font, screen, (width / 3) - 100, (height / 3)+100)
        screen.blit(text,((width / 3) - 50,(height / 3)+150))


    def trophy_spawn():
        if trophy_loc[1]> height:
            trophy_loc[1]=-200
            trophy.set_alpha(255)      
            random_loc=random.randint(0,2)
            if random_loc==0:
                trophy_loc.center = left_lane,-200
            elif random_loc==1:
                trophy_loc.center = right_lane,-200
            elif random_loc==2:
                trophy_loc.center = middle_lane,-200     
            
    def game_restart():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: #escape quits
                        terminate()
                    else:
                        game_main()
                    return
    clock = pygame.time.Clock()

    running = True


    pygame.display.update()
    
    
    #1car
    car = pygame.image.load("car.png")
    car_loc=car.get_rect()
    car_loc.center= middle_lane,height*0.8
    
    
    #2car
    car2 = pygame.image.load("otherCar.png")
    car2_loc=car2.get_rect()
    car2_loc.center= -middle_lane,height*0.8
    
    
    #3car
    trophy = pygame.image.load("trophy.png").convert_alpha()
    trophy =pygame.transform.scale(trophy,(100,100)).convert_alpha()
    trophy_loc=trophy.get_rect()
    trophy_loc.center= -middle_lane,height*0.8


    #game start 
    screen.fill(black)
    drawText('Press any key to start the game.', font, screen, (width / 3) - 30, (height / 3))
    drawText('And Enjoy', font, screen, (width / 3), (height / 3)+30)
    pygame.display.update()
    waitForPlayerToPressKey()
    screen.fill(green)
    reward_count=0
    
    
    while running:
        #score
        clock.tick(120)
        if game_done==True:
            secs+=1
        
        if secs==60:
            secs=0
            mins+=1
        if mins==60:
            mins=0
            secs= 0
            hours+=1
        text=font.render("score: {}".format (mins), True,black, green)
        screen.blit(text,(10,10))
        # drawText('trophy %s '%(reward_count),font,screen,10,40,)
        text=font.render("trophy: {}".format(reward_count), True,green,black)
        screen.blit(text,(10,40))
        
        #game_end_logic
        if car_loc[0]==car2_loc[0] and car2_loc[1]>car_loc[1]-250 and game_done :
            if car_loc[1]:
                while True:
                    print("game end")
                    # display_game_over = game_over_font.render("game over",True,red,black)
                    secs=0
                    game_done=False  
                    game_over()
                    pygame.display.flip()
                    break
        
        #reward 
        trophy_spawn()       
        if car_loc.center[1]==trophy_loc.center[1] and car_loc.center[0]==trophy_loc.center[0]:
            print("working")
            trophy.set_alpha(0)
            reward_count+=1
            

        if game_done==True:
            car2_loc[1]+=7
            trophy_loc[1]+=3
        
        if car2_loc[1]> height:
            car2_loc[1]=-200

            random_loc=random.randint(0,2)
            if random_loc==0:
                car2_loc.center = right_lane,-200
            elif random_loc==1:
                car2_loc.center = middle_lane,-200
            elif random_loc==2:
                car2_loc.center = left_lane,-200
        
        #antiquit
        for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                running= False 
            
            if game_done==True:
                if event.type== KEYDOWN:
                    if event.key in [K_a,K_LEFT]:
                        car_loc=car_loc.move([-right_lane/4,0])
                    if event.key in [K_d,K_RIGHT]:
                        car_loc=car_loc.move([right_lane/4,0])
        
        pygame.draw.rect(screen,(50,50,50),(width/2-road_w/2,0,road_w,height))
        pygame.draw.rect(screen,(255,240,60),(width/2+road_w/8-roadmark_w/2,0,roadmark_w,height))
        pygame.draw.rect(screen,(255,240,60),(width/2-road_w/8-roadmark_w/2,0,roadmark_w,height))
        pygame.draw.rect(screen,(255,255,255),(width/2-road_w/2+roadmark_w*2,0,roadmark_w,height))
        pygame.draw.rect(screen,(255,255,255),(width/2+road_w/2-roadmark_w*3,0,roadmark_w,height))
                
        
        screen.blit(car,car_loc)
        screen.blit(car2,car2_loc)
        screen.blit(trophy,trophy_loc)
        if game_done==False:
            t
            game_over()
            game_restart()
            waitForPlayerToPressKey()
        pygame.display.update()


    pygame.quit()
#menu functions
def menu():
    mainClock = pygame.time.Clock()
    pygame.display.set_caption('game base')
    size= width,height= (1200,800)
    screen = pygame.display.set_mode((size),0,32)
    
    #setting font settings
    font = pygame.font.SysFont(None, 30)
    
    """
    A function that can be used to write text on our screen and buttons
    """
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    # A variable to check for the status later
    click = False
    
    # Main container function that holds the buttons and game functions
    def main_menu():
        while True:
    
            screen.fill((30,30,30))
            draw_text('Main Menu', font, (255,255,255), screen, width/2-150/3, height/2-75)
    
            mx, my = pygame.mouse.get_pos()

            #creating buttons
            button_1 = pygame.Rect(width/2-200/2, height/2, 200, 50)
            button_2 = pygame.Rect(width/2-200/2, height/2+70, 200, 50)

            #defining functions when a certain button is pressed
            if button_1.collidepoint((mx, my)):
                if click:
                    game()
            if button_2.collidepoint((mx, my)):
                if click:
                    carselect()
            pygame.draw.rect(screen, (255, 0, 0), button_1)
            pygame.draw.rect(screen, (255, 0, 0), button_2)
    
            #writing text on top of button
            draw_text('PLAY', font, (255,255,255), screen, width/2-270/10, height/2+15)
            draw_text('CAR SELECT', font, (255,255,255), screen, width/2-250/4,height/2+85)


            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            mainClock.tick(60)
    
    """
    This function is called when the "PLAY" button is clicked.
    """
    def game():
        game_main()
        mainClock.tick(60)

    """
    This function is called when the "Car selection" button is clicked.
    """
    def carselect():
        running = True
        while running:
            screen.fill((0,0,0))
    
            draw_text('Car selection', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
        
            pygame.display.update()
            mainClock.tick(60)
    main_menu()
    
menu()
