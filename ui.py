import pygame


def draw_splash_screen(screen, title_font, font):
    """
    Draw the splash screen with a Pong-themed background and start option.
    """
    # Create a gradient background (dark blue to black)
    for y in range(600):
        color = (0, 0, int(50 * (1 - y / 600)))
        pygame.draw.line(screen, color, (0, y), (800, y))
    
    # Draw some Pong elements for decoration
    pygame.draw.rect(screen, (255, 255, 255), (390, 280, 20, 40))  # Center line segments
    pygame.draw.rect(screen, (255, 255, 255), (390, 340, 20, 40))
    
    # Draw paddles on sides
    pygame.draw.rect(screen, (255, 255, 255), (50, 250, 10, 100))
    pygame.draw.rect(screen, (255, 255, 255), (740, 250, 10, 100))
    
    # Draw ball in center
    pygame.draw.ellipse(screen, (255, 255, 255), (390, 290, 20, 20))
    
    # Title
    title_text = title_font.render("PONG", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(400, 150))
    screen.blit(title_text, title_rect)
    
    # Subtitle
    subtitle_text = font.render("Classic Arcade Game", True, (200, 200, 200))
    subtitle_rect = subtitle_text.get_rect(center=(400, 220))
    screen.blit(subtitle_text, subtitle_rect)
    
    # Start instruction
    start_text = font.render("Press SPACE to Play", True, (255, 255, 0))
    start_rect = start_text.get_rect(center=(400, 500))
    screen.blit(start_text, start_rect)
    
    # Instructions
    instr_text = font.render("Player 1: W/S keys    Player 2: AI", True, (180, 180, 180))
    instr_rect = instr_text.get_rect(center=(400, 550))
    screen.blit(instr_text, instr_rect)


def draw_game_over(screen, font, large_font, game_controller):
    """
    Draw the game over message and restart prompt.
    """
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
    
    restart_text = font.render("Press R to return to menu", True, (200, 200, 200))
    restart_rect = restart_text.get_rect(center=(400, 450))
    screen.blit(restart_text, restart_rect)


def draw_game(screen, ball, player1, player2, game_controller, font, large_font):
    """
    Draw the game state on screen.
    """
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
        draw_game_over(screen, font, large_font, game_controller)
