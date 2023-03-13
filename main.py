from tiles import *
from spritesheet import Spritesheet
from player import Player

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 800, 800
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()

################################# LOAD PLAYER AND SPRITESHEET###################################
spritesheet = Spritesheet('spritesheet_real.png')
player = Player()

#################################### LOAD THE LEVEL #######################################
map = TileMap('tile_map_csv_all_walls_Floor.csv', spritesheet )
player.position.x, player.position.y = map.start_x, map.start_y

################################# GAME LOOP ##########################
pygame.key.set_repeat()
while running:
    clock.tick(8)
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = True
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = True
            elif event.key == pygame.K_UP:
                player.UP_KEY = True
            elif event.key == pygame.K_DOWN:
                player.DOWN_KEY = True



    ################################# UPDATE/ Animate SPRITE #################################
    player.update()
    ################################# UPDATE WINDOW AND DISPLAY #################################
    map.draw_map(canvas)
    player.draw(canvas)
    window.blit(canvas, (0,0))
    pygame.display.update()
