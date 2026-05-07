from manim import *

class AircraftDay03(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("150-Project Journey: Aircraft Design", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        subtitle = Text("Day 3: Animate Incoming Airflow", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE AIRFOIL SHAPE (Same as Day 1 & 2) ===
        upper_points = [
            [-3, 0, 0],
            [-2, 0.8, 0],
            [0, 1.2, 0],
            [2, 0.9, 0],
            [3, 0.3, 0],
        ]
        
        lower_points = [
            [3, 0.3, 0],
            [2, -0.3, 0],
            [0, -0.5, 0],
            [-2, -0.4, 0],
            [-3, 0, 0],
        ]
        
        upper_curve = CubicBezier(
            upper_points[0],
            upper_points[1],
            upper_points[2],
            upper_points[3],
            color=BLUE,
            stroke_width=4
        )
        
        lower_curve = CubicBezier(
            lower_points[0],
            lower_points[1],
            lower_points[2],
            lower_points[3],
            color=BLUE,
            stroke_width=4
        )
        
        trailing_edge = Line(
            upper_points[4],
            lower_points[0],
            color=BLUE,
            stroke_width=4
        )
        
        airfoil = VGroup(upper_curve, lower_curve, trailing_edge)
        airfoil.scale(1.5)
        airfoil.move_to(ORIGIN)
        
        airfoil_filled = VMobject()
        airfoil_filled.set_points_as_corners([
            *upper_points,
            *lower_points,
            upper_points[0]
        ])
        airfoil_filled.set_fill(BLUE, opacity=0.3)
        airfoil_filled.set_stroke(BLUE, width=4)
        airfoil_filled.scale(1.5)
        airfoil_filled.move_to(ORIGIN)
        
        self.play(
            Create(upper_curve),
            Create(lower_curve),
            Create(trailing_edge),
            FadeIn(airfoil_filled),
            run_time=3
        )
        self.wait(0.5)

        # === CREATE INCOMING AIRFLOW ARROWS ===
        # Multiple parallel arrows approaching from the left
        num_arrows = 8
        airflow_arrows = VGroup()
        
        # Arrow positions (spread vertically on the left side)
        y_positions = [-2.5, -1.8, -1.1, -0.4, 0.3, 1.0, 1.7, 2.4]
        
        for y_pos in y_positions:
            arrow = Arrow(
                start=[-6, y_pos, 0],
                end=[-4.5, y_pos, 0],
                color=WHITE,
                buff=0,
                max_tip_length_to_length_ratio=0.15,
                stroke_width=3
            )
            airflow_arrows.add(arrow)
        
        # === ANIMATE AIRFLOW ARROWS APPEARING ===
        airflow_label = Text("Incoming Airflow", font_size=28, font="Consolas", color=WHITE)
        airflow_label.to_edge(LEFT).shift(UP * 2.5)
        
        self.play(Write(airflow_label))
        
        # Animate arrows appearing one by one
        for i, arrow in enumerate(airflow_arrows):
            self.play(
                Create(arrow),
                run_time=0.3
            )
        self.wait(0.5)

        # === ANIMATE AIRFLOW MOVING TOWARD WING ===
        # Move all arrows to the right (toward the airfoil)
        self.play(
            airflow_arrows.animate.shift(RIGHT * 2),
            run_time=2,
            rate_func=linear
        )
        self.wait(0.5)

        # === SHOW AIRFLOW SPLITTING AT LEADING EDGE ===
        split_label = Text("Airflow Splits at Leading Edge", font_size=28, font="Consolas", color=YELLOW)
        split_label.to_edge(LEFT).shift(UP * 2)
        
        self.play(Write(split_label))
        self.wait(0.5)

        # Create split path arrows (upper and lower)
        upper_flow_arrows = VGroup()
        lower_flow_arrows = VGroup()
        
        # Upper surface flow (curved over the top)
        upper_flow_paths = [
            [-3, 0.5, 0],  # Start near leading edge
            [-1, 1.5, 0],  # Curve over top
            [1, 1.3, 0],   # Continue over
            [3, 0.8, 0],   # Exit at trailing edge
        ]
        
        # Lower surface flow (curved under the bottom)
        lower_flow_paths = [
            [-3, -0.5, 0],  # Start near leading edge
            [-1, -1.0, 0],  # Curve under bottom
            [1, -0.8, 0],   # Continue under
            [3, -0.3, 0],   # Exit at trailing edge
        ]
        
        # Create upper flow arrows
        for i in range(3):
            arrow = Arrow(
                start=[upper_flow_paths[0][0] + i*0.5, upper_flow_paths[0][1], 0],
                end=[upper_flow_paths[1][0] + i*0.5, upper_flow_paths[1][1], 0],
                color=RED,
                buff=0,
                max_tip_length_to_length_ratio=0.15,
                stroke_width=3
            )
            upper_flow_arrows.add(arrow)
        
        # Create lower flow arrows
        for i in range(3):
            arrow = Arrow(
                start=[lower_flow_paths[0][0] + i*0.5, lower_flow_paths[0][1], 0],
                end=[lower_flow_paths[1][0] + i*0.5, lower_flow_paths[1][1], 0],
                color=BLUE,
                buff=0,
                max_tip_length_to_length_ratio=0.15,
                stroke_width=3
            )
            lower_flow_arrows.add(arrow)
        
        # Animate split flow appearing
        self.play(
            Create(upper_flow_arrows),
            Create(lower_flow_arrows),
            run_time=2
        )
        self.wait(0.5)

        # === ANIMATE FLOW ALONG SURFACES ===
        # Move upper flow arrows along the upper surface
        self.play(
            upper_flow_arrows.animate.shift(RIGHT * 2 + UP * 0.3),
            lower_flow_arrows.animate.shift(RIGHT * 2 + DOWN * 0.3),
            run_time=2,
            rate_func=linear
        )
        self.wait(0.5)

        # === FLOW INFORMATION BOX ===
        flow_info_box = Rectangle(width=5.5, height=3, color=WHITE, fill_opacity=0.1)
        flow_info_box.to_edge(DOWN)
        
        flow_info_title = Text("Airflow Behavior", font_size=32, font="Consolas", color=YELLOW)
        flow_info_title.move_to(flow_info_box.get_center()).shift(UP * 1)
        
        flow_info_items = VGroup(
            Text("• Air approaches from the left", font_size=24, font="Consolas", color=WHITE),
            Text("• Splits at the leading edge", font_size=24, font="Consolas", color=WHITE),
            Text("• Upper flow: Faster, lower pressure (red)", font_size=24, font="Consolas", color=RED),
            Text("• Lower flow: Slower, higher pressure (blue)", font_size=24, font="Consolas", color=BLUE),
            Text("• Meets at trailing edge", font_size=24, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        
        flow_info_items.next_to(flow_info_title, DOWN, buff=0.3)
        flow_info_items.move_to(flow_info_box.get_center()).shift(DOWN * 0.3)
        
        self.play(
            Create(flow_info_box),
            Write(flow_info_title),
            Write(flow_info_items),
            run_time=3
        )
        self.wait(1)

        # === PROGRESS TRACKER ===
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(flow_info_box), FadeOut(flow_info_title), FadeOut(flow_info_items),
            FadeOut(airflow_label), FadeOut(split_label),
            FadeOut(airflow_arrows), FadeOut(upper_flow_arrows), FadeOut(lower_flow_arrows)
        )
        
        progress_title = Text("150-Project Progress", font_size=36, color=GREEN)
        progress_title.to_edge(UP).shift(DOWN * 1)
        
        aircraft_progress = Text("Aircraft Design: Day 3/30", font_size=28, font="Consolas", color=GREEN)
        aircraft_progress.next_to(progress_title, DOWN, buff=0.3)
        
        total_progress = Text("Overall: 3/150 Complete (2.0%)", font_size=28, font="Consolas", color=YELLOW)
        total_progress.next_to(aircraft_progress, DOWN, buff=0.3)
        
        self.play(
            Write(progress_title),
            Write(aircraft_progress),
            Write(total_progress),
            run_time=2
        )
        self.wait(2)

        # === FINAL MESSAGE ===
        final_text = Text("✨ 147 Projects to Go! ✨", font_size=48, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)