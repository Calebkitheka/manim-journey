from manim import *
import numpy as np

class Day25(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 25: Fluid Dynamics", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Simulating Particle Flow", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE CONTAINER ===
        container = Rectangle(
            width=10,
            height=6,
            color=WHITE,
            stroke_width=3
        )
        self.play(Create(container))
        self.wait(0.5)

        # === FLUID PARTICLES ===
        num_particles = 50
        particles = VGroup()
        # FIXED: Use only valid Manim colors
        particle_colors = [BLUE, BLUE_E, GREEN, TEAL, PURPLE]
        
        np.random.seed(42)
        particle_data = []
        
        for i in range(num_particles):
            x = np.random.uniform(-4, 4)
            y = np.random.uniform(-2, 2)
            color = particle_colors[i % len(particle_colors)]
            
            particle = Dot(
                point=[x, y, 0],
                color=color,
                radius=0.15
            )
            particles.add(particle)
            
            particle_data.append({
                'dot': particle,
                'vx': np.random.uniform(-0.5, 0.5),
                'vy': np.random.uniform(-0.5, 0.5)
            })
        
        self.play(Create(particles), run_time=2)
        self.wait(0.5)

        # === FLOW FIELD VISUALIZATION ===
        flow_field = VGroup()
        for x in np.arange(-4, 4, 1):
            for y in np.arange(-2, 2, 1):
                dx = -y * 0.3
                dy = x * 0.3
                arrow = Arrow(
                    start=[x, y, 0],
                    end=[x + dx, y + dy, 0],
                    color=GRAY,
                    stroke_width=1,
                    max_tip_length_to_length_ratio=0.2,
                    stroke_opacity=0.5
                )
                flow_field.add(arrow)
        
        self.play(Create(flow_field), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(flow_field))

        # === ANIMATE PARTICLE MOVEMENT ===
        time_tracker = ValueTracker(0)
        
        # FIXED: Complete the for-loop properly
        for data in particle_data:
            dot = data['dot']
            
            def update_particle(p, dt, data=data, tracker=time_tracker):
                new_x = p.get_x() + data['vx'] * dt * 2
                new_y = p.get_y() + data['vy'] * dt * 2
                
                if new_x > 4 or new_x < -4:
                    data['vx'] *= -1
                if new_y > 2 or new_y < -2:
                    data['vy'] *= -1
                
                data['vy'] += np.sin(tracker.get_value() * 0.5) * 0.01
                
                p.move_to([new_x, new_y, 0])
            
            dot.add_updater(update_particle)
        
        self.add(particles)
        self.play(
            time_tracker.animate.set_value(10),
            run_time=5,
            rate_func=linear
        )
        
        # FIXED: Complete the for-loop properly
        for data in particle_data:
            data['dot'].clear_updaters()
        
        self.wait(0.5)

        # === ADD OBSTACLE ===
        obstacle = Circle(radius=0.8, color=RED, fill_opacity=0.5)
        obstacle.move_to([0, 0, 0])
        
        obstacle_label = Text("Obstacle", font_size=24, color=RED)
        obstacle_label.next_to(obstacle, DOWN, buff=0.3)
        
        self.play(Create(obstacle), Write(obstacle_label))
        self.wait(0.5)

        # === PARTICLES FLOWING AROUND OBSTACLE ===
        for i, data in enumerate(particle_data):
            data['dot'].move_to([-4 + (i % 10) * 0.5, -2 + (i // 10) * 0.5, 0])
            data['vx'] = 0.3
            data['vy'] = 0
        
        self.play(FadeIn(particles))
        self.wait(0.5)
        
        for data in particle_data:
            dot = data['dot']
            
            def flow_around_obstacle(p, dt, data=data):
                x = p.get_x()
                y = p.get_y()
                
                data['vx'] = 0.2
                
                dist_to_obstacle = np.sqrt(x**2 + y**2)
                if dist_to_obstacle < 2:
                    angle = np.arctan2(y, x)
                    data['vy'] = np.sin(angle) * 0.3
                
                if x > 4:
                    data['vx'] = -0.2
                if x < -4:
                    data['vx'] = 0.2
                if y > 2 or y < -2:
                    data['vy'] *= -1
                
                p.shift([data['vx'] * dt, data['vy'] * dt, 0])
            
            dot.add_updater(flow_around_obstacle)
        
        self.add(particles)
        self.play(
            time_tracker.animate.set_value(20),
            run_time=5,
            rate_func=linear
        )
        
        # FIXED: Complete the for-loop properly
        for data in particle_data:
            data['dot'].clear_updaters()
        
        self.wait(0.5)

        # === FLUID DYNAMICS INFO ===
        info_box = Rectangle(width=5, height=2.5, color=WHITE, fill_opacity=0.1)
        info_box.to_edge(DOWN)
        
        fluid_info = VGroup(
            Text("Navier-Stokes Equations", font_size=24, font="Consolas", color=YELLOW),
            Text("• Conservation of Mass", font_size=20, font="Consolas", color=WHITE),
            Text("• Conservation of Momentum", font_size=20, font="Consolas", color=WHITE),
            Text("• Viscosity & Pressure", font_size=20, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        fluid_info.move_to(info_box.get_center())
        
        self.play(Create(info_box), Write(fluid_info), run_time=2)
        self.wait(1)
        self.play(FadeOut(info_box), FadeOut(fluid_info))

        # === REAL-WORLD APPLICATIONS ===
        apps_title = Text("Real-World Applications", font_size=36, color=GREEN)
        apps_title.to_edge(UP)
        self.play(Write(apps_title))
        
        applications = VGroup(
            Text("Aerodynamics (Aircraft Design)", font_size=24, font="Consolas", color=WHITE),
            Text("Ocean Current Modeling", font_size=24, font="Consolas", color=WHITE),
            Text("Blood Flow in Arteries", font_size=24, font="Consolas", color=WHITE),
            Text("Weather Prediction", font_size=24, font="Consolas", color=WHITE),
            Text("Video Game Physics", font_size=24, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        applications.next_to(apps_title, DOWN, buff=0.5)
        
        for app in applications:
            self.play(Write(app), run_time=0.5)
            self.wait(0.1)
        
        self.wait(1)
        self.play(FadeOut(apps_title), FadeOut(applications))

        # === FINAL MESSAGE ===
        # FIXED: Use valid color (GREEN instead of CYAN)
        final_text = Text("✨ Fluids Flow by Physics! ✨", font_size=48, color=GREEN)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)