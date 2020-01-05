from model import Player
from model import Enemy

import pygame


class Game:
    def __init__(self):
        self.player=Player()
        self.enemy_lst=[]
        for i in range(0,10):
            self.enemy_lst.append(Enemy())

        self.running=True

    def run(self):
        pygame.init()
        clock=pygame.time.Clock()

        while self.running:

            clock.tick(60)
            self.draw_board()
            self.handle_events()

        pygame.quit()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.handle_keys()


    def handle_keys(self):

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
             self.player.move_left()
             print("LEFT")
        if keys[pygame.K_RIGHT]:
             self.player.move_right()
             print("RIGHT")
        if keys[pygame.K_UP]:
             self.player.move_up()
             print("UP")
        if keys[pygame.K_DOWN]:
            self.player.move_down()
            print("DOWN")
        
        print(self.player.get_coords())






    def draw_surface(self):
        surface=pygame.display.set_mode((600, 600))
        surface.fill(pygame.Color(255, 255, 255))


    def draw_player(self,player:Player)->None:
        height=player.get_height()
        width=player.get_width()
        x=player.get_x()
        y=player.get_y()

        surface=pygame.display.get_surface()
        pygame.draw.rect(surface,pygame.Color(0, 32, 255),(x, y, width, height))


    def draw_enemy(self,enemy:Enemy)->None:
        surface = pygame.display.get_surface()
        pygame.draw.rect(surface, pygame.Color(202, 0, 42), (10 * enemy.get_x(), 10 * enemy.get_x(), 10, 10))


    def draw_board(self)->None:
        #draws entire board
        surface=pygame.display.get_surface()
        self.draw_surface()
        self.draw_player(self.player)
        for enemy in self.enemy_lst:
            self.draw_enemy(enemy)
        pygame.display.flip()










if __name__=="__main__":
    game=Game()
    game.run()


