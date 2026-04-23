from manim import *
import numpy as np

class Day23(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 23: Neural Networks", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("How Artificial Intelligence Learns", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === NEURAL NETWORK ARCHITECTURE ===
        # Use simple numbers for x positions instead of Manim vectors
        layer_positions = [-4, 0, 4]  # LEFT * 4, ORIGIN, RIGHT * 4 as numbers
        neuron_counts = [4, 5, 2]
        layer_names = ["Input Layer", "Hidden Layer", "Output Layer"]
        colors = [BLUE, GREEN, RED]
        
        all_neurons = []
        all_labels = []
        
        # Create neurons for each layer
        for layer_idx, (x_pos, count, name, color) in enumerate(
            zip(layer_positions, neuron_counts, layer_names, colors)
        ):
            layer_neurons = VGroup()
            y_spacing = 1.5
            start_y = (count - 1) * y_spacing / 2
            
            for i in range(count):
                neuron = Circle(radius=0.3, color=color, fill_opacity=0.8)
                # FIXED: Use simple x coordinate number
                neuron.move_to([x_pos, start_y - i * y_spacing, 0])
                layer_neurons.add(neuron)
            
            # Layer label
            label = Text(name, font_size=24, font="Consolas", color=color)
            label.next_to(layer_neurons, DOWN, buff=0.5)
            all_labels.append(label)
            all_neurons.append(layer_neurons)
        
        # === ANIMATE NEURONS APPEARING ===
        for i, layer in enumerate(all_neurons):
            self.play(Create(layer), Write(all_labels[i]), run_time=1)
            self.wait(0.3)
        
        self.wait(0.5)

        # === CREATE CONNECTIONS (Synapses) ===
        connections = VGroup()
        
        # Connect each layer to the next
        for layer_idx in range(len(all_neurons) - 1):
            current_layer = all_neurons[layer_idx]
            next_layer = all_neurons[layer_idx + 1]
            
            for neuron1 in current_layer:
                for neuron2 in next_layer:
                    line = Line(
                        neuron1.get_center(),
                        neuron2.get_center(),
                        color=WHITE,
                        stroke_width=1,
                        stroke_opacity=0.5
                    )
                    connections.add(line)
        
        self.play(Create(connections), run_time=2)
        self.wait(0.5)

        # === ANIMATE SIGNAL FLOW ===
        signal_label = Text("Signal Flow →", font_size=28, font="Consolas", color=YELLOW)
        signal_label.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(signal_label))
        
        # Animate pulses traveling through connections
        for layer_idx in range(len(all_neurons) - 1):
            current_layer = all_neurons[layer_idx]
            next_layer = all_neurons[layer_idx + 1]
            
            for neuron1 in current_layer:
                for neuron2 in next_layer:
                    pulse = Dot(neuron1.get_center(), color=YELLOW, radius=0.1)
                    self.add(pulse)
                    self.play(
                        MoveAlongPath(
                            pulse,
                            Line(neuron1.get_center(), neuron2.get_center())
                        ),
                        run_time=0.3
                    )
                    self.remove(pulse)
        
        self.wait(0.5)
        self.play(FadeOut(signal_label))

        # === DISPLAY NETWORK INFO ===
        info_box = Rectangle(width=5, height=2.5, color=WHITE, fill_opacity=0.1)
        info_box.to_edge(DOWN)
        
        network_info = VGroup(
            Text("Architecture: 4 → 5 → 2", font_size=24, font="Consolas", color=WHITE),
            Text("Weights: Learned Parameters", font_size=24, font="Consolas", color=WHITE),
            Text("Activation: Neuron Fires", font_size=24, font="Consolas", color=WHITE),
            Text("Output: Prediction/Classification", font_size=24, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        network_info.move_to(info_box.get_center())
        
        self.play(Create(info_box), Write(network_info), run_time=2)
        self.wait(1)
        self.play(FadeOut(info_box), FadeOut(network_info))

        # === SHOW LEARNING PROCESS ===
        learning_title = Text("Training Process", font_size=36, color=GREEN)
        learning_title.to_edge(UP)
        self.play(Write(learning_title))
        
        training_steps = VGroup(
            Text("1. Forward Pass (Make Prediction)", font_size=24, font="Consolas", color=BLUE),
            Text("2. Calculate Loss (Error)", font_size=24, font="Consolas", color=YELLOW),
            Text("3. Backpropagation (Adjust Weights)", font_size=24, font="Consolas", color=RED),
            Text("4. Repeat Until Accurate", font_size=24, font="Consolas", color=GREEN)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        training_steps.next_to(learning_title, DOWN, buff=0.5)
        
        for step in training_steps:
            self.play(Write(step), run_time=0.7)
            self.wait(0.2)
        
        self.wait(1)
        self.play(FadeOut(learning_title), FadeOut(training_steps))

        # === REAL-WORLD APPLICATIONS ===
        applications_title = Text("Real-World Applications", font_size=36, color=PURPLE)
        applications_title.to_edge(UP)
        self.play(Write(applications_title))
        
        applications = VGroup(
            Text("🏥 Medical Diagnosis", font_size=24, font="Consolas", color=WHITE),
            Text("🚗 Self-Driving Cars", font_size=24, font="Consolas", color=WHITE),
            Text("💬 Language Translation", font_size=24, font="Consolas", color=WHITE),
            Text("🎨 Image Generation (AI Art)", font_size=24, font="Consolas", color=WHITE),
            Text("📈 Stock Market Prediction", font_size=24, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        applications.next_to(applications_title, DOWN, buff=0.5)
        
        for app in applications:
            self.play(Write(app), run_time=0.5)
            self.wait(0.1)
        
        self.wait(1)
        self.play(FadeOut(applications_title), FadeOut(applications))

        # === FINAL MESSAGE ===
        final_text = Text("✨ AI Learns from Data! ✨", font_size=48, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)