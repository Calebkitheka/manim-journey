from manim import *

class AircraftDay01(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("150-Project Journey: Aircraft Design", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        subtitle = Text("Day 1: Draw an Airfoil Shape", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE AIRFOIL SHAPE (NACA 4-digit airfoil approximation) ===
        # Using Bezier curves to create a wing cross-section
        
        # Upper surface control points (curved)
        upper_points = [
            [-3, 0, 0],      # Leading edge
            [-2, 0.8, 0],    # Upper curve start
            [0, 1.2, 0],     # Upper peak
            [2, 0.9, 0],     # Upper curve end
            [3, 0.3, 0],     # Trailing edge
        ]
        
        # Lower surface control points (flatter)
        lower_points = [
            [3, 0.3, 0],     # Trailing edge
            [2, -0.3, 0],    # Lower curve end
            [0, -0.5, 0],    # Lower peak
            [-2, -0.4, 0],   # Lower curve start
            [-3, 0, 0],      # Leading edge
        ]
        
        # Create Bezier curves for upper and lower surfaces
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
        
        # Connect trailing edge
        trailing_edge = Line(
            upper_points[4],
            lower_points[0],
            color=BLUE,
            stroke_width=4
        )
        
        airfoil = VGroup(upper_curve, lower_curve, trailing_edge)
        airfoil.scale(1.5)
        airfoil.move_to(ORIGIN)
        
        # === ANIMATE AIRFOIL DRAWING ===
        self.play(
            Create(upper_curve),
            run_time=2
        )
        self.play(
            Create(lower_curve),
            run_time=2
        )
        self.play(
            Create(trailing_edge),
            run_time=1
        )
        self.wait(0.5)

        # === FILL THE AIRFOIL ===
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
            FadeIn(airfoil_filled),
            run_time=1
        )
        self.wait(0.5)

        # === LABELS ===
        leading_label = Text("Leading Edge", font_size=24, color=WHITE)
        leading_label.next_to(airfoil, LEFT, buff=0.5)
        leading_arrow = Arrow(leading_label.get_right(), airfoil.get_left(), color=WHITE)
        
        trailing_label = Text("Trailing Edge", font_size=24, color=WHITE)
        trailing_label.next_to(airfoil, RIGHT, buff=0.5)
        trailing_arrow = Arrow(trailing_label.get_left(), airfoil.get_right(), color=WHITE)
        
        upper_label = Text("Upper Surface", font_size=24, color=WHITE)
        upper_label.next_to(airfoil, UP, buff=0.5)
        
        lower_label = Text("Lower Surface", font_size=24, color=WHITE)
        lower_label.next_to(airfoil, DOWN, buff=0.5)
        
        self.play(
            Write(leading_label), Create(leading_arrow),
            Write(trailing_label), Create(trailing_arrow),
            Write(upper_label),
            Write(lower_label),
            run_time=2
        )
        self.wait(1)

        # === AIRFOIL INFO BOX ===
        info_box = Rectangle(width=5, height=2.5, color=WHITE, fill_opacity=0.1)
        info_box.to_edge(DOWN)
        
        info_text = VGroup(
            Text("NACA 4-Digit Airfoil", font_size=28, font="Consolas", color=YELLOW),
            Text("• First digit: Maximum camber (%)", font_size=22, font="Consolas", color=WHITE),
            Text("• Second digit: Position of max camber", font_size=22, font="Consolas", color=WHITE),
            Text("• Last two digits: Max thickness (%)", font_size=22, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        info_text.move_to(info_box.get_center())
        
        self.play(Create(info_box), Write(info_text), run_time=2)
        self.wait(1)

        # === PROGRESS TRACKER ===
        progress_title = Text("150-Project Progress", font_size=36, color=GREEN)
        progress_title.to_edge(UP).shift(DOWN * 1)
        
        progress_text = Text("Aircraft Design: Day 1/30", font_size=28, font="Consolas", color=GREEN)
        progress_text.next_to(progress_title, DOWN, buff=0.3)
        
        total_progress = Text("Overall: 1/150 Complete", font_size=28, font="Consolas", color=YELLOW)
        total_progress.next_to(progress_text, DOWN, buff=0.3)
        
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(info_box), FadeOut(info_text),
            Write(progress_title), Write(progress_text), Write(total_progress),
            run_time=2
        )
        self.wait(2)

        # === FINAL MESSAGE ===
        final_text = Text("✨ 149 Projects to Go! ✨", font_size=48, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)