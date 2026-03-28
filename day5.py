from manim import *
import numpy as np

class Day5(Scene):
    def construct(self):
        # === PART 1: CREATE AXES ===
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 10, 2],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE},
            tips=True
        )
        
        # Use Text() instead of LaTeX labels
        x_label = Text("x", font_size=36).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=36).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=2)
        self.wait(0.5)

        # === PART 2: PLOT A FUNCTION ===
        graph = axes.plot(lambda x: x**2, color=YELLOW, x_range=[-2, 2])
        
        # Use Text() instead of MathTex
        func_label = Text("f(x) = x²", font_size=36).to_edge(UP)
        
        self.play(Write(func_label), Create(graph), run_time=3)
        self.wait(1)

        # === PART 3: ADD A POINT ON THE GRAPH ===
        point = Dot(axes.c2p(1, 1), color=RED)
        point_label = Text("(1, 1)", font_size=28).next_to(point, UR)
        
        self.play(FadeIn(point), Write(point_label), run_time=1.5)
        self.wait(0.5)

        # === PART 4: ANIMATE THE POINT MOVING ===
        mover = Dot(color=GREEN)
        mover.move_to(axes.c2p(-1.5, (-1.5)**2))
        
        self.play(FadeIn(mover))
        self.play(
            mover.animate.move_to(axes.c2p(1.5, (1.5)**2)),
            run_time=3,
            rate_func=linear
        )
        self.wait(1)

        # === PART 5: PLOT MULTIPLE FUNCTIONS ===
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(point), 
                  FadeOut(point_label), FadeOut(mover), FadeOut(func_label))
        
        axes2 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6
        )
        
        self.play(Create(axes2), run_time=1.5)
        
        sin_graph = axes2.plot(lambda x: 2 * np.sin(x), color=RED)
        cos_graph = axes2.plot(lambda x: 2 * np.cos(x), color=BLUE)
        
        sin_label = Text("y = 2sin(x)", color=RED, font_size=24).to_edge(UL)
        cos_label = Text("y = 2cos(x)", color=BLUE, font_size=24).next_to(sin_label, DOWN)
        
        self.play(Write(sin_label), Write(cos_label))
        self.play(Create(sin_graph), Create(cos_graph), run_time=3)
        
        self.wait(2)

        # === PART 6: FINAL MESSAGE ===
        final_text = Text("📈 Graphs Bring Math to Life!", color=GREEN)
        final_text.scale(1.2)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text))
        self.wait(2)