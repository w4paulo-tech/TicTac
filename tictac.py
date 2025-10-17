import sys
import pygame
from settings import Settings
from button import Button
from textbox import TextBox

class TicTac:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((450, 450))
        pygame.display.set_caption("TicTacToe")
        self.tic_img = pygame.image.load('images/tic.png')
        self.tac_img = pygame.image.load('images/tac.png') 
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.game_active = False
        self.play_button = Button(self, "Pradėti žaist")
        self.quit_button = Button(self, "Baigti žaidimą", 60)
        self.font = pygame.font.SysFont(None, 48)
        self.laimetojas = None
        self.zaidejas = "X"
        self.first_run = True
        # self.winning_line = None
        # self.x_laimejimai = 0
        # self.o_laimejimai = 0
        # self.lygiosios = 0

    def run_game(self):
        while True:
            self._check_events()
            laimetojas = self._check_winner()
            if laimetojas: #and self.laimetojas == None:
                self.laimetojas = laimetojas
                self.game_active = False
                # self._winning_count()
            
            self._update_screen()
            self.clock.tick(60)

    def _game_start(self):
        self.game_active = True
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.laimetojas = None
        # self.winning_line = None
        self.zaidejas = "X"
        self.first_run = False

    # def _winning_count(self):
    #     if not self.first_run:
    #         if self.laimetojas == "X":
    #             self.x_laimejimai += 1
    #         elif self.laimetojas == "O":
    #             self.o_laimejimai += 1
    #         elif self.laimetojas == "Lygiosios":
    #             self.lygiosios += 1

    # def _draw_statistics(self):
    #     stats = (f"X: {self.x_laimejimai}\nO: {self.o_laimejimai}\n"
    #              f"Lygiosios: {self.lygiosios}")
    #     stat_text = TextBox(self, stats, box_x=0, box_y=0)
    #     stat_text.draw()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.game_active:
                    if self.play_button.rect.collidepoint(mouse_pos):
                        self._game_start()
                    elif self.quit_button.rect.collidepoint(mouse_pos):
                        sys.exit()
                else:
                    row, col = mouse_pos[1] // 150, mouse_pos[0] // 150
                    if self.board[row][col] is None:
                        self.board[row][col] = self.zaidejas
                        if self.zaidejas == "X":
                            self.zaidejas = "O" 
                        else:
                            self.zaidejas = "X"
                    
    def _draw_grid(self):            
        pygame.draw.line(self.screen, (0, 0, 0), (150, 0), (150, 450), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (300, 0), (300, 450), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 150), (450, 150), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 300), (450, 300), 3)
    
    def _count_lines(self):
        rows = []
        columns = []
        for r in range(3):
            x = 0
            o = 0
            for c in range(3):
                if self.board[r][c] == "X":
                    x += 1
                elif self.board[r][c] == "O":
                    o += 1
            rows.append((x, o))
        for c in range(3):
            x = 0
            o = 0
            for r in range(3):
                if self.board[r][c] == "X":
                    x += 1
                elif self.board[r][c] == "O":
                    o += 1
            columns.append((x, o))

        # Suskaičiuoja X ir O vienoj įstrižainėj (0, 0)(1, 1)(2, 2)
        is1_x = 0
        is1_o = 0
        for i in range(3):
            if self.board[i][i] == "X":
                is1_x += 1
            elif self.board[i][i] == "O":
                is1_o += 1

        # Suskaičiuoja X ir O priešingoj įstrižainėj (0, 2)(1, 1)(2, 0)
        is2_x = 0
        is2_o = 0
        for i in range(3):
            if self.board[i][2 - i] == "X":
                is2_x += 1
            elif self.board[i][2 - i] == "O":
                is2_o += 1

        diagonals = [(is1_x, is1_o), (is2_x, is2_o)]
        return {"rows": rows, "columns": columns, "diagonals": diagonals}
    
    def _check_winner(self):
        counted = self._count_lines()
        all_lines = counted["rows"] + counted["columns"] + counted["diagonals"]
        for count in all_lines:
            x = count[0]
            o = count[1]
            if x == 3:
                return "X"
            elif o == 3:
                return "O"

        for row in self.board:
            if None in row:    
                return None
        
        return "Lygiosios"

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "X":
                    self.screen.blit(self.tic_img, (col * 150, row * 150))
                elif self.board[row][col] == "O":
                    self.screen.blit(self.tac_img, (col * 150, row * 150))
        
        if self.game_active or not self.first_run:
            self._draw_grid()

        if not self.game_active:
            self.play_button.draw_button()
            self.quit_button.draw_button()
            # self._draw_statistics()
        
        if self.laimetojas != None:
            if self.laimetojas == "Lygiosios":
                msg = ("Lygiosios!")
                text = TextBox(self, msg)
            else:    
                msg = (f"Laimėjo {self.laimetojas} žaidėjas!")
                text = TextBox(self, msg)
            text.draw()
        
        pygame.display.flip()

if __name__ == '__main__':
    tt = TicTac()
    tt.run_game()