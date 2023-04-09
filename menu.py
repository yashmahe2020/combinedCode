import pygame
import sys
import main
from video import Video
from constants import WIDTH, HEIGHT, VOLUME, TITLE

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def options(text):

    global VOLUME

    while True:

        music.set_volume(VOLUME / 100)

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = Button(image=None, pos=(640, 100),
                              text_input="OPTIONS", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_TEXT.update(SCREEN)

        TEMP_TEXT = "Volume:{0}%"
        VOLUME_TEXT = get_font(50).render(TEMP_TEXT.format(VOLUME), True, "#d7fcd4")
        VOLUME_RECT = VOLUME_TEXT.get_rect(center=(550, 350))
        SCREEN.blit(VOLUME_TEXT, VOLUME_RECT)

        VOLUME_DOWN = Button(image=pygame.image.load("assets/arrow2.png"), pos=(855, 350),
                           text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        VOLUME_DOWN.update(SCREEN)

        VOLUME_UP = Button(image=pygame.image.load("assets/arrow1.png"), pos=(900, 350),
                              text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        VOLUME_UP.update(SCREEN)

        OPTIONS_BACK = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 600),
                              text_input="BACK", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOLUME_UP.checkForInput(OPTIONS_MOUSE_POS) and VOLUME <= 95:
                    VOLUME += 5
                elif VOLUME_DOWN.checkForInput(OPTIONS_MOUSE_POS) and VOLUME >= 5:
                    VOLUME -= 5
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu(text)

        pygame.display.update()

vid = Video("testVid.mp4")
vid.set_size((WIDTH,HEIGHT))

def intro():
    while True:
        vid.draw(SCREEN, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                main_menu("PLAY")

def main_menu(text):

    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render(TITLE, True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH//2, 100))

        FIRST_BUTTON_TEXT = "assets/{0} Rect.png"
        PLAY_BUTTON = Button(image=pygame.image.load(FIRST_BUTTON_TEXT.format(text)), pos=(WIDTH//2, 250),
                             text_input=text, font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(WIDTH//2, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(WIDTH//2, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main.main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(text)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

pygame.init()

music = pygame.mixer.Sound('assets/music.mp3')
music.play(-1)

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")