from tiles import *
from spritesheet import Spritesheet
from player import Player
from board import Board
from game import Game

g = Game()
clock = pygame.time.Clock()

################################# LOAD PLAYER AND SPRITESHEET###################################
spritesheet = Spritesheet('spritesheet_real.png')
player = Player(0,0)

#################################### LOAD THE LEVEL #######################################
map = TileMap('tile_map_csv_all_walls_Floor.csv', spritesheet )
gameBoard = Board('tile_map_csv_all_walls_Floor.csv')

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
# ################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
# pygame.init()
# DISPLAY_W, DISPLAY_H = 1200, 800
# canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
# window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
# running = True
# clock = pygame.time.Clock()

# ################################# LOAD PLAYER AND SPRITESHEET###################################
# spritesheet = Spritesheet('spritesheet_real.png')
# player = Player(0,0)

# #################################### LOAD THE LEVEL #######################################
# map = TileMap('tile_map_csv_all_walls_Floor.csv', spritesheet )
# gameBoard = Board('tile_map_csv_all_walls_Floor.csv')
# #player.position.x, player.position.y = 100, 100


# ############################### GAME LOGIC STUFF #################################
# # def checkDirection(dir, x, y):
# #     if dir == "W":    
# #         if x == 0 | gameBoard.getTile(x-1,y) != 1:
# #             print("out of bounds")
# #             return
# #         else:
# #             checkCollision(gameBoard, True, True, x, y)

# #     elif dir == "E":
# #         if x == 15 | gameBoard.getTile(x+1,y) != 1:
# #             print("out of bounds")
# #             return
# #         else:
# #             return checkCollision(gameBoard, True, False, x, y)

# #     elif dir == "N":
# #         if y == 0 | gameBoard.getTile(x,y-1) != 2:
# #             print("out of bounds")
# #             return
# #         else:
# #             return checkCollision(gameBoard, False, True, x, y)

# #     elif dir == "S":
# #         if y == 15 | gameBoard.getTile(x,y+1) != 2:
# #             print("out of bounds")
# #             return
# #         else:
# #             return checkCollision(gameBoard, False, False, x, y)

# def checkCollision(gameBoard, isRow, isLeft, x, y):
#         if(isRow):
#             pos = x
#             line = gameBoard.getRow(y)
#         else:
#             pos = y
#             line = gameBoard.getCol(x)
        
#         amt = 0
#         if(isLeft):
#             while(pos >= 0):
#                 if (pos != 0 or line[pos-1] == 0):
#                     pos -= 1
#                 else:
#                     return amt
#         else:
#             len = line.length
#             while(pos <= len):
#                 if (pos != len or line[pos] == 0):
#                     pos += 1
#                     amt+=1
#                 else:
#                     return amt


# ################################# GAME LOOP ##########################
# pygame.key.set_repeat()
# while running:
#     clock.tick(8)

#     #print("hello")
#     ################################# CHECK PLAYER INPUT #################################
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 player.LEFT_KEY = True
#             elif event.key == pygame.K_RIGHT:
#                 player.RIGHT_KEY = True
#             elif event.key == pygame.K_UP:
#                 player.UP_KEY = True
#             elif event.key == pygame.K_DOWN:
#                 player.DOWN_KEY = True



#     ################################# UPDATE/ Animate SPRITE #################################
#     nextMove = "N"
#     ####amountMoves = checkDirection(nextMove, player.getX, player.getY)
#     #get next move
#     #check amount of steps in that move
#     #move player that amount of steps
#     #remove move
#     player.update()
#     ################################# UPDATE WINDOW AND DISPLAY #################################
#     map.draw_map(canvas)
#     player.draw(canvas)
#     window.blit(canvas, (0,0))
#     pygame.display.update()

