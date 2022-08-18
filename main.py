import pygame
from datetime import datetime
from datetime import timedelta
import random


pygame.init()

WHITE=(255,255,255)
RED=(255,0,00)
GREEN=(0,255,0)

size=[400,400]
screen=pygame.display.set_mode(size)

done=False
clock=pygame.time.Clock()
last_moved_time=datetime.now()

KEY_DIRECTION={
    pygame.K_UP:'N',
    pygame.K_DOWN:'S',
    pygame.K_LEFT:'W',
    pygame.K_RIGHT:'E'
}

def draw_block(screen,color,position):
    block=pygame.Rect((position[0]*20,position[1]*20),(20,20))
    pygame.draw.rect(screen,color,block)

class Snake:
    def __init__(self):
        self.positions=[(2,0),(1,0),(0,0)]
        self.direction=''

    def draw(self):
        for position in self.positions:
            draw_block(screen,GREEN,position)

    def move(self):
        head_position=self.positions[0]
        x,y=head_position
        if self.direction=='N':
            self.positions=[(x,y-1)]+self.positions[:-1]
        elif self.direction=='S':
            self.positions=[(x,y+1)]+self.positions[:-1]
        elif self.direction=='W':
            self.positions=[(x-1,y)]+self.positions[:-1]
        elif self.direction=='E':
            self.positions=[(x+1,y)]+self.positions[:-1]
    
    def grow(self):
        tall_position=self.positions[-1]
        x,y=tall_position
        if self.direction=='N':
            self.positions.append((x,y+1))
        elif self.direction=='S':
            self.positions.append((x,y-1))
        elif self.direction=='W':
            self.positions.append((x+1,y))
        elif self.direction=='E':
            self.positions.append((x-1,y))

class Apple:
    def __init__(self,position=(5,5)):
        self.position=position

    def draw(self):
        draw_block(screen,RED,self.position)


def runGame():
    global done,last_moved_time

    snake=Snake()
    apple=Apple()

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type==pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction=KEY_DIRECTION[event.key]


        print(snake.direction)
        if snake.positions[0][0]==-1 and snake.direction=='W':
            done=True
        elif snake.positions[0][0]==20 and snake.direction=='E':
            done=True
        elif snake.positions[0][1]==-1 and snake.direction=='N':
            done=True
        elif snake.positions[0][1]==20 and snake.direction=='S':
            done=True

        if timedelta(seconds=0.5)<=datetime.now()-last_moved_time:
            print(snake.positions[0])
            if snake.positions[0][0]!=apple.position[0]:
                if snake.positions[0][0]-apple.position[0]<0:
                    snake.direction='E'
                else:
                    snake.direction='W'
            elif snake.positions[0][1]!=apple.position[1]:
                if snake.positions[0][1]-apple.position[1]<0:
                    snake.direction='S'
                else:
                    snake.direction='N'
            snake.move()

        snake.draw()
        apple.draw()


        if snake.positions[0]==apple.position:
            snake.grow()
            apple.position=(random.randint(0,19),random.randint(0,19))

        if snake.positions[0] in snake.positions[1:]:
            done=True
        pygame.display.update()

runGame()
pygame.quit()