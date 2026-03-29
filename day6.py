from manim import *
import numpy as np

class Day6(Scene):
    def construct(self):
        # === PART 1: SETUP AXES AND GRAPH ===
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 2],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE}
        )
        
        # Labels using Text() to avoid LaTeX errors
        x_label = Text("x", font_size=36).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=36).next_to(axes.y_axis, UP)
        title = Text("Day 6: Derivatives & Tangents", font_size=48).to_edge(UP)
        
        # Plot y = 0.5x^2
        graph = axes.plot(lambda x: 0.5 * x**2, color=YELLOW)
        func_label = Text("f(x) = 0.5x²", font_size=36, color=YELLOW).to_edge(RIGHT).shift(UP * 2)
        
        self.play(Write(title), Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph), Write(func_label))
        self.wait(1)

        # === PART 2: VALUE TRACKER (The Magic!) ===
        x_tracker = ValueTracker(-2)
        
        # === PART 3: DYNAMIC TANGENT LINE (Manual Calculation) ===
        # For y = 0.5x², derivative is y' = x (slope = x value)
        # We create a line manually using point-slope form
        def get_tangent_line():
            x_val = x_tracker.get_value()
            y_val = 0.5 * x_val**2  # Point on curve
            slope = x_val  # Derivative of 0.5x² is x
            
            # Create two points for the line (extends in both directions)
            line_length = 2
            x1 = x_val - line_length
            y1 = y_val + slope * (x1 - x_val)
            x2 = x_val + line_length
            y2 = y_val + slope * (x2 - x_val)
            
            line = Line(
                axes.c2p(x1, y1),
                axes.c2p(x2, y2),
                color=GREEN,
                stroke_width=3
            )
            return line
        
        tangent_line = always_redraw(get_tangent_line)
        
        # === PART 4: DYNAMIC POINT ===
        point = always_redraw(lambda: Dot(
            axes.c2p(x_tracker.get_value(), 0.5 * x_tracker.get_value()**2), 
            color=RED
        ))
        
        # === PART 5: SLOPE LABEL ===
        slope_label = always_redraw(lambda: Text(
            f"Slope = {x_tracker.get_value():.2f}", 
            font_size=32, 
            color=GREEN
        ).to_edge(DOWN))
        
        self.add(tangent_line, point, slope_label)
        self.wait(1)

        # === PART 6: ANIMATE THE MOVEMENT ===
        self.play(
            x_tracker.animate.set_value(2),
            run_time=4,
            rate_func=linear
        )
        
        self.wait(2)

        # === PART 7: FINAL MESSAGE ===
        final_text = Text("✨ The Derivative is the Slope! ✨", color=WHITE)
        final_text.scale(1.2)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text))
        self.wait(2)