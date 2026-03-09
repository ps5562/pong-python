# Simple Pong game with AI using pygame
import pygame
import sys

def main():
    """
    Basic Pong game with one human player and one simpple AI player.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Game objects using classes
    ball = Ball(400, 300)
    player1 = Paddle(50, 250)
    player2 = Paddle(740, 250)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the ball
        ball.move()

        # Ball collision with paddles
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            ball.speed_x *= -1

        # Move player1 (human)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.move("up")
        if keys[pygame.K_s]:
            player1.move("down")

        # Move player2 (AI)
        ai_move(player2.rect, ball.rect)

        # Draw everything
        screen.fill((0, 0, 0))
        player1.draw(screen)
        player2.draw(screen)
        ball.draw(screen)
        pygame.display.flip()
        clock.tick(60)

# Simple AI movement logic for player2
def ai_move(player2, ball):
    """
    Simple AI logic to move the paddle towards the ball.
    """
    if player2.centery < ball.centery and player2.bottom < 600:
        player2.y += 5
    elif player2.centery > ball.centery and player2.top > 0:
        player2.y -= 5

# Paddle class
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

# Ball class
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

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)


if __name__ == "__main__":
    main()