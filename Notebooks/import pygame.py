import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
width = 400
height = 100
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Welcome Message")

# Set up font and text
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))

# Fill background and draw text
screen.fill((0, 0, 0))  # Black background
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.KEYUP]:
            run = False

# Quit Pygame
pygame.quit()


