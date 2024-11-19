import pygame,random,time
# from PIL import Image
from tkinter import messagebox,Toplevel
pygame.init()

screen_width=1550
screen_height=800 
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("GetPack")
clock=pygame.time.Clock()
# hero_image=Image.open(r"C:\Users\Computer Makah\Pictures\images\hero.png")
hero_surf=pygame.image.load(r"C:\Users\Computer Makah\Pictures\images\hero.png")
fire_surf=pygame.image.load(r"C:\Users\Computer Makah\Pictures\images\fire.png")
heart_surf=pygame.image.load(r"C:\Users\Computer Makah\Pictures\images\heart.png")
class Hero():
    def __init__(self,x,y,surface):
        self.x=x
        self.y=y
        self.y_step=8
        self.x_step=8
        self.rect=surface.get_rect(center=(self.x,self.y))
        self.score=0
        self.hearts=4

    def move_up(self,hero_rect):
        if hero_rect.top>55:
            self.y-=self.y_step
            self.rect.y-=self.y_step
            
        
    def move_down(self,hero_rect):
        if hero_rect.bottom<screen_height-50:
            self.y+=self.y_step
            self.rect.y+=self.y_step

    def move_right(self,hero_rect):
        if hero_rect.right<screen_width:
            self.x+=self.x_step
            self.rect.x+=self.x_step
            
        
    def move_left(self,hero_rect):
        if hero_rect.left>0:
            self.x-=self.x_step
            self.rect.x-=self.x_step

    def check_crash(self):
        for fire in fires_list:
            # check hitting fire from right
            if fire.rect.left<=self.rect.right and fire.rect.right>self.rect.right:
                if fire.rect.top<self.rect.bottom and fire.rect.bottom>self.rect.top:
                    self.hearts-=1
                    fires_list.remove(fire)
            # check hitting fire from bottom
            elif fire.rect.bottom >= self.rect.top and fire.rect.top<self.rect.top and fire.rect.left<self.rect.right and fire.rect.right > self.rect.left:
                    self.hearts-=1
                    fires_list.remove(fire)
            # check hitting fire from top
            elif fire.rect.top <= self.rect.bottom and fire.rect.bottom>self.rect.top and fire.rect.left<self.rect.right and fire.rect.right > self.rect.left:
                    self.hearts-=1
                    fires_list.remove(fire)

    def draw_score(self):
        score=pygame.font.SysFont("Algerian",40).render(f"Score: {int(self.score)}",True,"cyan")
        screen.blit(score,(screen_width-250,10))
                    
    def draw_hearts(self):
        hearts=pygame.font.SysFont("Algerian",40).render(f"Hearts: {self.hearts}",True,"magenta")
        screen.blit(hearts,(50,10))
        red_heart=pygame.image.load(r"C:\Users\Computer Makah\Pictures\images\red_heart.png")
        for i in range(self.hearts):
            screen.blit(red_heart,(250+i*40,15))
    
    def check_get_heart(self):
        if self.hearts<5:
            for heart in hearts_list:
            # check getting heart from right
                if heart.rect.left<=self.rect.right and heart.rect.right>self.rect.right:
                    if heart.rect.top<self.rect.bottom and heart.rect.bottom>self.rect.top:
                        self.hearts+=1
                        hearts_list.remove(heart)
                # check getting heart from bottom
                elif heart.rect.bottom >= self.rect.top and heart.rect.top<self.rect.top and heart.rect.left<self.rect.right and heart.rect.right > self.rect.left:
                        self.hearts+=1
                        hearts_list.remove(heart)
                # check getting heart from top
                elif heart.rect.top <= self.rect.bottom and heart.rect.bottom>self.rect.top and heart.rect.left<self.rect.right and heart.rect.right > self.rect.left:
                        self.hearts+=1
                        hearts_list.remove(heart)


    def Check_GameOver(self):
        if self.hearts==0:
            self.draw_hearts()
            pygame.display.update()
            msg=messagebox.askyesno("Game Over","Do you want to restart the game.")
            if msg :
                self.hearts=4
                self.score=0
                reset_parameters()
            else:
                messagebox.showinfo("Good Luck","We hope you enjoyed our game.")
                quit()
