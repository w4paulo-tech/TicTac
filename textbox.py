import pygame.font

class TextBox:
    def __init__(self, tt_game, msg, bg_color=(0, 135, 0), 
                 text_color=(255, 255, 255), box_x=20, box_y=10):
        self.screen = tt_game.screen
        self.font = pygame.font.SysFont(None, 48)
        self.play_button = tt_game.play_button
        self.bg_color = bg_color
        self.text_color = text_color

        self.text_surf = self.font.render(msg, True, self.text_color, self.bg_color)
        self.text_rect = self.text_surf.get_rect(center=self.screen.get_rect().center)
        self.text_rect.centerx = self.play_button.rect.centerx
        self.text_rect.bottom = self.play_button.rect.top - 20
        self.box_x = box_x
        self.box_y = box_y
        self.box_rect = self.text_rect.inflate(box_x * 2, box_y * 2)

    def draw(self):   
        pygame.draw.rect(self.screen, self.bg_color, self.box_rect)
        pygame.draw.rect(self.screen, self.text_color, self.box_rect, 2)
        self.screen.blit(self.text_surf, self.text_rect)
