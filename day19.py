from manim import *
import numpy as np

class Day19(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 19: Wave Interference", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Constructive & Destructive Interference", font_size=28, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE AXES ===
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE}
        )
        
        x_label = Text("Position", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Amplitude", font_size=24).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # === VALUE TRACKERS ===
        time_tracker = ValueTracker(0)
        phase_diff = ValueTracker(0)  # Phase difference between waves

        # === WAVE 1 (Blue) ===
        wave1 = always_redraw(lambda: axes.plot(
            lambda x: np.sin(x - time_tracker.get_value()),
            color=BLUE,
            x_range=[0, 4 * PI]
        ))
        
        wave1_label = Text("Wave 1", font_size=24, font="Consolas", color=BLUE)
        wave1_label.to_edge(RIGHT).shift(UP * 2)
        
        # === WAVE 2 (Red) ===
        wave2 = always_redraw(lambda: axes.plot(
            lambda x: np.sin(x - time_tracker.get_value() + phase_diff.get_value()),
            color=RED,
            x_range=[0, 4 * PI]
        ))
        
        wave2_label = Text("Wave 2", font_size=24, font="Consolas", color=RED)
        wave2_label.to_edge(RIGHT).shift(UP * 1.5)
        
        self.play(Create(wave1), Write(wave1_label))
        self.play(Create(wave2), Write(wave2_label))
        self.wait(0.5)

        # === RESULTANT WAVE (Green - Sum of both) ===
        resultant = always_redraw(lambda: axes.plot(
            lambda x: np.sin(x - time_tracker.get_value()) + 
                      np.sin(x - time_tracker.get_value() + phase_diff.get_value()),
            color=GREEN,
            x_range=[0, 4 * PI],
            stroke_width=3
        ))
        
        resultant_label = Text("Resultant", font_size=24, font="Consolas", color=GREEN)
        resultant_label.to_edge(RIGHT).shift(UP * 1)
        
        self.play(Create(resultant), Write(resultant_label))
        self.wait(1)

        # === PHASE DIFFERENCE DISPLAY ===
        phase_label = always_redraw(lambda: Text(
            f"Phase Diff: {phase_diff.get_value():.2f} rad",
            font_size=24,
            font="Consolas",
            color=YELLOW
        ).to_edge(LEFT).shift(UP * 2))
        
        self.play(Write(phase_label))
        self.wait(0.5)

        # === ANIMATE WAVE PROPAGATION ===
        self.play(
            time_tracker.animate.set_value(2 * PI),
            run_time=4,
            rate_func=linear
        )
        self.wait(0.5)

        # === DEMO: CONSTRUCTIVE INTERFERENCE (phase = 0) ===
        self.play(phase_diff.animate.set_value(0), run_time=2)
        
        construct_text = Text("Constructive: Waves Add Up!", font_size=28, color=GREEN)
        construct_text.to_edge(DOWN)
        self.play(Write(construct_text))
        self.wait(1)
        self.play(FadeOut(construct_text))

        # === DEMO: DESTRUCTIVE INTERFERENCE (phase = π) ===
        self.play(phase_diff.animate.set_value(PI), run_time=2)
        
        destruct_text = Text("Destructive: Waves Cancel Out!", font_size=28, color=RED)
        destruct_text.to_edge(DOWN)
        self.play(Write(destruct_text))
        self.wait(1)
        self.play(FadeOut(destruct_text))

        # === DEMO: PARTIAL INTERFERENCE (phase = π/2) ===
        self.play(phase_diff.animate.set_value(PI/2), run_time=2)
        
        partial_text = Text("Partial: Somewhere In Between", font_size=28, color=YELLOW)
        partial_text.to_edge(DOWN)
        self.play(Write(partial_text))
        self.wait(1)
        self.play(FadeOut(partial_text))

        # === FINAL MESSAGE ===
        final_text = Text("✨ Interference Powers Technology! ✨", font_size=36, color=WHITE)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text))
        self.wait(2)