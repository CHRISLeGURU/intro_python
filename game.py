import Pygame 



pygame.init()

# Définition des constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_JUMP_SPEED = 15

# Définition des classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.change_y = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/platform.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Configuration du jeu
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu de plateforme")
clock = pygame.time.Clock()

# Création des instances
player = Player()
platform = Platform(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Logique du jeu
    player.change_y -= 1
    player.rect.y += player.change_y

    # Collision entre le joueur et la plateforme
    if pygame.sprite.collide_rect(player, platform):
        player.change_y = 0

    # Affichage
    screen.fill((255, 255, 255))
    screen.blit(player.image, player.rect)
    screen.blit(platform.image, platform.rect)
    pygame.display.flip()

    # Limiter la vitesse du jeu
    clock.tick(60)