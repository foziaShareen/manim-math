from manim import *

class FirstScene(Scene):
    def construct(self):
        # self.add(NumberPlane())
        title= Text("Math is fun!",color=DARK_BLUE).shift(RIGHT*3,UP*2)
        self.play(Write(title))
        self.wait(3)
        # self.play(Unwrite(title))
        square=Square(color=BLUE,fill_opacity=0.5).shift(LEFT*2, DOWN*1)
        self.play(Write(square))
        self.wait(2)

    
        
        
        