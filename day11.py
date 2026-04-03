from manim import *
import numpy as np

class Day11(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 11: Matrix Transformations", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Linear Algebra Visualized", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(0.5)

        # === CREATE 2D GRID ===
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        )
        
        x_label = Text("x", font_size=28, color=WHITE).next_to(grid.x_axis, RIGHT)
        y_label = Text("y", font_size=28, color=WHITE).next_to(grid.y_axis, UP)
        
        self.play(Create(grid), Write(x_label), Write(y_label))
        self.wait(1)

        # === CREATE BASIS VECTORS ===
        i_hat = Arrow(
            start=ORIGIN,
            end=RIGHT,
            color=RED,
            buff=0,
            max_tip_length_to_length_ratio=0.1
        )
        i_label = Text("i-hat", font_size=28, color=RED).next_to(i_hat, RIGHT, buff=0.2)
        
        j_hat = Arrow(
            start=ORIGIN,
            end=UP,
            color=GREEN,
            buff=0,
            max_tip_length_to_length_ratio=0.1
        )
        j_label = Text("j-hat", font_size=28, color=GREEN).next_to(j_hat, UP, buff=0.2)
        
        self.play(Create(i_hat), Write(i_label), Create(j_hat), Write(j_label))
        self.wait(1)

        # === DISPLAY TRANSFORMATION MATRIX ===
        # FIXED: Use Text() instead of MathTex() to avoid LaTeX errors
        matrix_title = Text("Transformation Matrix:", font_size=28).to_edge(RIGHT).shift(UP * 2)
        
        matrix = Text(
            "[1  1]\n[0  1]",
            font_size=36,
            font="Consolas",
            color=YELLOW
        ).to_edge(RIGHT).shift(UP * 1)
        
        self.play(Write(matrix_title), Write(matrix))
        self.wait(1)

        # === ANIMATE THE TRANSFORMATION ===
        self.play(
            grid.animate.apply_matrix([[1, 1], [0, 1]]),
            i_hat.animate.apply_matrix([[1, 1], [0, 1]]),
            j_hat.animate.apply_matrix([[1, 1], [0, 1]]),
            run_time=3
        )
        self.wait(1)

        # === SHOW NEW BASIS VECTOR POSITIONS ===
        new_i_label = Text("i-hat → [1, 0]", font_size=24, color=RED)
        new_i_label.to_edge(RIGHT).shift(DOWN * 1)
        
        new_j_label = Text("j-hat → [1, 1]", font_size=24, color=GREEN)
        new_j_label.to_edge(RIGHT).shift(DOWN * 1.5)
        
        self.play(Write(new_i_label), Write(new_j_label))
        self.wait(1)

        # === SECOND TRANSFORMATION ===
        self.play(
            grid.animate.apply_matrix([[1, -1], [0, 1]]),
            i_hat.animate.apply_matrix([[1, -1], [0, 1]]),
            j_hat.animate.apply_matrix([[1, -1], [0, 1]]),
            run_time=2
        )
        self.wait(1)

        # === FINAL MESSAGE ===
        final_text = Text("✨ Matrices Transform Space! ✨", font_size=36, color=GREEN)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)