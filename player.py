import pygame
from spritesheet import Spritesheet
from tiles import *

class Player(pygame.sprite.Sprite):
    moveList = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheet('spritesheet_real.png').parse_sprite('robot.png')
        self.rect = self.image.get_rect()
        self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY, self.ENTER_KEY = False, False, False, False, False
        self.position = pygame.math.Vector2(0, 0)
        
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
            elif self.ENTER_KEY:
                return self.moveList

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.movement()

    def movement(self):
        if self.LEFT_KEY:
            if self.rect.x == 0:
                print("out of bounds")
                self.LEFT_KEY = False
            else:
                self.position.x -= 50
                self.rect.x = self.position.x
                if self.rect.x == 0:
                    self.LEFT_KEY = False

        elif self.RIGHT_KEY:
            if self.rect.x == 750:
                print("out of bounds")
                self.RIGHT_KEY = False
            else:
                self.position.x += 50
                self.rect.x = self.position.x
                if (self.rect.x == 750):
                    self.RIGHT_KEY = False

        elif self.UP_KEY:
            if self.rect.y == 0:
                print("out of bounds")
                self.UP_KEY = False
            else:
                self.position.y -= 50
                self.rect.y = self.position.y
                if self.rect.y == 0:
                    self.LEFT_KEY = False
    
        elif self.DOWN_KEY:
            if self.rect.y == 750:
                print("out of bounds")
                self.DOWN_KEY = False
            else:
                self.position.y += 50
                self.rect.y = self.position.y
                if self.rect.y == 750:
                    self.DOWN_KEY = False
