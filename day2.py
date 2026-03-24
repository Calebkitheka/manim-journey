from manim import *

class Day2(Scene):
    def construct(self):
        # === CREATE SHAPES ===
        circle = Circle(radius=1)
        square = Square(side_length=2)
        triangle = Triangle().scale(1.5)  # Make it bigger
        
        # === STYLE WITH COLORS ===
        circle.set_fill(BLUE, opacity=0.6)
        circle.set_stroke(color=WHITE, width=3)
        
        square.set_fill(RED, opacity=0.6)
        square.set_stroke(color=YELLOW, width=3)
        
        triangle.set_fill(GREEN, opacity=0.6)
        triangle.set_stroke(color=PURPLE, width=3)
        
        # === POSITION USING CODE ===
        # Start with circle in center
        circle.move_to(ORIGIN)  # (0,0) - the center of the screen
        
        # Place square to the RIGHT of circle
        square.next_to(circle, RIGHT, buff=1)  # buff = space between
        
        # Place triangle to the RIGHT of square
        triangle.next_to(square, RIGHT, buff=1)
        
        # === ADD TO SCENE ===
        self.add(circle, square, triangle)
        
        # === ADD A TITLE ===
        title = Text("Day 2: Colors & Positioning", font_size=36)
        title.to_edge(UP)  # Move to top edge of screen
        self.add(title)