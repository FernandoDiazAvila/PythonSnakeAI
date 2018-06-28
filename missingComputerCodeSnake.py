from pygame.locals import *
from random import randint
import pygame
import time
 
class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[0] = 1*44
       self.x[0] = 2*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
 
 
class Computer:

    ## ADD CODE WHERE COMMENTS EXPLICITLY ASK :-)
    
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0

     # initializer
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[0] = 1*44
       self.y[0] = 4*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            ## ADD 4 IF STATEMENTS TO UPDATE POSITION
            if self.direction == 0:
                self.x[0]= self.x[0] + self.step
            if self.direction == 1:
                self.x[0]= self.x[0] - self.step
            if self.direction == 2:
                self.y[0]= self.y[0] - self.step
            if self.direction == 3:
                self.y[0]= self.y[0] + self.step
            
 
            ##RESET COUNTER HERE
            self.updateCount=0
 
 
    def moveRight(self):
        self.direction = 0
 
    ## DEFINE MOVE LEFT FUNCTION
    def moveLeft(self):
        self.direction = 1
 
    ## DEFINE MOVE UP FUNCTION
    def moveUp(self):
        self.direction = 2
 
    ## DEFINE MOVE DOWN FUNCTION
    def moveDown(self):
        self.direction = 3
 


    ##FINISH THE TARGET FUNCTION
    ## DX is the X of the APPLE
    ## DY is the Y of the APPLY
    def target(self,dx,dy):

        ## This function moves left if snake is on the right side of the apple
        if self.x[0] > dx:
            self.moveLeft()
 
        ## WHEN SHOULD YOU MOVE RIGHT?
        if self.x[0] < dx:
            self.moveRight()

        ##WHEN SHOULD YOU MOVE DOWN?
        if self.y[0] > dy:
            self.moveUp()

        ## WHEN SHOULD YOU MOVE UP?
        if self.y[0] < dy:
            self.moveDown()
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
 
class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
 
class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
    computer = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(5) 
        self.apple = Apple(8,5)
        ##INITIALIZE COMPUTER HERE
        self.computer = Computer(5)
        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("python-icon-32.png").convert()
        self._apple_surf = pygame.image.load("images.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.computer.target(self.apple.x,self.apple.y)
        self.player.update()
        ## UPDATE COMPUTER HERE
        self.computer.update()

        
        # does snake eat apple?
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.player.length = self.player.length + 1
 
        # does computer eat apple?
        ##CHECK IF COMPUTER EATS APPLE HERE (USE ABOVE FOR LOOP FOR IDEAS)
        for i in range(0,self.computer.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.computer.x[i],self.computer.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.computer.length = self.computer.length + 1

        
        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                print ("You lose! Collision: ")
                print ("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")"  )
                print ("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i])) + ")"  
                exit(0)
 
        pass

        for i in range(2,self.computer.length):
            if self.game.isCollision(self.computer.x[0],self.computer.y[0],self.computer.x[i], self.computer.y[i],40):
                print ("You lose! Collision: ")
                print ("x[0] (" + str(self.computer.x[0]) + "," + str(self.computer.y[0]) + ")"  )
                print ("x[" + str(i) + "] (" + str(self.computer.x[i]) + "," + str(self.computer.y[i])) + ")"  
                exit(0)
 
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        ### DRAW COMPUTER HERE
        self.computer.draw(self._display_surf, self._image_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
 
            time.sleep (50.0 / 1000.0);
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
