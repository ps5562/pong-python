import pygame


class Paddle:
    """
    Represents a paddle in the Pong game.
    """
    def __init__(self, x, y):
        self.position = (x, y)
        self.speed = 5
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, direction):
        if direction == "up" and self.rect.top > 0:
            self.rect.y -= self.speed
        elif direction == "down" and self.rect.bottom < 600:
            self.rect.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
