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
    car3 = pygame.image.load("trophy.png")
    car3 =pygame.transform.scale(car3,(100,100))
    car3_loc=car3.get_rect()
    car3_loc.center= -middle_lane,height*0.8


#game start 
    screen.fill(black)
    drawText('Press any key to start the game.', font, screen, (width / 3) - 30, (height / 3))
    drawText('And Enjoy', font, screen, (width / 3), (height / 3)+30)
    pygame.display.update()
    waitForPlayerToPressKey()
    screen.fill(green)
    
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
        
    #game_end_logic
        if car_loc[0]==car2_loc[0] and car2_loc[1]>car_loc[1]-250 and game_done:
            while True:
                print("game end")
                
                # display_game_over = game_over_font.render("game over",True,red,black)
                secs=0
                game_done=False  
                game_over()
                pygame.display.flip()
                break
            
        if game_done==True:
            car2_loc[1]+=7
            car3_loc[1]+=3
        
        if car2_loc[1]> height:
            car2_loc[1]=-200

            random_loc=random.randint(0,2)
            if random_loc==0:
                car2_loc.center = right_lane,-200
            elif random_loc==1:
                car2_loc.center = middle_lane,-200
            elif random_loc==2:
                car2_loc.center = left_lane,-200


        if car3_loc[1]> height:
            car3_loc[1]=-200
            random_loc=random.randint(0,2)
            if random_loc==0:
                car3_loc.center = left_lane,-200
            elif random_loc==1:
                car3_loc.center = right_lane,-200
            elif random_loc==2:
                car3_loc.center = middle_lane,-200            
        
        #antiquit
        for event in pygame.event.get():
            if event.type == QUIT:
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
        screen.blit(car3,car3_loc)
        if game_done==False:
            t
            game_over()
            game_restart()
            waitForPlayerToPressKey()
        pygame.display.update()


game_main()


pygame.quit()