# ***************************************************
class Line():
    def __init__(self,x):
        self.x=x
        self.width=10
        self.color="yellow"
        self.step=2
    def update(self):
            self.x-=5
            pygame.draw.line(screen,self.color,(self.x,0),(self.x,screen_height))
    

# ***************************************************
class Fire():
    def __init__(self,surf,x,step):
        self.surf=surf
        self.x=x
        self.y=random.randint(50,screen_height-50)
        self.step=step
        self.rect=surf.get_rect(topleft=(screen_width,self.y))
    def move(self):
        self.x-=self.step
        self.rect.x-=self.step

# ***************************************************
class Heart():
    def __init__(self,surf,x,step):
        self.surf=surf
        self.x=x
        self.y=random.randint(50,screen_height-50)
        self.step=step
        self.rect=surf.get_rect(topleft=(screen_width,self.y))
    def move(self):
        self.x-=self.step
        self.rect.x-=self.step
        


# ***************************************************
def check_events():
    events=pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()



# ***************************************************
def move_hero(hero):
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hero.move_up(my_hero.rect)

    if keys[pygame.K_DOWN]:
        hero.move_down(my_hero.rect)
    if keys[pygame.K_RIGHT]:
        hero.move_right(my_hero.rect)

    if keys[pygame.K_LEFT]:
        hero.move_left(my_hero.rect)
# ***************************************************

def update_lines():
    global lines_counter

    if lines_counter==10:
        lines_list.append(Line(screen_width))
        lines_counter=0
    else:
        lines_counter+=1
    
    
    for line in lines_list:
        if line.x<0:
            lines_list.remove(line)
        else:
            line.update()

# ***************************************************
def update_fires():

    global fire_counter,increase_fire_speed,fire_step
    if fire_counter==10:
        fires_list.append(Fire(fire_surf,screen_width,fire_step))
        fire_counter=0
    else:
        fire_counter+=1

    for fire in fires_list:
        if increase_fire_speed==100:
            fire_step+=5
            increase_fire_speed=0
        else:
            increase_fire_speed+=0.1
        if fire.rect.x<0:
            fires_list.remove(fire)
        else:
            fire.move()
            screen.blit(fire.surf,fire.rect)
    
# ***************************************************

def update_hearts():

    global heart_counter,heart_step
    if heart_counter==500:
        hearts_list.append(Heart(heart_surf,screen_width,heart_step))
        heart_counter=0
    else:
        heart_counter+=1

    for heart in hearts_list:
        if heart.rect.x<0:
            hearts_list.remove(heart)
        else:
            heart.move()
            screen.blit(heart.surf,heart.rect)
    
           
# ***************************************************
def reset_parameters():
    my_hero=Hero(screen_width/2,screen_height/2,hero_surf)
    lines_list=[]
    fires_list=[]
    hearts_list=[]
    lines_counter=0
    fire_counter=0
    fire_step=12
    increase_fire_speed=0
    heart_counter=0
    heart_step=5

# ***************************************************
# Game Parameters
my_hero=Hero(screen_width/2,screen_height/2,hero_surf)
lines_list=[]
fires_list=[]
hearts_list=[]
lines_counter=0
fire_counter=0
fire_step=10
increase_fire_speed=0
heart_counter=0
heart_step=5
# ***************************************************
# reset_parameters()
img=pygame.image.load(r"C:\Users\Computer Makah\Pictures\images\fantastic.png")
def start_game():
    while True:
        screen.fill("darkblue")
        check_events()
        update_lines()
        # ************************
        pygame.draw.rect(screen,"darkred",(0,50,screen_width,screen_height-100))
        # screen.blit(img,(0,50))
        # ************************
        update_fires()
        update_hearts()
        my_hero.check_crash()
        my_hero.check_get_heart()
        move_hero(my_hero)
        my_hero.draw_score()
        my_hero.draw_hearts()
        my_hero.Check_GameOver()
        screen.blit(hero_surf,my_hero.rect)
        my_hero.score+=1/30
        clock.tick(30)
        pygame.display.update()


start_game()