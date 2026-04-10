from manim import *
import numpy as np

class Day15(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 15: Euler's Formula", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("e^(iθ) = cos(θ) + i·sin(θ)", font_size=32, font="Consolas", color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE COMPLEX PLANE ===
        # NumberPlane works perfectly for Complex Numbers (Real=X, Imaginary=Y)
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        )
        
        # Axis Labels
        real_label = Text("Real", font_size=24, color=WHITE).next_to(plane.x_axis, RIGHT)
        imag_label = Text("Imaginary", font_size=24, color=WHITE).next_to(plane.y_axis, UP)
        
        self.play(Create(plane), Write(real_label), Write(imag_label))
        self.wait(0.5)

        # === VALUE TRACKER ===
        theta = ValueTracker(0)

        # === COMPLEX VECTOR (e^(iθ)) ===
        # Vector from origin to point on unit circle
        vector = always_redraw(lambda: Arrow(
            start=ORIGIN,
            end=plane.c2p(np.cos(theta.get_value()), np.sin(theta.get_value())),
            color=YELLOW,
            buff=0,
            max_tip_length_to_length_ratio=0.1
        ))
        
        # === DOT ON CIRCLE ===
        dot = always_redraw(lambda: Dot(
            plane.c2p(np.cos(theta.get_value()), np.sin(theta.get_value())),
            color=WHITE,
            radius=0.08
        ))
        
        self.add(vector, dot)
        self.wait(0.5)

        # === PROJECTION LINES ===
        # Cosine (Real part)
        cos_line = always_redraw(lambda: DashedLine(
            start=dot.get_center(),
            end=plane.c2p(dot.get_center()[0], 0),
            color=GREEN,
            stroke_width=2
        ))
        
        # Sine (Imaginary part)
        sin_line = always_redraw(lambda: DashedLine(
            start=dot.get_center(),
            end=plane.c2p(0, dot.get_center()[1]),
            color=RED,
            stroke_width=2
        ))
        
        self.play(Create(cos_line), Create(sin_line))
        self.wait(0.5)

        # === DYNAMIC LABELS ===
        # Show values updating
        value_label = always_redraw(lambda: Text(
            f"θ = {theta.get_value():.2f} rad",
            font_size=24,
            font="Consolas",
            color=YELLOW
        ).to_edge(RIGHT).shift(UP * 2))
        
        euler_label = always_redraw(lambda: Text(
            f"e^(iθ) = {np.cos(theta.get_value()):.2f} + {np.sin(theta.get_value()):.2f}i",
            font_size=24,
            font="Consolas",
            color=WHITE
        ).to_edge(RIGHT).shift(UP * 1.5))
        
        self.play(Write(value_label), Write(euler_label))
        self.wait(0.5)

        # === ANIMATE ROTATION ===
        self.play(
            theta.animate.set_value(2 * PI),  # Full circle
            run_time=6,
            rate_func=linear
        )
        self.wait(1)

        # === HIGHLIGHT EULER'S IDENTITY (θ = π) ===
        # Reset to PI
        self.play(theta.animate.set_value(PI), run_time=2)
        
        identity_text = Text("e^(iπ) + 1 = 0", font_size=48, color=GREEN)
        identity_text.to_edge(DOWN)
        
        self.play(Write(identity_text))
        self.wait(2)

        # === FINAL MESSAGE ===
        final_text = Text("✨ The Most Beautiful Equation ✨", font_size=36, color=WHITE)
        final_text.to_edge(DOWN)
        
        self.play(
            FadeOut(identity_text),
            Write(final_text),
            run_time=2
        )
        self.wait(2)