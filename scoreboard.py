from turtle import Turtle
alignment = 'center'
font = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snake_data.txt') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.penup() 
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
         
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}' , align = alignment, font = font)
        
    def increase_score(self):
        self.score += 1     
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_data.txt', 'w') as f:
                f.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
        
   