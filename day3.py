from manim import *

class Day3(Scene):
    def construct(self):
        # === PART 1: DISPLAYING TEXT ===
        # Regular text (uses system fonts)
        title = Text("Day 3: Text & Math!", font_size=48, color=YELLOW)
        title.to_edge(UP)
        
        # Subtitle with fade-in animation
        subtitle = Text("Animating equations with Manim", font_size=32)
        subtitle.next_to(title, DOWN)
        
        # === PART 2: MATHEMATICAL EQUATIONS ===
        # MathTex: For LaTeX-style math (requires LaTeX installed)
        # If you get LaTeX errors, see troubleshooting below!
        equation = MathTex("x^2 + y^2 = r^2", font_size=40)
        equation.next_to(subtitle, DOWN, buff=1)
        
        # Tex: For mixed text and math
        explanation = Tex("The Pythagorean Theorem:", font_size=36)
        explanation.next_to(equation, DOWN, buff=0.5)
        
        # === PART 3: BASIC ANIMATIONS ===
        # Animate text appearing
        self.play(Write(title))           # Typewriter effect
        self.play(FadeIn(subtitle))       # Smooth fade in
        
        # Wait 1 second before continuing
        self.wait(1)
        
        # Animate equation appearing
        self.play(Create(equation))       # Draws the equation stroke by stroke
        self.play(FadeIn(explanation))    # Fade in the explanation
        
        # === PART 4: TRANSFORMING TEXT ===
        # Transform one equation into another!
        new_equation = MathTex("a^2 + b^2 = c^2", font_size=40)
        new_equation.move_to(equation)    # Place it in the same spot
        
        self.wait(1)
        self.play(Transform(equation, new_equation))  # Morph old → new
        
        # === PART 5: FINAL MESSAGE ===
        final_text = Text("✨ Math is Beautiful ✨", color=GREEN)
        final_text.scale(1.2)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text))
        self.wait(2)  # Hold final frame for 2 seconds