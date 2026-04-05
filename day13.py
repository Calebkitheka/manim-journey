from manim import *
import numpy as np

class Day13(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 13: Interactive Simulations", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Parameter Explorer - Gravity Comparison", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(0.5)

        # === CREATE THREE PENDULUMS SIDE BY SIDE ===
        pendulum_positions = [LEFT * 4, ORIGIN, RIGHT * 4]
        gravity_values = [1.6, 9.8, 24.8]  # Moon, Earth, Jupiter
        labels = ["Moon (1.6 m/s²)", "Earth (9.8 m/s²)", "Jupiter (24.8 m/s²)"]
        colors = [BLUE, GREEN, RED]
        
        pendulums = []
        traces = []
        value_trackers = []
        
        # Create 3 pendulums
        for i, pos in enumerate(pendulum_positions):
            # Pivot for each pendulum
            pivot = Dot(pos + UP * 2, color=WHITE, radius=0.08)
            
            # Value tracker for angle
            angle_tracker = ValueTracker(30 * DEGREES)
            value_trackers.append(angle_tracker)
            
            # Bob
            bob = Dot(color=colors[i], radius=0.2)
            bob.add_updater(lambda b, idx=i: b.move_to(
                pivot.get_center() + 1.5 * np.array([
                    np.sin(value_trackers[idx].get_value()),
                    -np.cos(value_trackers[idx].get_value()),
                    0
                ])
            ))
            
            # Arm
            arm = always_redraw(lambda p=pivot, b=bob: Line(
                p.get_center(),
                b.get_center(),
                color=colors[i],
                stroke_width=3
            ))
            
            # Trace path
            trace = VMobject(color=colors[i], stroke_width=1)
            trace.set_points_as_corners([bob.get_center(), bob.get_center()])
            trace.add_updater(lambda t, b=bob: t.add_points_as_corners([b.get_center()]))
            
            # Label
            label = Text(labels[i], font_size=20, font="Consolas", color=colors[i])
            label.next_to(pivot, DOWN, buff=0.3)
            
            self.add(pivot, arm, bob, trace, label)
            pendulums.append((pivot, arm, bob, trace, label))
        
        self.wait(0.5)

        # === DISPLAY GRAVITY INFO ===
        info_box = Rectangle(width=5, height=2, color=WHITE, fill_opacity=0.1)
        info_box.to_edge(DOWN)
        
        info_text = Text(
            "Watch how gravity affects swing speed!",
            font_size=24,
            font="Consolas"
        )
        info_text.move_to(info_box.get_center())
        
        self.play(Create(info_box), Write(info_text))
        self.wait(0.5)

        # === ANIMATE ALL PENDULUMS ===
        # Simulate physics for each pendulum
        dt = 0.016
        total_time = 8
        
        for i in range(int(total_time / dt)):
            for j, tracker in enumerate(value_trackers):
                # Different gravity for each pendulum
                gravity = gravity_values[j]
                length = 1.5
                
                # Physics equation
                angular_acceleration = -(gravity / length) * np.sin(tracker.get_value())
                
                # Simple velocity simulation (simplified for demo)
                current_angle = tracker.get_value()
                new_angle = current_angle + 0.1 * np.sin(i * 0.1 * (gravity / 5)) * dt * 10
                tracker.set_value(new_angle)
            
            if i % 2 == 0:
                self.wait(dt * 2)

        self.wait(1)

        # === SHOW PARAMETER TABLE ===
        self.play(FadeOut(info_box), FadeOut(info_text))
        
        table_title = Text("Gravity Comparison Table", font_size=32, color=YELLOW)
        table_title.to_edge(DOWN)
        
        table_data = VGroup(
            Text("Moon:    Slow swing, long period", font_size=20, font="Consolas", color=BLUE),
            Text("Earth:   Medium swing", font_size=20, font="Consolas", color=GREEN),
            Text("Jupiter: Fast swing, short period", font_size=20, font="Consolas", color=RED)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        table_data.next_to(table_title, DOWN, buff=0.3)
        
        self.play(Write(table_title), Write(table_data))
        self.wait(2)

        # === FINAL MESSAGE ===
        final_text = Text("✨ Parameters Change Everything! ✨", font_size=36, color=WHITE)
        final_text.to_edge(DOWN)
        self.play(
            FadeOut(table_title),
            FadeOut(table_data),
            Write(final_text),
            run_time=2
        )
        self.wait(2)