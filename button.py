import pygame.font

class Button:
    def __init__(self, tt_game, msg, y_pos: int=0):
        self.screen = tt_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 250, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        centerx = self.screen.get_rect().centerx
        centery = self.screen.get_rect().centery
        self.rect.center = (centerx, centery + y_pos)
        self.border_color = (255, 255, 255)
        self.border_width = 3

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_width)
        self.screen.blit(self.msg_image, self.msg_image_rect)