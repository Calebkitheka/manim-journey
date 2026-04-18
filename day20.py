from manim import *
import numpy as np

class Day20(Scene):
    def construct(self):
        # === OPENING TITLE ===
        title = Text("19 Days of Manim", font_size=60, color=YELLOW)
        subtitle = Text("Mid-Month Review & Celebration", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), Write(subtitle), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # === STATISTICS SHOWCASE ===
        stats_title = Text("By The Numbers", font_size=48, color=BLUE)
        stats_title.to_edge(UP)
        self.play(Write(stats_title))
        self.wait(0.5)

        stats = VGroup(
            Text("19 Days", font_size=32, font="Consolas", color=YELLOW),
            Text("19 Unique Animations", font_size=32, font="Consolas", color=GREEN),
            Text("100+ Git Commits", font_size=32, font="Consolas", color=BLUE),
            Text("19 YouTube Videos", font_size=32, font="Consolas", color=RED),
            Text("30 Days Goal", font_size=32, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        stats.next_to(stats_title, DOWN, buff=0.5)
        
        for stat in stats:
            self.play(Write(stat), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1)
        self.play(FadeOut(stats_title), FadeOut(stats))

        # === SKILLS ACQUIRED ===
        skills_title = Text("Skills Mastered", font_size=48, color=GREEN)
        skills_title.to_edge(UP)
        self.play(Write(skills_title))
        self.wait(0.5)

        skills = VGroup(
            Text("✓ Python Programming", font_size=28, font="Consolas"),
            Text("✓ Manim Animation Engine", font_size=28, font="Consolas"),
            Text("✓ 2D & 3D Visualizations", font_size=28, font="Consolas"),
            Text("✓ Calculus & Derivatives", font_size=28, font="Consolas"),
            Text("✓ Complex Numbers (Euler)", font_size=28, font="Consolas"),
            Text("✓ Fourier Series", font_size=28, font="Consolas"),
            Text("✓ Physics Simulations", font_size=28, font="Consolas"),
            Text("✓ Differential Equations (SIR)", font_size=28, font="Consolas"),
            Text("✓ Git & GitHub", font_size=28, font="Consolas"),
            Text("✓ YouTube Content Creation", font_size=28, font="Consolas")
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        skills.scale(0.8)
        skills.next_to(skills_title, DOWN, buff=0.5)
        
        # Animate skills appearing in groups
        for i in range(0, len(skills), 3):
            self.play(Write(skills[i:i+3]), run_time=1)
            self.wait(0.3)
        
        self.wait(1)
        self.play(FadeOut(skills_title), FadeOut(skills))

        # === BEST PROJECTS SHOWCASE ===
        projects_title = Text("Favorite Projects", font_size=48, color=PURPLE)
        projects_title.to_edge(UP)
        self.play(Write(projects_title))
        self.wait(0.5)

        projects = VGroup(
            Text("Day 6: Derivatives & Tangents", font_size=28, font="Consolas", color=YELLOW),
            Text("Day 12: Physics Pendulum", font_size=28, font="Consolas", color=BLUE),
            Text("Day 15: Euler's Formula", font_size=28, font="Consolas", color=GREEN),
            Text("Day 16: Fourier Series", font_size=28, font="Consolas", color=RED),
            Text("Day 18: 3D Surface Plots", font_size=28, font="Consolas", color=PURPLE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        projects.next_to(projects_title, DOWN, buff=0.5)
        
        for project in projects:
            self.play(Write(project), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1)
        self.play(FadeOut(projects_title), FadeOut(projects))

        # === LESSONS LEARNED ===
        lessons_title = Text("Key Lessons", font_size=48, color=ORANGE)
        lessons_title.to_edge(UP)
        self.play(Write(lessons_title))
        self.wait(0.5)

        lessons = VGroup(
            Text("1. Consistency > Perfection", font_size=28, font="Consolas", color=WHITE),
            Text("2. Errors Are Learning Opportunities", font_size=28, font="Consolas", color=WHITE),
            Text("3. Math Becomes Intuitive When Visualized", font_size=28, font="Consolas", color=WHITE),
            Text("4. Community & Sharing Accelerates Growth", font_size=28, font="Consolas", color=WHITE),
            Text("5. 30 Days is Just the Beginning", font_size=28, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        lessons.next_to(lessons_title, DOWN, buff=0.5)
        
        for lesson in lessons:
            self.play(Write(lesson), run_time=0.7)
            self.wait(0.3)
        
        self.wait(1)
        self.play(FadeOut(lessons_title), FadeOut(lessons))

        # === GITHUB STREAK VISUAL ===
        streak_title = Text("GitHub Streak", font_size=48, color=GREEN)
        streak_title.to_edge(UP)
        self.play(Write(streak_title))
        self.wait(0.5)

        # Create 19 green squares to represent the streak
        squares = VGroup()
        for i in range(19):
            sq = Square(side_length=0.3, color=GREEN, fill_opacity=1)
            sq.shift(RIGHT * i * 0.35)
            squares.add(sq)
        
        squares.center()
        squares.next_to(streak_title, DOWN, buff=0.5)
        
        self.play(Create(squares), run_time=2)
        self.wait(1)
        self.play(FadeOut(streak_title), FadeOut(squares))

        # === FINAL MESSAGE ===
        final_title = Text("Day 20 Complete!", font_size=60, color=YELLOW)
        final_title.to_edge(UP)
        
        halfway = Text("Halfway to 30 Days!", font_size=40, color=WHITE)
        halfway.next_to(final_title, DOWN)
        
        github_link = Text("github.com/Calebkitheka/manim-journey", font_size=24, color=BLUE)
        github_link.to_edge(DOWN)
        
        self.play(Write(final_title), Write(halfway), Write(github_link), run_time=3)
        self.wait(3)

        # === COUNTDOWN TO DAY 30 ===
        countdown = Text("10 Days Remaining...", font_size=48, color=RED)
        countdown.to_edge(DOWN)
        
        self.play(
            FadeOut(final_title), FadeOut(halfway),
            Write(countdown),
            run_time=2
        )
        self.wait(2)