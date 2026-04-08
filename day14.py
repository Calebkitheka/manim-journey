from manim import *
import numpy as np

class Day14(Scene):
    def construct(self):
        # === INTRO TITLE ===
        title = Text("14-Day Manim Challenge", font_size=48, color=YELLOW)
        subtitle = Text("Capstone: Calculus Visualizer", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), Write(subtitle), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # === CREATE AXES ===
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE, "include_ticks": False}
        )
        
        x_label = Text("x", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=24).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=2)

        # === CREATE FUNCTION GRAPH ===
        graph = axes.plot(lambda x: np.sin(x), color=GREEN, x_range=[-2 * PI, 2 * PI])
        graph_label = Text("f(x) = sin(x)", font_size=28, color=GREEN)
        graph_label.to_edge(RIGHT).shift(UP * 2)
        
        self.play(Create(graph), Write(graph_label), run_time=2)
        self.wait(0.5)

        # === VALUE TRACKER FOR MOVEMENT ===
        x_tracker = ValueTracker(-2 * PI)

        # === DYNAMIC TANGENT LINE (FIXED for v0.20.1) ===
        def get_tangent():
            x_val = x_tracker.get_value()
            y_val = np.sin(x_val)
            slope = np.cos(x_val)  # Derivative of sin(x)
            
            line_length = 1
            x1 = x_val - line_length
            y1 = y_val + slope * (x1 - x_val)
            x2 = x_val + line_length
            y2 = y_val + slope * (x2 - x_val)
            
            return Line(
                axes.c2p(x1, y1),
                axes.c2p(x2, y2),
                color=YELLOW,
                stroke_width=3
            )
        
        tangent_line = always_redraw(get_tangent)
        
        # === DYNAMIC POINT ON GRAPH ===
        dot = always_redraw(lambda: Dot(
            axes.c2p(x_tracker.get_value(), np.sin(x_tracker.get_value())),
            color=WHITE,
            radius=0.08
        ))
        
        self.add(tangent_line, dot)
        self.wait(0.5)

        # === UI PANEL ===
        panel = Rectangle(width=4, height=2, color=WHITE, fill_opacity=0.1)
        panel.to_edge(RIGHT).shift(DOWN * 1)
        
        slope_label = always_redraw(lambda: Text(
            f"Slope: {np.cos(x_tracker.get_value()):.2f}",
            font_size=24,
            font="Consolas",
            color=YELLOW
        ).move_to(panel.get_center()))
        
        panel_label = Text("Derivative Value", font_size=20, color=WHITE)
        panel_label.next_to(panel, UP, buff=0.1)
        
        self.play(Create(panel), Write(panel_label), Write(slope_label))
        self.wait(0.5)

        # === ANIMATE THE MOVEMENT ===
        self.play(
            x_tracker.animate.set_value(2 * PI),
            run_time=8,
            rate_func=linear
        )
        self.wait(1)

        # === CONCLUSION ===
        final_title = Text("14 Days Complete!", font_size=48, color=YELLOW)
        final_title.to_edge(UP)
        
        skills = VGroup(
            Text("✓ Animations", font_size=24, font="Consolas"),
            Text("✓ Graphs & Calculus", font_size=24, font="Consolas"),
            Text("✓ 3D & Physics", font_size=24, font="Consolas"),
            Text("✓ Git & YouTube", font_size=24, font="Consolas")
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        skills.next_to(final_title, DOWN, buff=0.5)
        
        github_text = Text("github.com/Calebkitheka/manim-journey", font_size=20, color=BLUE)
        github_text.to_edge(DOWN)
        
        self.play(
            FadeOut(axes), FadeOut(graph), FadeOut(tangent_line),
            FadeOut(dot), FadeOut(panel), FadeOut(panel_label),
            FadeOut(slope_label), FadeOut(graph_label),
            FadeOut(x_label), FadeOut(y_label),
            Write(final_title), Write(skills), Write(github_text),
            run_time=3
        )
        
        self.wait(3)