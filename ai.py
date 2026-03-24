def ai_move(player2, ball):
    """
    Simple AI logic to move the paddle towards the ball.
    """
    if player2.centery < ball.centery and player2.bottom < 600:
        player2.y += 5
    elif player2.centery > ball.centery and player2.top > 0:
        player2.y -= 5
