from manim import *

class Day4(Scene):
    def construct(self):
        # === CREATE OBJECTS ===
        circle = Circle(radius=1, color=BLUE, fill_opacity=0.5)
        square = Square(side_length=2, color=RED, fill_opacity=0.5)
        triangle = Triangle().scale(1.5).set_color(GREEN).set_fill(opacity=0.5)
        
        # Arrange them initially
        circle.move_to(LEFT * 3)      # Start far left
        square.move_to(ORIGIN)        # Start center
        triangle.move_to(RIGHT * 3)   # Start far right
        
        title = Text("Day 4: Movement & Timing", font_size=48)
        title.to_edge(UP)
        
        self.add(title, circle, square, triangle)
        self.wait(1)

        # === ANIMATION 1: Basic Movement with .animate ===
        # Move circle to center, square to right, triangle to left
        self.play(
            circle.animate.move_to(ORIGIN),
            square.animate.move_to(RIGHT * 2),
            triangle.animate.move_to(LEFT * 2),
            run_time=2  # Takes 2 seconds
        )
        self.wait(0.5)

        # === ANIMATION 2: Chaining Properties (Color + Position) ===
        # Change square color AND move it up at the same time
        self.play(
            square.animate.set_color(YELLOW).shift(UP * 2),
            run_time=1.5
        )
        self.wait(0.5)

        # === ANIMATION 3: Rotation and Scaling ===
        # Spin the triangle while making it bigger
        self.play(
            triangle.animate.rotate(PI).scale(1.5), # PI radians = 180 degrees
            run_time=2
        )
        self.wait(0.5)

        # === ANIMATION 4: Sequential vs Simultaneous ===
        # Do things one after another (Sequential)
        self.play(circle.animate.set_color(RED), run_time=1)
        self.play(square.animate.set_color(BLUE), run_time=1)
        self.play(triangle.animate.set_color(PURPLE), run_time=1)
        
        self.wait(1)

        # === ANIMATION 5: The "Wait" Trap ===
        # Notice how wait() pauses everything, but play() runs animations
        final_text = Text("Movement is Key!", color=WHITE)
        final_text.scale(1.5)
        final_text.to_edge(DOWN)
        
        # Fade in while moving up slightly
        self.play(
            Write(final_text),
            final_text.animate.shift(UP * 0.5),
            run_time=2
        )
        
        self.wait(2)