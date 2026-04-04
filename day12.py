from manim import *
import numpy as np

class Day12(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 12: Physics Pendulum", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Harmonic Motion Simulation", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(0.5)

        # === PHYSICS CONSTANTS ===
        GRAVITY = 9.8
        LENGTH = 3
        MASS = 1
        DAMPING = 0.995  # Air resistance (1 = no resistance)
        
        # === CREATE PENDULUM PIVOT ===
        pivot = Dot(ORIGIN + UP * 2.5, color=WHITE, radius=0.1)
        self.play(Create(pivot))
        self.wait(0.5)

        # === VALUE TRACKERS ===
        # Angle (in radians), Angular velocity, Angular acceleration
        angle_tracker = ValueTracker(45 * DEGREES)  # Start at 45 degrees
        angular_velocity = ValueTracker(0)
        
        # === PENDULUM BOB ===
        bob = Dot(color=RED, radius=0.3)
        bob.add_updater(lambda b: b.move_to(
            pivot.get_center() + LENGTH * np.array([
                np.sin(angle_tracker.get_value()),
                -np.cos(angle_tracker.get_value()),
                0
            ])
        ))
        
        # === PENDULUM ARM ===
        arm = always_redraw(lambda: Line(
            pivot.get_center(),
            bob.get_center(),
            color=BLUE,
            stroke_width=4
        ))
        
        self.play(Create(arm), Create(bob))
        self.wait(0.5)

        # === CREATE TRACE PATH ===
        trace = VMobject(color=YELLOW, stroke_width=2)
        trace.set_points_as_corners([bob.get_center(), bob.get_center()])
        trace.add_updater(lambda t: t.add_points_as_corners([bob.get_center()]))
        
        self.play(Create(trace))
        self.wait(0.5)

        # === DISPLAY PHYSICS VALUES ===
        # Angle display
        angle_label = always_redraw(lambda: Text(
            f"Angle: {angle_tracker.get_value() * 180 / PI:.1f}°",
            font_size=24,
            font="Consolas"
        ).to_edge(LEFT).shift(UP * 2))
        
        # Velocity display
        velocity_label = always_redraw(lambda: Text(
            f"Velocity: {angular_velocity.get_value():.2f} rad/s",
            font_size=24,
            font="Consolas"
        ).to_edge(LEFT).shift(UP * 1.5))
        
        # Time display
        time_tracker = ValueTracker(0)
        time_label = always_redraw(lambda: Text(
            f"Time: {time_tracker.get_value():.1f} s",
            font_size=24,
            font="Consolas"
        ).to_edge(LEFT).shift(UP * 1))
        
        self.play(Write(angle_label), Write(velocity_label), Write(time_label))
        self.wait(0.5)

        # === PHYSICS SIMULATION ===
        # Simulate pendulum motion using Euler integration
        dt = 0.016  # Time step (approximately 60 FPS)
        total_time = 10  # Simulate for 10 seconds
        
        for i in range(int(total_time / dt)):
            # Physics equations for pendulum
            # Angular acceleration = -(g/L) * sin(angle)
            angular_acceleration = -(GRAVITY / LENGTH) * np.sin(angle_tracker.get_value())
            
            # Update velocity
            new_velocity = angular_velocity.get_value() + angular_acceleration * dt
            angular_velocity.set_value(new_velocity * DAMPING)
            
            # Update angle
            new_angle = angle_tracker.get_value() + angular_velocity.get_value() * dt
            angle_tracker.set_value(new_angle)
            
            # Update time
            time_tracker.set_value(time_tracker.get_value() + dt)
            
            # Wait for next frame
            if i % 3 == 0:  # Update every 3 frames for performance
                self.wait(dt * 3)

        self.wait(1)

        # === FINAL MESSAGE ===
        final_text = Text("✨ Physics in Motion! ✨", font_size=36, color=GREEN)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)