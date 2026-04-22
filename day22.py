from manim import *
import numpy as np

class Day22(ThreeDScene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 22: General Relativity", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Gravity is Spacetime Curvature", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === SET 3D CAMERA ORIENTATION ===
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=30 * DEGREES,
            zoom=0.9
        )

        # === CREATE 3D AXES ===
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-2, 2, 1],
            x_length=8,
            y_length=8,
            z_length=4,
            axis_config={"color": BLUE}
        )
        
        self.play(Create(axes), run_time=2)
        self.wait(0.5)

        # === SPACETIME GRID (Flat - No Mass) ===
        flat_grid = Surface(
            lambda u, v: axes.c2p(u, v, 0),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_color=GRAY,
            fill_opacity=0.3,
            stroke_color=WHITE,
            stroke_width=1
        )
        
        flat_label = Text("Flat Spacetime (No Mass)", font_size=24, font="Consolas", color=WHITE)
        flat_label.to_edge(RIGHT).shift(UP * 2)
        
        self.play(Create(flat_grid), Write(flat_label), run_time=2)
        self.wait(1)

        # === TRANSFORM TO CURVED SPACETIME ===
        # Spacetime curvature around a mass (like a star/black hole)
        # z = -1/r where r = sqrt(x² + y²)
        
        def spacetime_curvature(u, v):
            r = np.sqrt(u**2 + v**2)
            # Avoid division by zero at center
            if r < 0.3:
                r = 0.3
            z = -1 / r
            return axes.c2p(u, v, z)
        
        curved_grid = Surface(
            spacetime_curvature,
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=YELLOW,
            stroke_width=1
        )
        
        curved_label = Text("Curved Spacetime (With Mass)", font_size=24, font="Consolas", color=YELLOW)
        curved_label.to_edge(RIGHT).shift(UP * 2)
        
        # Animate the transformation
        self.play(
            Transform(flat_grid, curved_grid),
            Transform(flat_label, curved_label),
            run_time=3
        )
        self.wait(1)

        # === ADD MASS OBJECT (Star/Black Hole) ===
        mass_sphere = Sphere(radius=0.5, color=RED, fill_opacity=0.8)
        mass_sphere.move_to(axes.c2p(0, 0, -2))
        
        mass_label = Text("Mass (Star)", font_size=24, font="Consolas", color=RED)
        mass_label.to_edge(RIGHT).shift(DOWN * 1)
        
        self.play(Create(mass_sphere), Write(mass_label), run_time=2)
        self.wait(1)

        # === ANIMATE CAMERA ROTATION ===
        # Show the curvature from different angles
        self.move_camera(
            phi=70 * DEGREES,
            theta=120 * DEGREES,
            run_time=3
        )
        self.wait(0.5)

        self.move_camera(
            phi=70 * DEGREES,
            theta=210 * DEGREES,
            run_time=3
        )
        self.wait(0.5)

        # === ORBITING OBJECT (Planet) ===
        # Show how objects follow the curvature (orbit)
        orbit_path = ParametricFunction(
            lambda t: axes.c2p(
                2 * np.cos(t),
                2 * np.sin(t),
                -0.5  # Slightly above the curvature
            ),
            t_range=[0, 2 * PI],
            color=GREEN,
            stroke_width=2
        )
        
        orbit_label = Text("Orbit = Following Curvature", font_size=24, font="Consolas", color=GREEN)
        orbit_label.to_edge(LEFT).shift(UP * 2)
        
        self.play(Create(orbit_path), Write(orbit_label), run_time=2)
        self.wait(1)

        # === EINSTEIN'S FIELD EQUATION ===
        # Simplified visualization (not rendering full tensor equation)
        einstein_text = Text(
            "Matter tells spacetime how to curve,",
            font_size=24,
            font="Consolas",
            color=WHITE
        )
        einstein_text.to_edge(DOWN).shift(UP * 0.5)
        
        einstein_text2 = Text(
            "Spacetime tells matter how to move.",
            font_size=24,
            font="Consolas",
            color=WHITE
        )
        einstein_text2.next_to(einstein_text, DOWN, buff=0.3)
        
        self.play(Write(einstein_text), Write(einstein_text2), run_time=3)
        self.wait(2)

        # === FINAL MESSAGE ===
        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, run_time=2)
        
        final_text = Text("✨ Gravity is Geometry! ✨", font_size=48, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(
            FadeOut(einstein_text), FadeOut(einstein_text2),
            Write(final_text),
            run_time=2
        )
        self.wait(2)