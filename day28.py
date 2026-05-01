from manim import *
import numpy as np

class Day28(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 28: Climate Modeling", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Visualizing Global Climate Data", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE DUAL AXES (CO₂ and Temperature) ===
        axes = Axes(
            x_range=[1960, 2020, 10],
            y_range=[0, 100, 10],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE}
        )
        
        x_label = Text("Year", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Change (%)", font_size=24).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # === SIMULATED CLIMATE DATA ===
        # Real-world inspired data (simplified for visualization)
        years = np.arange(1960, 2021, 5)
        
        # CO₂ levels (ppm) - based on Mauna Loa data
        co2_data = [315, 320, 325, 330, 338, 345, 350, 355, 360, 370, 380, 390, 400, 410, 415]
        co2_normalized = [(c - 315) / 100 * 100 for c in co2_data]  # Normalize to percentage
        
        # Temperature anomaly (°C) - based on NASA GISS data
        temp_data = [-0.05, 0, 0.1, 0.2, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]
        temp_normalized = [(t + 0.05) / 1.15 * 100 for t in temp_data]  # Normalize to percentage

        # === PLOT CO₂ CURVE ===
        co2_label = Text("CO₂ Levels", font_size=24, font="Consolas", color=RED)
        co2_label.to_edge(RIGHT).shift(UP * 2)
        
        co2_graph = axes.plot_line_graph(
            x_values=years,
            y_values=co2_normalized,
            line_color=RED,
            stroke_width=3
        )
        
        self.play(Write(co2_label), Create(co2_graph), run_time=2)
        self.wait(0.5)

        # === PLOT TEMPERATURE CURVE ===
        temp_label = Text("Global Temperature", font_size=24, font="Consolas", color=ORANGE)
        temp_label.to_edge(RIGHT).shift(UP * 1.5)
        
        temp_graph = axes.plot_line_graph(
            x_values=years,
            y_values=temp_normalized,
            line_color=ORANGE,
            stroke_width=3
        )
        
        self.play(Write(temp_label), Create(temp_graph), run_time=2)
        self.wait(0.5)

        # === ADD DATA POINTS ===
        dots = VGroup()
        for i, year in enumerate(years[::3]):  # Show every 3rd point
            dot_co2 = Dot(
                axes.c2p(year, co2_normalized[i*3]),
                color=RED,
                radius=0.08
            )
            dot_temp = Dot(
                axes.c2p(year, temp_normalized[i*3]),
                color=ORANGE,
                radius=0.08
            )
            dots.add(dot_co2, dot_temp)
        
        self.play(Create(dots), run_time=1)
        self.wait(0.5)

        # === SHOW CORRELATION ===
        correlation_box = Rectangle(width=5, height=2, color=WHITE, fill_opacity=0.1)
        correlation_box.to_edge(DOWN)
        
        correlation_text = VGroup(
            Text("Key Findings:", font_size=28, font="Consolas", color=YELLOW),
            Text("• CO₂ increased by 32% since 1960", font_size=22, font="Consolas", color=WHITE),
            Text("• Temperature rose by 1.1°C", font_size=22, font="Consolas", color=WHITE),
            Text("• Strong correlation between CO₂ and temperature", font_size=22, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        correlation_text.move_to(correlation_box.get_center())
        
        self.play(Create(correlation_box), Write(correlation_text), run_time=2)
        self.wait(1)
        self.play(FadeOut(correlation_box), FadeOut(correlation_text))

        # === ANIMATE TREND LINE ===
        trend_label = Text("Projected Trend →", font_size=28, font="Consolas", color=GREEN)
        trend_label.to_edge(LEFT).shift(UP * 2)
        
        # Draw a projection line
        trend_line = Line(
            axes.c2p(1960, 10),
            axes.c2p(2030, 90),
            color=GREEN,
            stroke_width=2,
            stroke_opacity=0.5
        )
        
        self.play(Write(trend_label), Create(trend_line), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(trend_label), FadeOut(trend_line))

        # === IMPACT VISUALIZATION ===
        impact_title = Text("Climate Change Impacts", font_size=42, color=YELLOW)
        impact_title.to_edge(UP)
        self.play(Write(impact_title))
        
        impacts = VGroup(
            Text("🌊 Rising Sea Levels (coastal flooding)", font_size=26, font="Consolas", color=WHITE),
            Text("🌡️ More Extreme Weather Events", font_size=26, font="Consolas", color=WHITE),
            Text("🐻 Loss of Arctic Ice & Wildlife Habitat", font_size=26, font="Consolas", color=WHITE),
            Text("🌾 Agricultural Disruption & Food Security", font_size=26, font="Consolas", color=WHITE),
            Text("💧 Water Scarcity in Many Regions", font_size=26, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        impacts.next_to(impact_title, DOWN, buff=0.5)
        
        for impact in impacts:
            self.play(Write(impact), run_time=0.6)
            self.wait(0.1)
        
        self.wait(1)
        self.play(FadeOut(impact_title), FadeOut(impacts))

        # === SOLUTIONS ===
        solutions_title = Text("Potential Solutions", font_size=42, color=GREEN)
        solutions_title.to_edge(UP)
        self.play(Write(solutions_title))
        
        solutions = VGroup(
            Text("⚡ Transition to Renewable Energy", font_size=26, font="Consolas", color=WHITE),
            Text("🌳 Reforestation & Conservation", font_size=26, font="Consolas", color=WHITE),
            Text("🚗 Electric Vehicles & Public Transit", font_size=26, font="Consolas", color=WHITE),
            Text("🏭 Carbon Capture Technology", font_size=26, font="Consolas", color=WHITE),
            Text("🌍 International Cooperation (Paris Agreement)", font_size=26, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        solutions.next_to(solutions_title, DOWN, buff=0.5)
        
        for solution in solutions:
            self.play(Write(solution), run_time=0.6)
            self.wait(0.1)
        
        self.wait(1)
        self.play(FadeOut(solutions_title), FadeOut(solutions))

        # === CALL TO ACTION ===
        cta_box = Rectangle(width=6, height=2.5, color=GREEN, fill_opacity=0.1)
        cta_box.move_to(ORIGIN)
        
        cta_text = VGroup(
            Text("Every Degree Matters", font_size=36, font="Consolas", color=GREEN),
            Text("Every Action Counts", font_size=36, font="Consolas", color=GREEN),
            Text("The Time to Act is Now", font_size=36, font="Consolas", color=YELLOW)
        ).arrange(DOWN, buff=0.4)
        
        cta_text.move_to(cta_box.get_center())
        
        self.play(Create(cta_box), Write(cta_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(cta_box), FadeOut(cta_text))

        # === CLEAN UP GRAPH ===
        self.play(
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(co2_label), FadeOut(temp_label),
            FadeOut(co2_graph), FadeOut(temp_graph),
            FadeOut(dots)
        )

        # === FINAL MESSAGE ===
        final_text = Text("✨ Math Helps Us Understand Our Planet! ✨", font_size=42, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)