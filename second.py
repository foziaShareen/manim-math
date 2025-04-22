from manim import *
# https://docs.devtaoism.com/docs/html/contents/_1_basic_elements.html
# https://github.com/HarleyCoops/Math-To-Manim/blob/main/3BouncingBalls/bouncing_balls.py
class SecondScene(Scene):
    def construct(self):
        sq = Square(side_length=2, color=BLUE)
        self.play(Create(sq))
        self.wait(2)
       