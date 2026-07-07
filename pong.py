import pygame,sys
import random
pygame.init()

screen_width = 800
screen_height = 600

Black = (0,0,0)

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("my screen")

clock = pygame.time.Clock()

score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 50)
class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.speed = 5
        self.radius = 10
        
    
    def start(self):
        self.vx = self.speed
        self.vy = self.speed

    def update(self):
        self.x += self.vx
        self.y += self.vy
        
    
    





    def check(self):
        if self.x-self.radius <= paddle_1.x+10 and self.y>=paddle_1.y and self.y<=paddle_1.y+60:
            self.vx = -self.vx
        
        if self.x+self.radius >= paddle_2.x  and self.y >= paddle_2.y and self.y <= paddle_2.y+60:
            self.vx = -self.vx 
        
    




    def boundry(self):
        
        if self.y-self.radius<=0:
            self.y = self.radius
            self.vy = -self.vy
        if self.y+self.radius>=600:
            self.y = 600 - self.radius
            self.vy = -self.vy
        
    
    def reset(self):
        self.x = 400
        self.y = 300


    def draw(self):
        pygame.draw.circle(screen,(255,255,255),(self.x,self.y),self.radius)
    
    def score(self):
        global score1,score2

        if self.x < 0:
            score2+=1
            self.reset()
        if self.x > 800:
            score1+=1
            self.reset()
    
    






class Box:
    def __init__(self,x,y):
        self.direction  = "" 
        self.width = 10
        self.height = 60 
    
        self.speed = 5
        self.x = x
        self.y = y
    def move_up(self):
        self.y-= self.speed 
        
    def move_down(self):
        self.y+=self.speed
        
    def update(self): 
        if self.direction == "UP":
            self.move_up()
        if self.direction =="down":
            self.move_down()
        
    def boundary(self):
        if self.y<=0:
            self.y = 0
        if self.y+60>=600:
            self.y = 600-60 
        
    def draw(self):
        pygame.draw.rect(screen,(255,0,0),(self.x,self.y,self.width,self.height))
        

#object 
paddle_1 = Box(0,240)
paddle_2 = Box(790,240)
ball = Ball(400,300)
ball.start()

#loop
while True:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
    # updating key
    paddle_1.direction = None
    paddle_2.direction = None
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_1.direction = "UP"
        
    if keys[pygame.K_s]:
        paddle_1.direction = "down"
        

    if keys[pygame.K_UP]:
        paddle_2.direction = "UP"
    if keys[pygame.K_DOWN]:
        paddle_2.direction = "down"


    
    ball.update()
    ball.check()
    ball.boundry()
    ball.score()
    paddle_1.update()
    paddle_2.update()
    paddle_1.boundary()
    paddle_2.boundary()
    
    score1_text = font.render(f"{score1}", True, (255,255,255))
    score2_text = font.render(f"{score2}", True, (255,255,255))
    
    # winning conditon 
    if score1 == 10 and score1 > score2:
        print("player 1 wins")
        break
    if score2 ==  10 and score2 > score1:
        break
        print("player 2 wins")

    #drawing
    screen.fill(Black)
    pygame.draw.line(screen,(255,255,255),(398,0),(398,600),1)
    paddle_1.draw()
    paddle_2.draw()
    ball.draw()
    screen.blit(score1_text, (200, 20))   # left side
    screen.blit(score2_text, (550, 20))   # right side




    pygame.display.flip()
    clock.tick(60)