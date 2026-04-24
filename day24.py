from manim import *
import numpy as np

class Day24(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 24: The Mandelbrot Set", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Infinite Complexity from z² + c", font_size=32, font="Consolas", color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE COMPLEX PLANE ===
        axes = Axes(
            x_range=[-2.5, 1, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=7,
            y_length=6,
            axis_config={"color": BLUE}
        )
        
        real_label = Text("Re", font_size=24).next_to(axes.x_axis, RIGHT)
        imag_label = Text("Im", font_size=24).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(real_label), Write(imag_label))
        self.wait(0.5)

        # === MANDELBROT GENERATION FUNCTION ===
        def mandelbrot(c, max_iter=50):
            """Calculate Mandelbrot set membership for complex number c"""
            z = 0
            for n in range(max_iter):
                if abs(z) > 2:
                    return n / max_iter
                z = z**2 + c
            return 1

        # === CREATE MANDELBROT IMAGE ===
        # Use smaller dimensions for faster rendering
        width, height = 200, 150
        x_min, x_max = -2.5, 1
        y_min, y_max = -1.5, 1.5
        
        # Create image array (uint8, 0-255 range for ImageMobject)
        image_data = np.zeros((height, width, 3), dtype=np.uint8)
        
        for py in range(height):
            for px in range(width):
                # Map pixel to complex plane
                x = x_min + (px / width) * (x_max - x_min)
                y = y_min + (py / height) * (y_max - y_min)
                c = complex(x, y)
                
                # Calculate Mandelbrot value
                value = mandelbrot(c, max_iter=50)
                
                # Color mapping (0-255 range for uint8)
                if value == 1:
                    color = [0, 0, 0]  # Black for inside set
                else:
                    # Smooth color gradient (0-255 range)
                    color = [
                        int(128 + 127 * np.sin(value * 3)),
                        int(128 + 127 * np.sin(value * 3 + 2)),
                        int(128 + 127 * np.sin(value * 3 + 4))
                    ]
                image_data[py, px] = color

        # === DISPLAY THE FRACTAL ===
        # FIXED: ImageMobject infers dimensions from array
        mandelbrot_image = ImageMobject(image_data)
        mandelbrot_image.scale(0.02)  # Scale to fit scene
        mandelbrot_image.move_to(ORIGIN)
        
        self.play(FadeIn(mandelbrot_image), run_time=3)
        self.wait(1)

        # === FORMULA DISPLAY ===
        formula_box = Rectangle(width=4, height=1.5, color=WHITE, fill_opacity=0.1)
        formula_box.to_edge(RIGHT).shift(UP * 1)
        
        formula_text = VGroup(
            Text("zₙ₊₁ = zₙ² + c", font_size=32, font="Consolas", color=YELLOW),
            Text("z₀ = 0", font_size=24, font="Consolas", color=WHITE),
            Text("If |z| > 2 → Escapes", font_size=20, font="Consolas", color=RED)
        ).arrange(DOWN, buff=0.2)
        
        formula_text.move_to(formula_box.get_center())
        
        self.play(Create(formula_box), Write(formula_text))
        self.wait(1)

        # === ZOOM ANIMATION CONCEPT ===
        zoom_box = Rectangle(
            width=0.8,
            height=0.8,
            color=GREEN,
            stroke_width=2
        )
        zoom_box.move_to(axes.c2p(-0.75, 0.1))
        
        zoom_label = Text("Zoom → Infinite Detail", font_size=20, color=GREEN)
        zoom_label.next_to(zoom_box, RIGHT, buff=0.2)
        
        self.play(Create(zoom_box), Write(zoom_label))
        self.wait(1)
        
        self.play(
            zoom_box.animate.scale(1.2),
            rate_func=there_and_back,
            run_time=1
        )
        self.play(
            zoom_box.animate.scale(0.8),
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(0.5)
        
        self.play(FadeOut(zoom_box), FadeOut(zoom_label))

        # === FUN FACTS ===
        facts_title = Text("Mind-Blowing Facts", font_size=36, color=PURPLE)
        facts_title.to_edge(UP)
        self.play(Write(facts_title))
        
        facts = VGroup(
            Text("🌀 Boundary has infinite length", font_size=24, font="Consolas", color=WHITE),
            Text("🔍 Every zoom reveals new patterns", font_size=24, font="Consolas", color=WHITE),
            Text("🌊 Contains mini-Mandelbrots", font_size=24, font="Consolas", color=WHITE),
            Text("🧮 Defined by simple iteration", font_size=24, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        facts.next_to(facts_title, DOWN, buff=0.5)
        
        for fact in facts:
            self.play(Write(fact), run_time=0.7)
            self.wait(0.2)
        
        self.wait(1)
        self.play(FadeOut(facts_title), FadeOut(facts))

        # === FINAL MESSAGE ===
        final_text = Text("✨ Infinity in a Formula! ✨", font_size=48, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)