from manim import *
import random

class Day10(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 10: Probability Simulator", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Coin Flip Simulation", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(0.5)

        # === CREATE COIN VISUAL ===
        coin = Circle(radius=1, color=WHITE, fill_opacity=1)
        coin.move_to(ORIGIN)
        
        # Heads side (H)
        heads_text = Text("H", font_size=48, color=GOLD)
        heads_text.move_to(coin.get_center())
        
        # Tails side (T) - FIXED: Use GRAY instead of SILVER
        tails_text = Text("T", font_size=48, color=GRAY)
        tails_text.move_to(coin.get_center())
        
        # Start with Heads visible
        coin_group = VGroup(coin, heads_text)
        self.play(Create(coin), Write(heads_text))
        self.wait(0.5)

        # === CREATE COUNTERS ===
        heads_count = 0
        tails_count = 0
        
        # Display counters
        heads_label = Text("Heads: 0", font_size=32, color=GOLD)
        heads_label.to_edge(LEFT).shift(UP * 2)
        
        # FIXED: Use GRAY instead of SILVER
        tails_label = Text("Tails: 0", font_size=32, color=GRAY)
        tails_label.to_edge(RIGHT).shift(UP * 2)
        
        self.play(Write(heads_label), Write(tails_label))
        self.wait(0.5)

        # === CREATE PERCENTAGE BAR ===
        bar_background = Rectangle(width=6, height=0.5, color=WHITE)
        bar_background.to_edge(DOWN)
        
        bar_fill = Rectangle(width=0, height=0.5, color=GOLD, fill_opacity=1)
        bar_fill.next_to(bar_background, LEFT, buff=0, aligned_edge=LEFT)
        
        percentage_text = Text("50%", font_size=28)
        percentage_text.next_to(bar_background, UP)
        
        self.play(Create(bar_background), Create(bar_fill), Write(percentage_text))
        self.wait(0.5)

        # === SIMULATE COIN FLIPS ===
        num_flips = 50
        
        for i in range(num_flips):
            result = random.randint(0, 1)
            
            if result == 0:
                heads_count += 1
                self.play(
                    Rotate(coin, angle=PI, axis=RIGHT),
                    run_time=0.2
                )
                coin.set_color(WHITE)
                heads_text.set_color(GOLD)
                # FIXED: Use GRAY instead of SILVER
                tails_text.set_color(GRAY)
            else:
                tails_count += 1
                self.play(
                    Rotate(coin, angle=PI, axis=RIGHT),
                    run_time=0.2
                )
                coin.set_color(WHITE)
                heads_text.set_color(GRAY)
                tails_text.set_color(GOLD)
            
            # Update counter labels
            heads_label.become(Text(f"Heads: {heads_count}", font_size=32, color=GOLD).to_edge(LEFT).shift(UP * 2))
            tails_label.become(Text(f"Tails: {tails_count}", font_size=32, color=GRAY).to_edge(RIGHT).shift(UP * 2))
            
            # Update percentage bar
            total = heads_count + tails_count
            heads_percentage = (heads_count / total) * 100
            bar_fill.set_width(6 * (heads_percentage / 100))
            percentage_text.become(Text(f"{heads_percentage:.1f}%", font_size=28).next_to(bar_background, UP))
            
            if i > 20:
                self.wait(0.05)
            else:
                self.wait(0.1)

        self.wait(1)

        # === FINAL MESSAGE ===
        final_text = Text("✨ Law of Large Numbers! ✨", font_size=36, color=GREEN)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)