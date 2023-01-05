import pygame
from pygame.locals import *
import random

pygame.init()
def game_main():
    size= width,height= (600,600)
    road_w= int(width/1.6)
    roadmark_w= int(width/80)

    red= (255,0,0)
    black= (0,0,0)
    white = (255,255,255)


    window=pygame.display.set_mode ( (500, 500))
    done=False
    secs=0
    mins=0
    hours=0
    game_done=True
    font=pygame.font.Font ('freesansbold.ttf', 32)
    text=font.render("{}:{}:{}".format (hours, mins, secs), True, (255, 255, 255), (0, 0, 0))


    right_lane= width/2+road_w/4
    left_lane= width/2-road_w/4

    def game_over():
        display_game_over= game_over_font.render("game over",True,red,black)
        screen.blit(display_game_over,(70,300))

    

    def game_restart():
        game_restart_font = pygame.font.Font('freesansbold.ttf',100)
        display_game_over= game_restart_font.render("game over",True,black,white)
        screen.blit(display_game_over,(70,300))
        
    clock = pygame.time.Clock()


    # font = pygame.font.Font('freesansbold.ttf',20)
    game_over_font = pygame.font.Font('freesansbold.ttf',60)



    running = True
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("tushar's car game")
    #screen color
    screen.fill((60,220,0))

    pygame.display.update()
    #1car
    car = pygame.image.load("car.png")
    car= pygame.transform.scale(car,(100,150))
    car_loc=car.get_rect()
    car_loc.center= right_lane,height*0.8
    #2car
    car2 = pygame.image.load("otherCar.png")
    car2_loc=car2.get_rect()
    car2_loc.center= left_lane,height*0.2
    while running:
        #score
        clock.tick(120)
        if game_done==True:
            secs+=1
        window.blit(text,(10,10))
        if secs==60:
            secs=0
            mins+=1
        if mins==60:
            mins=0
            secs= 0
            hours+=1
        text=font.render("{}:{}:{}".format (hours, mins, secs), True, white, black)
        
    #game_end_logic
        if car_loc[0]==car2_loc[0] and car2_loc[1]>car_loc[1]-250 and game_done:
            while True:
                print("game end")
                display_game_over = game_over_font.render("game over",True,red,black)
                secs=0
                game_done=False  
                game_over()
                pygame.display.flip()
                break
            
        if game_done==True:
            car2_loc[1]+=4
        
        if car2_loc[1]> height:
            car2_loc[1]=-200
            if random.randint(0,1)==0:
                car2_loc.center = right_lane,-200
            else :
                car2_loc.center = left_lane,-200

        #antiquit
        for event in pygame.event.get():
            if event.type == QUIT:
                running= False 
            
            if game_done==True:
                if event.type== KEYDOWN:
                    if event.key in [K_a,K_LEFT]:
                        car_loc=car_loc.move([-int(road_w/2),0])
                    if event.key in [K_d,K_RIGHT]:
                        car_loc=car_loc.move([int(road_w/2),0])
        
        pygame.draw.rect(screen,(50,50,50),(width/2-road_w/2,0,road_w,height))
        pygame.draw.rect(screen,(255,240,60),(width/2-roadmark_w/2,0,roadmark_w,height))
        pygame.draw.rect(screen,(255,240,60),(width/2-roadmark_w/2,0,roadmark_w,height))
        pygame.draw.rect(screen,(255,255,255),(width/2-road_w/2+roadmark_w*2,0,roadmark_w,height))
        pygame.draw.rect(screen,(255,255,255),(width/2+road_w/2-roadmark_w*3,0,roadmark_w,height))
                
        
        screen.blit(car,car_loc)
        screen.blit(car2,car2_loc)
        if game_done==False:
            game_over()
            game_restart()
        pygame.display.update()

game_main()



pygame.quit()