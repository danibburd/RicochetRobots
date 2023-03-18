import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W - 180 , self.game.DISPLAY_H - 700
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.ai_optionsx, self.ai_optionsy = self.mid_w, self.mid_h + 50
        #self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            ###self.game.display.fill(self.game.BLACK)
            self.game.menu_display.blit(self.game.BLACK, (800,0))
            self.game.draw_text('Pick an option', 20, self.game.DISPLAY_W - 180 , self.game.DISPLAY_H - 750)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("AI Options", 20, self.ai_optionsx, self.ai_optionsy)
            #self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.ai_optionsx + self.offset, self.ai_optionsy)
                self.state = 'AI Options'
            elif self.state == 'AI Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.ai_optionsx + self.offset, self.ai_optionsy)
                self.state = 'AI Options'
            elif self.state == 'AI Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'AI Options':
                self.game.curr_menu = self.game.ai_options
            self.run_display = False

class AI_OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'DFS'
        self.dfsx, self.dfsy = self.mid_w, self.mid_h + 20
        self.bfsx, self.bfsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.dfsx + self.offset, self.dfsy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            ####self.game.display.fill((0, 0, 0))
            self.game.draw_text('AI Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("DFS", 15, self.dfsx, self.dfsy)
            self.game.draw_text("BFS", 15, self.bfsx, self.bfsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'DFS':
                self.state = 'BFS'
                self.cursor_rect.midtop = (self.bfsx + self.offset, self.bfsy)
            elif self.state == 'BFS':
                self.state = 'DFS'
                self.cursor_rect.midtop = (self.dfsx + self.offset, self.dfsy)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass