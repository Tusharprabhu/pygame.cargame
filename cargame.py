import pygame
from pygame.locals import *
import random
import sys
import time


pygame.init()

size= width,height= (1200,800)
car = pygame.image.load("images/car.png")
car1 = pygame.image.load("images/car1.png")
car2= pygame.image.load("images/car2.png")
screen=pygame.display.set_mode(size,RESIZABLE)
class Button :
    
    def __init__(self,CARS, x, y):
        self.img=CARS
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)
        self.clicked= False
    def draw(self):
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed ()[0]and not self.clicked:
                self.clicked=True
                game_main(self.img)

            if not pygame.mouse.get_pressed()[0]:
                self.clicked=False
        screen.blit (self.img, (self.rect.x, self.rect.y))
def game_main(l):
    mainClock = pygame.time.Clock()
    size= width,height= (1200,800)
    road_w= int(width/1.5)
    roadmark_w= int(width/80)
    t=time.sleep(0.5)

    red= (255,0,0)
    TEXTCOLOR = (255, 255, 255)
    black= (0,0,0)
    green=(60,220,0)
    white = (255,255,255)
    font=pygame.font.Font ('freesansbold.ttf', 32)


    screen=pygame.display.set_mode(size,RESIZABLE)
    pygame.display.set_caption("tushar's car game")

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

    def drawText(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    #game start #screen color
    screen.fill(black)
    drawText('Press any key to start the game.', font, screen, (width / 3) - 30, (height / 3))
    drawText('And Enjoy', font, screen, (width / 3), (height / 3)+30)
    pygame.display.update()
    waitForPlayerToPressKey()
    screen.fill(green)
    reward_count=0
    screen.fill(green)
    
    secs=0
    mins=0
    hours=0
    game_done=True
    # text=font.render("{}".format (mins), True, (255, 255, 255), (0, 0, 0))


    right_lane= width/2+road_w/4
    left_lane= width/2-road_w/4
    middle_lane= width/2 

    
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
                        game_main(l)
                    return
    clock = pygame.time.Clock()

    running = True


    pygame.display.update()
    
    
    #1car
    car = l
    car_loc=car.get_rect()
    car_loc.center= middle_lane,height*0.8
    
    
    #2car
    car2 = pygame.image.load("images/othercar.png")
    car2_loc=car2.get_rect()
    car2_loc.center= -middle_lane,height*0.8
    
    
    #3car
    trophy = pygame.image.load("images/trophy.png").convert_alpha()
    trophy =pygame.transform.scale(trophy,(100,100)).convert_alpha()
    trophy_loc=trophy.get_rect()
    trophy_loc.center= -middle_lane,height*0.8



    
    
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
                    mainClock.tick(30)
                    pygame.display.flip()
                    break
        
        #reward 
        trophy_spawn()       
        if car_loc[1]==trophy_loc[1] and car_loc.center[0]==trophy_loc.center[0]:
            print("trophy count:",reward_count)
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
    screen = pygame.display.set_mode((size))
    
    #setting font settings
    font = pygame.font.SysFont(None, 30)
    

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    

    def main_menu():
        while True:
    
            screen.fill((30,30,30))
            draw_text('Main Menu', font, (255,255,255), screen, width/2-150/3, height/2-75)
    
            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(width/2-200/2, height/2, 200, 50)
            button_2 = pygame.Rect(width/2-200/2, height/2+70, 200, 50)

            if button_1.collidepoint((mx, my)):
                if click:
                    game()
            if button_2.collidepoint((mx, my)):
                if click:
                    carselect()
            pygame.draw.rect(screen, (255, 0, 0), button_1)
            pygame.draw.rect(screen, (255, 0, 0), button_2)
    
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
            mainClock.tick(30)
    

    def game():
        game_main(l= pygame.image.load("images/car.png"))
        mainClock.tick(30)


    def carselect():
  
        running = True
        car = pygame.image.load("images/car.png")
        car1 = pygame.image.load("images/car1.png")
        car2= pygame.image.load("images/car2.png")
        b=Button(car,150,250)
        u=Button(car1,450,250)
        l=Button(car2,750,250)

        while running:
            screen.fill((0,0,0))
            b.draw()
            u.draw()
            l.draw()
            draw_text('Car selection', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
        
            pygame.display.update()
            mainClock.tick(30)
    main_menu()
    

menu()
