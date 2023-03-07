import pygame
from spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Spritesheet('spritesheet_real.png').parse_sprite('robot.png')
        self.rect = self.image.get_rect()
        self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False
        self.position, self.velocity = pygame.math.Vector2(0, 0), pygame.math.Vector2(0, 0)

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.movement()

    def movement(self):
        if self.LEFT_KEY:
            self.position.x -= 50
            self.rect.x = self.position.x

        elif self.RIGHT_KEY:
            self.position.x += 50
            self.rect.x = self.position.x
        elif self.UP_KEY:
            self.position.y -= 50
            self.rect.y = self.position.x
        elif self.DOWN_KEY:
            self.position.y += 50
            self.rect.y = self.position.y
