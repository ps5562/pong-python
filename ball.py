import pygame


class Ball:
    """
    Represents the ball in the Pong game.
    """
    def __init__(self, x, y):
        self.position = (x, y)
        self.speed_x = 5
        self.speed_y = 5
        self.rect = pygame.Rect(x, y, 20, 20)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Collision with top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1
    
    def reset(self):
        """
        Reset the ball to the center with initial speed and position.
        """
        self.rect.center = (400, 300)
        self.speed_x = 5
        self.speed_y = 5

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
