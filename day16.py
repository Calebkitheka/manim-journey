from manim import *
import numpy as np

class Day16(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 16: Fourier Series", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Building Complex Waves from Simple Sines", font_size=28, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE AXES ===
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE}
        )
        
        x_label = Text("t", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("amp", font_size=24).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # === TARGET WAVE (Square Wave) ===
        square_wave_label = Text("Target: Square Wave", font_size=24, color=GRAY)
        square_wave_label.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(square_wave_label))
        self.wait(0.5)

        # === FOURIER SERIES APPROXIMATION ===
        # Start with empty graph
        current_sum = axes.plot(lambda x: 0, color=WHITE)
        self.play(Create(current_sum))
        self.wait(0.5)

        # Function to calculate Fourier sum up to n terms
        def fourier_sum(x, n_terms):
            total = 0
            for k in range(1, n_terms + 1):
                # FIXED: Use underscore instead of space
                odd_harmonic = 2 * k - 1
                total += np.sin(odd_harmonic * x) / odd_harmonic
            return total * (4 / PI)  # Scaling factor

        # Animate adding harmonics
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
        
        for i in range(5):
            n_terms = i + 1
            
            # Create new graph
            new_graph = axes.plot(
                lambda x: fourier_sum(x, n_terms),
                color=colors[i % len(colors)],
                x_range=[0, 4 * PI]
            )
            
            # Label for this harmonic
            harmonic_label = Text(
                f"Harmonics: {n_terms}",
                font_size=24,
                font="Consolas",
                color=colors[i % len(colors)]
            ).to_edge(RIGHT).shift(DOWN * 1)