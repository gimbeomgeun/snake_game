import pygame
from datetime import datetime
from datetime import timedelta
import random


pygame.init()

WHITE=(255,255,255)
RED=(255,0,00)
GREEN=(0,255,0)
BLUE=(0,0,255)

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
        draw_block(screen,BLUE,self.positions[0])
        for position in self.positions[1:]:
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
        clock.tick(100)
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
            check=False
            while(check==False):
                print(snake.direction)
                check=True
                if snake.direction=='N':
                    if (snake.positions[0][0],snake.positions[0][1]-1) in snake.positions or snake.positions[0][1]==0:
                        plus_x=30
                        minus_x=30
                        for i in range(snake.positions[0][0]+1,20):
                            if (i,snake.positions[0][1]) in snake.positions:
                                plus_x=i-snake.positions[0][0]
                                break
                        for i in range(snake.positions[0][0]-1,-1,-1):
                            if (i,snake.positions[0][1]) in snake.positions:
                                minus_x=snake.positions[0][0]-i
                                break
                        if plus_x>minus_x:
                            snake.direction='E'
                        else:
                            snake.direction='W'

                        if snake.positions[0][0]==0 and (snake.positions[0][0]-1,snake.positions[0][1]) in snake.positions:
                            snake.direction='E'
                        check=False
                if snake.direction=='S':
                    if (snake.positions[0][0],snake.positions[0][1]+1) in snake.positions or snake.positions[0][1]==19:
                        plus_x=30
                        minus_x=30
                        for i in range(snake.positions[0][0]+1,20):
                            if (i,snake.positions[0][1]) in snake.positions:
                                plus_x=i-snake.positions[0][0]
                                break
                        for i in range(snake.positions[0][0]-1,-1,-1):
                            if (i,snake.positions[0][1]) in snake.positions:
                                minus_x=snake.positions[0][0]-i
                                break
                        if plus_x>minus_x:
                            snake.direction='E'
                        else:
                            snake.direction='W'
                        if snake.positions[0][0]==19 or (snake.positions[0][0]+1,snake.positions[0][1]) in snake.positions:
                            snake.direction='W'
                        check=False
                if snake.direction=='W':
                    if (snake.positions[0][0]-1,snake.positions[0][1]) in snake.positions or snake.positions[0][0]==0:
                        plus_y=30
                        minus_y=30
                        for i in range(snake.positions[0][1]+1,20):
                            if (snake.positions[0][0],i) in snake.positions:
                                plus_y=i-snake.positions[0][1]
                                break
                        for i in range(snake.positions[0][1]-1,-1,-1):
                            if (snake.positions[0][0],i) in snake.positions:
                                minus_y=snake.positions[0][1]-i
                                break
                        if plus_y>minus_y:
                            snake.direction='S'
                        else:
                            snake.direction='N'
                        if snake.positions[0][1]==0 or (snake.positions[0][0],snake.positions[0][1]-1) in snake.positions:
                            snake.direction='S'
                        check=False
                if snake.direction=='E':
                    if (snake.positions[0][0]+1,snake.positions[0][1]) in snake.positions or snake.positions[0][0]==19:
                        plus_y=30
                        minus_y=30
                        for i in range(snake.positions[0][1]+1,20):
                            if (snake.positions[0][0],i) in snake.positions:
                                plus_y=i-snake.positions[0][1]
                                break
                        for i in range(snake.positions[0][1]-1,-1,-1):
                            if (snake.positions[0][0],i) in snake.positions:
                                minus_y=snake.positions[0][1]-i
                                break
                        if plus_y>minus_y:
                            snake.direction='S'
                        else:
                            snake.direction='N'
                        if snake.positions[0][1]==19 or (snake.positions[0][0],snake.positions[0][1]+1) in snake.positions:
                            snake.direction='N'
                        check=False
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