# Simple Pong game with AI using pygame
import pygame
import sys
from ball import Ball
from paddle import Paddle
from game_controller import GameController
from ai import ai_move
from ui import draw_splash_screen, draw_game


def main():
    """
    Main game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    large_font = pygame.font.Font(None, 72)
    title_font = pygame.font.Font(None, 100)

    # Initialize game objects
    game_state = "splash"  # splash or playing
    game_mode = "ai"  # "ai" by default"
    ball = Ball(400, 300)
    player1 = Paddle(50, 250)
    player2 = Paddle(740, 250)
    game_controller = GameController()

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_state == "splash":
                    if event.key == pygame.K_1:
                        game_mode = "ai"
                    elif event.key == pygame.K_2:
                        game_mode = "2player"
                    elif event.key == pygame.K_SPACE:
                        game_state = "playing"
                        game_controller.reset_game()
                        ball.reset()
                elif game_state == "playing":
                    if game_controller.is_game_over() and event.key == pygame.K_r:
                        game_state = "splash"
                        game_mode = None
                    elif event.key == pygame.K_ESCAPE:
                        game_state = "splash"
                        game_mode = None

        # Update and render
        if game_state == "splash":
            screen.fill((0, 0, 0))
            draw_splash_screen(screen, title_font, font, game_mode=game_mode)
        elif game_state == "playing":
            if not game_controller.is_game_over():
                ball.move()
                
                if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
                    ball.speed_x *= -1

                if game_controller.check_score(ball) != 0:
                    game_controller.reset_ball(ball)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    player1.move("up")
                if keys[pygame.K_s]:
                    player1.move("down")

                # Player 2 control depends on game mode
                if game_mode == "ai":
                    ai_move(player2.rect, ball.rect)
                else:  # 2player
                    if keys[pygame.K_UP]:
                        player2.move("up")
                    if keys[pygame.K_DOWN]:
                        player2.move("down")

            draw_game(screen, ball, player1, player2, game_controller, font, large_font)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()