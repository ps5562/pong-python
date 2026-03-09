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
    font = pygame.font.Font(None, 36)
    large_font = pygame.font.Font(None, 72)

    # Game objects using classes
    ball = Ball(400, 300)
    player1 = Paddle(50, 250)
    player2 = Paddle(740, 250)
    game_controller = GameController()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Only update game state if game is not over
        if not game_controller.is_game_over():
            # Move the ball
            ball.move()

            # Ball collision with paddles
            if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
                ball.speed_x *= -1

            # Check for scoring
            scorer = game_controller.check_score(ball)
            if scorer != 0:
                game_controller.reset_ball(ball)

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
        
        # Draw scores
        score1_text = font.render(str(game_controller.player1_score), True, (255, 255, 255))
        score2_text = font.render(str(game_controller.player2_score), True, (255, 255, 255))
        screen.blit(score1_text, (100, 50))
        screen.blit(score2_text, (700, 50))
        
        # Draw game over message if game is over
        if game_controller.is_game_over():
            game_over_text = large_font.render("Game Over", True, (255, 255, 255))
            game_over_rect = game_over_text.get_rect(center=(400, 250))
            screen.blit(game_over_text, game_over_rect)
            
            winner = game_controller.get_winner()
            if winner == 1:
                winner_text = font.render("Player 1 Won!", True, (255, 255, 255))
            else:
                winner_text = font.render("Player 2 Won!", True, (255, 255, 255))
            winner_rect = winner_text.get_rect(center=(400, 350))
            screen.blit(winner_text, winner_rect)
        
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

# Game Controller class
class GameController:
    """
    Manages game state including score tracking.
    """
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
    
    def check_score(self, ball):
        """
        Check if a point has been scored and return the player who scored.
        Returns 1 if player1 scored, 2 if player2 scored, 0 if no score.
        """
        if ball.rect.left < 0:
            self.player2_score += 1
            return 2
        elif ball.rect.right > 800:
            self.player1_score += 1
            return 1
        return 0
    
    def reset_ball(self, ball):
        """
        Reset the ball to the center of the screen.
        """
        ball.rect.center = (400, 300)
        ball.speed_x = 5
        ball.speed_y = 5
    
    def is_game_over(self):
        """
        Check if the game is over (first to 6 points).
        """
        return self.player1_score >= 6 or self.player2_score >= 6
    
    def get_winner(self):
        """
        Return the winner (1 or 2), or 0 if no winner yet.
        """
        if self.player1_score >= 6:
            return 1
        elif self.player2_score >= 6:
            return 2
        return 0

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