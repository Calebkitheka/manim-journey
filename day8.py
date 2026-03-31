from manim import *
import numpy as np

class Day8(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 8: Fourier Series & Epicycles", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === CREATE AXES ===
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": BLUE}
        )
        
        x_label = Text("t", font_size=28).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=28).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # === CREATE CIRCLE (Epicycle Base) ===
        circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.1)
        circle.move_to(axes.c2p(0, 0))
        
        # Center dot
        center_dot = Dot(axes.c2p(0, 0), color=WHITE)
        
        # Rotating dot on circle edge
        rotating_dot = Dot(color=RED)
        rotating_dot.move_to(axes.c2p(1.5, 0))
        
        # === CREATE WAVE PATH ===
        wave_path = VMobject(color=YELLOW)
        wave_points = []
        
        # === VALUE TRACKERS ===
        angle_tracker = ValueTracker(0)
        time_tracker = ValueTracker(0)
        
        # === DYNAMIC ELEMENTS ===
        # Rotating dot moves around circle
        rotating_dot.add_updater(lambda d: d.move_to(
            axes.c2p(
                1.5 * np.cos(angle_tracker.get_value()),
                1.5 * np.sin(angle_tracker.get_value())
            )
        ))
        
        # Line from center to rotating dot (radius)
        radius_line = always_redraw(lambda: Line(
            axes.c2p(0, 0),
            rotating_dot.get_center(),
            color=BLUE,
            stroke_width=2
        ))
        
        # Dotted line from rotating dot to wave
        guide_line = always_redraw(lambda: DashedLine(
            rotating_dot.get_center(),
            axes.c2p(time_tracker.get_value(), rotating_dot.get_center()[1]),
            color=GREEN,
            stroke_width=1
        ))
        
        # Wave tracer dot
        wave_dot = always_redraw(lambda: Dot(
            axes.c2p(time_tracker.get_value(), rotating_dot.get_center()[1]),
            color=YELLOW,
            radius=0.08
        ))
        
        # === ANIMATE ===
        self.play(Create(circle), Create(center_dot), Create(rotating_dot))
        self.play(Create(radius_line))
        self.wait(0.5)
        
        # Add wave elements
        self.play(Create(guide_line), Create(wave_dot))
        
        # Animate rotation and wave drawing
        self.play(
            angle_tracker.animate.set_value(4 * PI),  # 2 full rotations
            time_tracker.animate.set_value(8),
            run_time=6,
            rate_func=linear
        )
        
        self.wait(2)

        # === FINAL MESSAGE ===
        final_text = Text("✨ Circular Motion → Wave! ✨", font_size=36, color=GREEN)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)