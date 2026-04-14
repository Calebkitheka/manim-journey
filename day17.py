from manim import *
import numpy as np

class Day17(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 17: SIR Epidemic Model", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Differential Equations in Action", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === SIR MODEL PARAMETERS ===
        N = 1000  # Total population
        I0 = 1    # Initial infected
        R0 = 0    # Initial recovered
        S0 = N - I0 - R0  # Initial susceptible
        
        beta = 0.3   # Infection rate
        gamma = 0.1  # Recovery rate
        
        # === CREATE AXES ===
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, N, 100],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE}
        )
        
        x_label = Text("Time (days)", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Population", font_size=24).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # === LEGEND ===
        legend = VGroup(
            Text("S - Susceptible", font_size=20, font="Consolas", color=BLUE),
            Text("I - Infected", font_size=20, font="Consolas", color=RED),
            Text("R - Recovered", font_size=20, font="Consolas", color=GREEN)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        
        legend.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(legend))
        self.wait(0.5)

        # === SIMULATE SIR MODEL ===
        # Using Euler method to solve differential equations
        dt = 0.1
        days = 100
        steps = int(days / dt)
        
        # Arrays to store values
        S_values = [S0]
        I_values = [I0]
        R_values = [R0]
        t_values = [0]
        
        # Calculate SIR over time
        S, I, R = S0, I0, R0
        for _ in range(steps):
            # Differential equations
            dS = -beta * S * I / N
            dI = beta * S * I / N - gamma * I
            dR = gamma * I
            
            # Update values
            S = S + dS * dt
            I = I + dI * dt
            R = R + dR * dt
            
            S_values.append(S)
            I_values.append(I)
            R_values.append(R)
            t_values.append(t_values[-1] + dt)

        # === CREATE GRAPHS ===
        # Susceptible curve (Blue)
        S_graph = axes.plot_line_graph(
            x_values=t_values,
            y_values=S_values,
            line_color=BLUE,
            stroke_width=2
        )
        
        # Infected curve (Red)
        I_graph = axes.plot_line_graph(
            x_values=t_values,
            y_values=I_values,
            line_color=RED,
            stroke_width=2
        )
        
        # Recovered curve (Green)
        R_graph = axes.plot_line_graph(
            x_values=t_values,
            y_values=R_values,
            line_color=GREEN,
            stroke_width=2
        )
        
        # Animate graphs appearing
        self.play(Create(S_graph), run_time=2)
        self.wait(0.5)
        self.play(Create(I_graph), run_time=2)
        self.wait(0.5)
        self.play(Create(R_graph), run_time=2)
        self.wait(1)

        # === DISPLAY KEY METRICS ===
        # Peak infected
        peak_infected = max(I_values)
        peak_day = I_values.index(peak_infected) * dt
        
        metrics = VGroup(
            Text(f"Peak Infected: {peak_infected:.0f}", font_size=24, font="Consolas", color=RED),
            Text(f"Peak Day: {peak_day:.1f}", font_size=24, font="Consolas", color=WHITE),
            Text(f"Total Recovered: {R_values[-1]:.0f}", font_size=24, font="Consolas", color=GREEN)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        metrics.to_edge(DOWN)
        self.play(Write(metrics))
        self.wait(2)

        # === FINAL MESSAGE ===
        final_text = Text("✨ Math Predicts Real-World Spread! ✨", font_size=36, color=WHITE)
        final_text.to_edge(DOWN)
        
        self.play(
            FadeOut(metrics),
            Write(final_text),
            run_time=2
        )
        self.wait(2)