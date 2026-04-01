from manim import *

class Day9(ThreeDScene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 9: 3D Objects & Camera", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === PART 1: SETUP 3D AXES ===
        # ThreeDAxes gives us X, Y, and Z axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            z_length=4,
            axis_config={"color": BLUE}
        )
        
        # Add axis labels
        x_label = Text("x", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=24).next_to(axes.y_axis, UP)
        z_label = Text("z", font_size=24).next_to(axes.z_axis, UP)
        
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label), Write(z_label))
        self.wait(1)

        # === PART 2: SET CAMERA ORIENTATION ===
        # Default view is often flat. Let's tilt it to see 3D.
        # phi = angle from Z-axis, theta = rotation around Z-axis
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait(1)

        # === PART 3: CREATE 3D OBJECTS ===
        # Sphere
        sphere = Sphere(radius=1, color=RED, fill_opacity=0.5)
        sphere.shift(LEFT * 2)
        
        # Cube
        cube = Cube(side_length=1.5, color=GREEN, fill_opacity=0.5)
        cube.shift(RIGHT * 2)
        
        self.play(Create(sphere), Create(cube))
        self.wait(1)

        # === PART 4: ROTATE OBJECTS IN 3D ===
        # Rotate the sphere around the Y-axis
        self.play(Rotate(sphere, angle=PI, axis=UP), run_time=2)
        
        # Rotate the cube around the X-axis
        self.play(Rotate(cube, angle=PI, axis=RIGHT), run_time=2)
        self.wait(1)

        # === PART 5: MOVE THE CAMERA ===
        # Animate the camera moving around the objects
        self.move_camera(phi=75 * DEGREES, theta=120 * DEGREES, run_time=3)
        self.wait(1)

        # === PART 6: RETURN TO 2D VIEW (Optional) ===
        # Flatten the camera to show 2D projection
        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, run_time=2)
        self.wait(1)

        # === FINAL MESSAGE ===
        final_text = Text("✨ Welcome to the 3rd Dimension! ✨", font_size=36, color=WHITE)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)