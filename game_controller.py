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
    
    def reset_game(self):
        """
        Reset the game scores to start a new game.
        """
        self.player1_score = 0
        self.player2_score = 0
