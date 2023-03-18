import pygame
from spritesheet import Spritesheet
from tiles import *

class Player(pygame.sprite.Sprite):
    
    moveList = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheet('spritesheet_real.png').parse_sprite('robot.png')
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY, self.ENTER_KEY = False, False, False, False, False
        self.position = pygame.math.Vector2(self.x, self.y)
        
    def listOfMoves(self):
        print("Input moves with the arrow keys. Press enter to confirm your moves.")
        while self.ENTER_KEY == False:
            if self.LEFT_KEY:
                self.moveList.append('LEFT')
            elif self.RIGHT_KEY:
                self.moveList.append('RIGHT')
            elif self.UP_KEY:
                self.moveList.append('UP')
            elif self.DOWN_KEY:
                self.moveList.append('DOWN')
                print(self.moveList)
            elif self.ENTER_KEY:
                return self.moveList

    def draw(self, display):
        display.blit(self.image, (self.rect.x * 50, self.rect.y * 50))

    def update(self):
        self.movement()

    def getX(self):
        return self.x

    def getY(self):
        return self.y    

    def movement(self):
        if self.LEFT_KEY:
            
            if self.rect.x == 0:
                print("out of bounds")
                self.LEFT_KEY = False
            else:
                
                #check collision
                self.rect.x -= 1
                if self.rect.x == 0:
                    self.LEFT_KEY = False

        elif self.RIGHT_KEY:
            if self.rect.x == 15:
                print("out of bounds")
                self.RIGHT_KEY = False
            else:
                self.rect.x += 1
                if self.rect.x == 15:
                    self.RIGHT_KEY = False

        elif self.UP_KEY:
            if self.rect.y == 0:
                print("out of bounds")
                self.UP_KEY = False
            else:
                self.rect.y -= 1
                if self.rect.y == 0:
                    self.LEFT_KEY = False
    
        elif self.DOWN_KEY:
            if self.rect.y == 15:
                print("out of bounds")
                self.DOWN_KEY = False
            else:
                #self.position.y += 50
                self.rect.y += 1
                if self.rect.y == 15:
                    self.DOWN_KEY = False
