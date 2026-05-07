from manim import *

class AircraftDay04(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("150-Project Journey: Aircraft Design", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        subtitle = Text("Day 4: Split Flow Above and Below", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE AIRFOIL SHAPE (Same as Day 1-3) ===
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

        # === CREATE INCOMING AIRFLOW (From Day 3) ===
        num_arrows = 5
        incoming_arrows = VGroup()
        y_positions = [-1.5, -0.75, 0, 0.75, 1.5]
        
        for y_pos in y_positions:
            arrow = Arrow(
                start=[-6, y_pos, 0],
                end=[-4.5, y_pos, 0],
                color=WHITE,
                buff=0,
                max_tip_length_to_length_ratio=0.15,
                stroke_width=3
            )
            incoming_arrows.add(arrow)
        
        incoming_label = Text("Incoming Airflow", font_size=28, font="Consolas", color=WHITE)
        incoming_label.to_edge(LEFT).shift(UP * 2.5)
        
        self.play(Write(incoming_label))
        
        for i, arrow in enumerate(incoming_arrows):
            self.play(Create(arrow), run_time=0.3)
        self.wait(0.5)

        # === ANIMATE INCOMING FLOW MOVING TOWARD WING ===
        self.play(
            incoming_arrows.animate.shift(RIGHT * 2),
            run_time=2,
            rate_func=linear
        )
        self.wait(0.5)

        # === SHOW SPLIT POINT AT LEADING EDGE ===
        leading_edge_point = airfoil_filled.get_left()
        split_dot = Dot(leading_edge_point, color=YELLOW, radius=0.15)
        split_label = Text("Split Point", font_size=24, font="Consolas", color=YELLOW)
        split_label.next_to(split_dot, LEFT, buff=0.5)
        split_arrow = Arrow(split_label.get_right(), split_dot, color=YELLOW, buff=0.2)
        
        self.play(
            Create(split_dot),
            Write(split_label),
            Create(split_arrow),
            run_time=1.5
        )
        self.wait(0.5)

        # === CREATE UPPER FLOW STREAM LINES ===
        upper_stream_lines = VGroup()
        upper_colors = [RED, RED_D, RED_E]
        
        # Three streamlines flowing over the top
        upper_paths = [
            [
                [-3, 0.5, 0],   # Start at leading edge area
                [-1, 1.8, 0],   # Curve over top
                [1, 1.5, 0],    # Continue over
                [3, 0.8, 0],    # Exit at trailing edge
            ],
            [
                [-3, 1.0, 0],
                [-1, 2.2, 0],
                [1, 1.9, 0],
                [3, 1.2, 0],
            ],
            [
                [-3, 1.5, 0],
                [-1, 2.6, 0],
                [1, 2.3, 0],
                [3, 1.6, 0],
            ],
        ]
        
        for i, path in enumerate(upper_paths):
            # Create curved line for stream path
            stream_line = VMobject()
            stream_line.set_points_smoothly([np.array(p) for p in path])
            stream_line.set_color(upper_colors[i % len(upper_colors)])
            stream_line.set_stroke(width=3)
            upper_stream_lines.add(stream_line)
            
            # Add arrow at the end showing direction
            end_arrow = Arrow(
                start=path[2],
                end=path[3],
                color=upper_colors[i % len(upper_colors)],
                buff=0,
                max_tip_length_to_length_ratio=0.2,
                stroke_width=3
            )
            upper_stream_lines.add(end_arrow)
        
        # === CREATE LOWER FLOW STREAM LINES ===
        lower_stream_lines = VGroup()
        lower_colors = [BLUE, BLUE_D, BLUE_E]
        
        # Three streamlines flowing under the bottom
        lower_paths = [
            [
                [-3, -0.5, 0],  # Start at leading edge area
                [-1, -1.2, 0],  # Curve under bottom
                [1, -1.0, 0],   # Continue under
                [3, -0.3, 0],   # Exit at trailing edge
            ],
            [
                [-3, -1.0, 0],
                [-1, -1.6, 0],
                [1, -1.4, 0],
                [3, -0.7, 0],
            ],
            [
                [-3, -1.5, 0],
                [-1, -2.0, 0],
                [1, -1.8, 0],
                [3, -1.1, 0],
            ],
        ]
        
        for i, path in enumerate(lower_paths):
            stream_line = VMobject()
            stream_line.set_points_smoothly([np.array(p) for p in path])
            stream_line.set_color(lower_colors[i % len(lower_colors)])
            stream_line.set_stroke(width=3)
            lower_stream_lines.add(stream_line)
            
            end_arrow = Arrow(
                start=path[2],
                end=path[3],
                color=lower_colors[i % len(lower_colors)],
                buff=0,
                max_tip_length_to_length_ratio=0.2,
                stroke_width=3
            )
            lower_stream_lines.add(end_arrow)

        # === LABELS FOR FLOW PATHS ===
        upper_flow_label = Text("Upper Flow (Faster)", font_size=26, font="Consolas", color=RED)
        upper_flow_label.to_edge(UP).shift(DOWN * 1.5)
        
        lower_flow_label = Text("Lower Flow (Slower)", font_size=26, font="Consolas", color=BLUE)
        lower_flow_label.to_edge(DOWN).shift(UP * 1.5)
        
        # === ANIMATE STREAM LINES APPEARING ===
        self.play(Write(upper_flow_label), Write(lower_flow_label))
        
        # Animate upper stream lines drawing
        for stream in upper_stream_lines:
            self.play(Create(stream), run_time=0.5)
        self.wait(0.3)
        
        # Animate lower stream lines drawing
        for stream in lower_stream_lines:
            self.play(Create(stream), run_time=0.5)
        self.wait(0.3)

        # === ANIMATE FLOW MOVEMENT ALONG PATHS ===
        # Create small dots that travel along the stream lines
        upper_dots = VGroup()
        lower_dots = VGroup()
        
        for path in upper_paths:
            dot = Dot(path[0], color=RED, radius=0.08)
            upper_dots.add(dot)
        
        for path in lower_paths:
            dot = Dot(path[0], color=BLUE, radius=0.08)
            lower_dots.add(dot)
        
        self.play(FadeIn(upper_dots), FadeIn(lower_dots))
        
        # Animate dots moving along paths
        for i, dot in enumerate(upper_dots):
            path = upper_paths[i]
            self.play(
                MoveAlongPath(
                    dot,
                    VMobject().set_points_smoothly([np.array(p) for p in path])
                ),
                run_time=2,
                rate_func=linear
            )
        
        for i, dot in enumerate(lower_dots):
            path = lower_paths[i]
            self.play(
                MoveAlongPath(
                    dot,
                    VMobject().set_points_smoothly([np.array(p) for p in path])
                ),
                run_time=2,
                rate_func=linear
            )
        
        self.wait(0.5)

        # === FLOW SPLIT INFORMATION BOX ===
        info_box = Rectangle(width=6, height=3.5, color=WHITE, fill_opacity=0.1)
        info_box.to_edge(DOWN)
        
        info_title = Text("Flow Split Physics", font_size=32, font="Consolas", color=YELLOW)
        info_title.move_to(info_box.get_center()).shift(UP * 1.2)
        
        info_items = VGroup(
            Text("• Air hits the leading edge", font_size=24, font="Consolas", color=WHITE),
            Text("• Splits into upper and lower streams", font_size=24, font="Consolas", color=WHITE),
            Text("• Upper path: Longer, faster flow (red)", font_size=24, font="Consolas", color=RED),
            Text("• Lower path: Shorter, slower flow (blue)", font_size=24, font="Consolas", color=BLUE),
            Text("• Rejoins at trailing edge", font_size=24, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        
        info_items.next_to(info_title, DOWN, buff=0.3)
        info_items.move_to(info_box.get_center()).shift(DOWN * 0.3)
        
        self.play(
            Create(info_box),
            Write(info_title),
            Write(info_items),
            run_time=3
        )
        self.wait(1)

        # === PROGRESS TRACKER ===
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(info_box), FadeOut(info_title), FadeOut(info_items),
            FadeOut(incoming_label), FadeOut(split_label), FadeOut(split_arrow),
            FadeOut(split_dot), FadeOut(upper_flow_label), FadeOut(lower_flow_label),
            FadeOut(incoming_arrows), FadeOut(upper_stream_lines), FadeOut(lower_stream_lines),
            FadeOut(upper_dots), FadeOut(lower_dots)
        )
        
        progress_title = Text("150-Project Progress", font_size=36, color=GREEN)
        progress_title.to_edge(UP).shift(DOWN * 1)
        
        aircraft_progress = Text("Aircraft Design: Day 4/30", font_size=28, font="Consolas", color=GREEN)
        aircraft_progress.next_to(progress_title, DOWN, buff=0.3)
        
        total_progress = Text("Overall: 4/150 Complete (2.7%)", font_size=28, font="Consolas", color=YELLOW)
        total_progress.next_to(aircraft_progress, DOWN, buff=0.3)
        
        self.play(
            Write(progress_title),
            Write(aircraft_progress),
            Write(total_progress),
            run_time=2
        )
        self.wait(2)

        # === FINAL MESSAGE ===
        final_text = Text("✨ 146 Projects to Go! ✨", font_size=48, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)