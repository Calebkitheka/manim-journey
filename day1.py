from manim import *

class Day1(Scene):
    def construct(self):
        # 1. Create a Circle object
        circle = Circle()
        
        # 2. Set the color to blue and fill it slightly
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(color=WHITE, width=4)
        
        # 3. Add the circle to the scene
        self.add(circle)
        
        # 4. Create a Text label
        label = Text("My First Manim Shape!")
        label.next_to(circle, DOWN)
        
        # 5. Add the label to the scene
        self.add(label)

        