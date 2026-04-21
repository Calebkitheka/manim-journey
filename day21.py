from manim import *
import numpy as np

class Day21(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 21: Quantum Wave Functions", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Visualizing the Schrödinger Equation", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE AXES ===
        axes = Axes(
            x_range=[-10, 10, 2],
            y_range=[0, 1.5, 0.5],
            x_length=12,
            y_length=4,
            axis_config={"color": BLUE}
        )
        
        x_label = Text("Position (x)", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Probability |ψ|²", font_size=24).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # === QUANTUM WAVE PACKET ===
        # Parameters
        x0_tracker = ValueTracker(0)
        sigma = 1.5
        k = 2
        
        # Probability density function
        def probability_density(x, x0):
            envelope = np.exp(-((x - x0)**2) / (2 * sigma**2))
            oscillation = np.cos(k * (x - x0))**2
            return envelope * oscillation

        # === WAVE FUNCTION GRAPH ===
        wave_graph = always_redraw(lambda: axes.plot(
            lambda x: probability_density(x, x0_tracker.get_value()),
            color=PURPLE,
            x_range=[-10, 10],
            stroke_width=3
        ))
        
        self.play(Create(wave_graph))
        self.wait(0.5)

        # === PARTICLE DOT ===
        particle_dot = always_redraw(lambda: Dot(
            axes.c2p(x0_tracker.get_value(), 
                     probability_density(x0_tracker.get_value(), x0_tracker.get_value())),
            color=YELLOW,
            radius=0.1
        ))
        
        self.play(Create(particle_dot))
        self.wait(0.5)

        # === LABELS ===
        psi_label = Text("ψ(x) = Wave Function", font_size=24, font="Consolas", color=PURPLE)
        psi_label.to_edge(RIGHT).shift(UP * 2)
        
        prob_label = Text("|ψ|² = Probability Density", font_size=24, font="Consolas", color=WHITE)
        prob_label.next_to(psi_label, DOWN, buff=0.3)
        
        self.play(Write(psi_label), Write(prob_label))
        self.wait(0.5)

        # === ANIMATE WAVE PACKET MOVEMENT ===
        self.play(
            x0_tracker.animate.set_value(5),
            run_time=4,
            rate_func=linear
        )
        self.wait(0.5)

        # === HEISENBERG UNCERTAINTY PRINCIPLE ===
        uncertainty_principle = Text("Δx · Δp ≥ ℏ/2", font_size=36, font="Consolas", color=YELLOW)
        uncertainty_principle.to_edge(DOWN)
        
        self.play(Write(uncertainty_principle))
        self.wait(2)

        # === FINAL MESSAGE ===
        final_text = Text("✨ Quantum Mechanics is Probabilistic! ✨", font_size=36, color=WHITE)
        final_text.to_edge(DOWN)
        
        self.play(
            FadeOut(uncertainty_principle),
            Write(final_text),
            run_time=2
        )
        self.wait(2)