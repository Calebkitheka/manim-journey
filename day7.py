from manim import *

class Day7(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("The Pythagorean Theorem", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === FORMULA ===
        formula = Text("a² + b² = c²", font_size=44, color=WHITE)
        formula.next_to(title, DOWN)
        self.play(Write(formula))
        self.wait(1)

        # === CREATE RIGHT TRIANGLE ===
        # Sides: a=3, b=4, c=5 (classic Pythagorean triple)
        a_side = 3
        b_side = 4
        
        # Create the triangle using Polygon
        triangle = Polygon(
            ORIGIN,                    # Bottom-left corner
            [b_side, 0, 0],           # Bottom-right (side b)
            [0, a_side, 0],           # Top-left (side a)
            color=WHITE,
            stroke_width=3
        )
        
        # Label the sides
        label_a = Text("a", font_size=32, color=BLUE).next_to(triangle, LEFT, buff=0.3)
        label_b = Text("b", font_size=32, color=GREEN).next_to(triangle, DOWN, buff=0.3)
        label_c = Text("c", font_size=32, color=RED).shift(UP * 1.5 + RIGHT * 2)
        
        # Right angle marker
        right_angle = Polygon(
            ORIGIN,
            [0.5, 0, 0],
            [0.5, 0.5, 0],
            [0, 0.5, 0],
            color=WHITE,
            fill_opacity=0
        )
        
        self.play(Create(triangle), Create(right_angle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        # === CREATE SQUARES ON EACH SIDE ===
        # Square on side a (blue)
        square_a = Square(side_length=a_side, color=BLUE, fill_opacity=0.3)
        square_a.set_stroke(color=BLUE, width=3)
        square_a.next_to(triangle, LEFT, buff=0, aligned_edge=DOWN)
        square_a_label = Text("a²", font_size=32, color=BLUE).move_to(square_a)
        
        # Square on side b (green)
        square_b = Square(side_length=b_side, color=GREEN, fill_opacity=0.3)
        square_b.set_stroke(color=GREEN, width=3)
        square_b.next_to(triangle, DOWN, buff=0, aligned_edge=LEFT)
        square_b_label = Text("b²", font_size=32, color=GREEN).move_to(square_b)
        
        # Animate squares appearing
        self.play(
            Create(square_a), Write(square_a_label),
            Create(square_b), Write(square_b_label),
            run_time=2
        )
        self.wait(1)

        # === SHOW AREA VALUES ===
        area_text = Text("Area: a² = 9, b² = 16", font_size=32).to_edge(DOWN)
        self.play(Write(area_text))
        self.wait(1)

        # === CREATE SQUARE ON HYPOTENUSE (c²) ===
        # This is trickier - we need to rotate it
        square_c = Square(side_length=5, color=RED, fill_opacity=0.3)
        square_c.set_stroke(color=RED, width=3)
        
        # Position and rotate to match hypotenuse
        square_c.move_to(triangle.get_center())
        square_c.shift(RIGHT * 2.5 + UP * 1.5)
        square_c.rotate(-0.6435)  # Approximately -36.87 degrees
        square_c_label = Text("c²", font_size=32, color=RED).move_to(square_c)
        
        self.play(Create(square_c), Write(square_c_label), run_time=2)
        self.wait(1)

        # === SHOW FINAL EQUATION ===
        self.play(FadeOut(area_text))
        
        final_equation = Text("9 + 16 = 25", font_size=44, color=YELLOW)
        final_equation.to_edge(DOWN)
        self.play(Write(final_equation))
        self.wait(1)

        # === CONCLUSION ===
        conclusion = Text("✨ a² + b² = c² PROVEN! ✨", font_size=36, color=GREEN)
        conclusion.to_edge(DOWN)
        
        self.play(
            FadeOut(final_equation),
            Write(conclusion),
            run_time=2
        )
        self.wait(2)

        # === FINAL MESSAGE ===
        end_text = Text("Day 7 Complete! 🎉", font_size=48, color=WHITE)
        end_text.scale(1.2)
        
        self.play(
            FadeOut(title), FadeOut(formula), FadeOut(triangle),
            FadeOut(square_a), FadeOut(square_b), FadeOut(square_c),
            FadeOut(label_a), FadeOut(label_b), FadeOut(label_c),
            FadeOut(square_a_label), FadeOut(square_b_label), FadeOut(square_c_label),
            FadeOut(right_angle), FadeOut(conclusion),
            Write(end_text),
            run_time=2
        )
        self.wait(2)