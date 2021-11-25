#rendering
#basick looping
#display object
#display images
#implement object oriented to the code
#introduce classes and objects into our code
#create game object class

#implemet player caracter class
#implement movement

import pygame

#MENGATUR UKURAN LAYAR
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Cross The Road'

clock = pygame.time.Clock()

#MENGATUR WARNA BACKGROUND (RGB CODE)
WHITE_COLOR = (255, 255, 255)
BALCK_COLOR = (0, 0, 0)

class Game:
    TICK_RATE = 60

    def __init__(self, title,width,height ):  #constucture
        self.title = title
        self.width = width
        self.height = height

        # MENAMPILKAN SCREEN
        game_screen = pygame.display.set_mode((width, height))
        game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        player_character = PlayerCharacter('asset/pemain.png', 375, 700, 50, 50)

        while not is_game_over:

            for event in pygame.event.get():  # perulangan
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            pygame.display.update()
            clock.tick(self.TICK_RATE)

class GameObject:
    def __init__(self, image_path, x, y, width, height):
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

        object_image = pygame.image.load(image_path)
        self.image =pygame.transform.scale(object_image,(width, height))

    def draw(self, background):
        background.blit(self.image, (self.x_pos,self.y_pos))

class PlayerCharacter(GameObject):
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

pygame.init()
new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()


#keluar dari program
pygame.quit()
quit()




#pygame.draw.rect(game_screen, BALCK_COLOR, [350,350,100,100])
    #pygame.draw.circle(game_screen, BALCK_COLOR, (400,300),50)

