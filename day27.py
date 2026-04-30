from manim import *
import numpy as np

class Day27(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 27: Neural Network Training", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("Watching AI Learn in Real-Time", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === CREATE NEURAL NETWORK ===
        layer_positions = [-4, 0, 4]
        neuron_counts = [3, 4, 2]
        layer_names = ["Input", "Hidden", "Output"]
        colors = [BLUE, GREEN, RED]
        
        all_neurons = []
        all_labels = []
        
        for layer_idx, (x_pos, count, name, color) in enumerate(
            zip(layer_positions, neuron_counts, layer_names, colors)
        ):
            layer_neurons = VGroup()
            y_spacing = 1.5
            start_y = (count - 1) * y_spacing / 2
            
            for i in range(count):
                neuron = Circle(radius=0.3, color=color, fill_opacity=0.8)
                neuron.move_to([x_pos, start_y - i * y_spacing, 0])
                layer_neurons.add(neuron)
            
            label = Text(name, font_size=24, font="Consolas", color=color)
            label.next_to(layer_neurons, DOWN, buff=0.5)
            all_labels.append(label)
            all_neurons.append(layer_neurons)
        
        for i, layer in enumerate(all_neurons):
            self.play(Create(layer), Write(all_labels[i]), run_time=1)
            self.wait(0.3)
        
        self.wait(0.5)

        # === CREATE CONNECTIONS ===
        connections = VGroup()
        for layer_idx in range(len(all_neurons) - 1):
            current_layer = all_neurons[layer_idx]
            next_layer = all_neurons[layer_idx + 1]
            
            for neuron1 in current_layer:
                for neuron2 in next_layer:
                    line = Line(
                        neuron1.get_center(),
                        neuron2.get_center(),
                        color=WHITE,
                        width=1,
                        stroke_opacity=0.5
                    )
                    connections.add(line)
        
        self.play(Create(connections), run_time=2)
        self.wait(0.5)

        # === TRAINING METRICS DISPLAY ===
        metrics_box = Rectangle(width=5, height=3, color=WHITE, fill_opacity=0.1)
        metrics_box.to_edge(RIGHT).shift(UP * 0.5)
        
        metrics_title = Text("Training Metrics", font_size=28, color=YELLOW)
        metrics_title.move_to(metrics_box.get_center()).shift(UP * 1)
        
        epoch_text = Text("Epoch: 0", font_size=24, font="Consolas", color=WHITE)
        epoch_text.next_to(metrics_title, DOWN, buff=0.3)
        
        loss_text = Text("Loss: 1.000", font_size=24, font="Consolas", color=RED)
        loss_text.next_to(epoch_text, DOWN, buff=0.2)
        
        accuracy_text = Text("Accuracy: 0%", font_size=24, font="Consolas", color=GREEN)
        accuracy_text.next_to(loss_text, DOWN, buff=0.2)
        
        self.play(
            Create(metrics_box), Write(metrics_title),
            Write(epoch_text), Write(loss_text), Write(accuracy_text)
        )
        self.wait(0.5)

        # === LOSS GRAPH ===
        graph_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1, 0.2],
            x_length=4,
            y_length=2,
            axis_config={"color": GRAY}
        )
        graph_axes.scale(0.5)
        graph_axes.to_edge(RIGHT).shift(DOWN * 1.5)
        
        graph_label = Text("Loss Over Time", font_size=16, color=WHITE)
        graph_label.next_to(graph_axes, UP, buff=0.1)
        
        self.play(Create(graph_axes), Write(graph_label))
        
        loss_curve = graph_axes.plot(lambda x: 1 / (1 + x), color=RED, x_range=[0, 10])
        self.play(Create(loss_curve))
        self.wait(0.5)

        # === SIMULATE TRAINING ===
        training_title = Text("Training in Progress...", font_size=36, color=YELLOW)
        training_title.to_edge(LEFT).shift(UP * 2)
        self.play(Write(training_title))
        
        total_epochs = 10
        for epoch in range(1, total_epochs + 1):
            loss = 1 / (1 + epoch * 0.5)
            accuracy = min(95, epoch * 10)
            
            new_epoch_text = Text(f"Epoch: {epoch}", font_size=24, font="Consolas", color=WHITE)
            new_epoch_text.move_to(epoch_text)
            
            new_loss_text = Text(f"Loss: {loss:.3f}", font_size=24, font="Consolas", color=RED)
            new_loss_text.move_to(loss_text)
            
            new_accuracy_text = Text(f"Accuracy: {accuracy}%", font_size=24, font="Consolas", color=GREEN)
            new_accuracy_text.move_to(accuracy_text)
            
            self.play(
                Transform(epoch_text, new_epoch_text),
                Transform(loss_text, new_loss_text),
                Transform(accuracy_text, new_accuracy_text),
                run_time=0.5
            )
            
            # FIXED: Use 'width' and 'opacity' not 'stroke_width' and 'stroke_opacity'
            self.play(
                connections.animate.set_stroke(color=YELLOW, width=2, opacity=1),
                run_time=0.2
            )
            self.play(
                connections.animate.set_stroke(color=WHITE, width=1, opacity=0.5),
                run_time=0.2
            )
            
            self.wait(0.1)
        
        self.wait(0.5)
        self.play(FadeOut(training_title))

        # === TRAINING COMPLETE ===
        complete_text = Text("✓ Training Complete!", font_size=48, color=GREEN)
        complete_text.to_edge(LEFT).shift(UP * 2)
        self.play(Write(complete_text))
        self.wait(1)

        # === FINAL METRICS ===
        self.play(
            Transform(epoch_text, Text("Epoch: 10", font_size=24, font="Consolas", color=WHITE).move_to(epoch_text)),
            Transform(loss_text, Text("Loss: 0.125", font_size=24, font="Consolas", color=RED).move_to(loss_text)),
            Transform(accuracy_text, Text("Accuracy: 95%", font_size=24, font="Consolas", color=GREEN).move_to(accuracy_text))
        )
        self.wait(1)

        # === HOW TRAINING WORKS ===
        self.play(FadeOut(metrics_box), FadeOut(metrics_title), FadeOut(epoch_text), 
                  FadeOut(loss_text), FadeOut(accuracy_text), FadeOut(graph_axes), 
                  FadeOut(graph_label), FadeOut(loss_curve))
        
        how_title = Text("How Training Works", font_size=48, color=YELLOW)
        how_title.to_edge(UP)
        self.play(Write(how_title))
        
        training_steps = VGroup(
            Text("1. Forward Pass: Make prediction", font_size=28, font="Consolas", color=BLUE),
            Text("2. Calculate Loss: Compare to answer", font_size=28, font="Consolas", color=RED),
            Text("3. Backpropagation: Calculate gradients", font_size=28, font="Consolas", color=YELLOW),
            Text("4. Update Weights: Adjust connections", font_size=28, font="Consolas", color=GREEN),
            Text("5. Repeat: Until loss is minimized", font_size=28, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        training_steps.next_to(how_title, DOWN, buff=0.5)
        
        for step in training_steps:
            self.play(Write(step), run_time=0.7)
            self.wait(0.2)
        
        self.wait(1)
        self.play(FadeOut(how_title), FadeOut(training_steps), FadeOut(complete_text))

        # === REAL-WORLD APPLICATIONS ===
        apps_title = Text("What Can Trained Networks Do?", font_size=42, color=YELLOW)
        apps_title.to_edge(UP)
        self.play(Write(apps_title))
        
        applications = VGroup(
            Text("Image Recognition (Photos, Medical)", font_size=26, font="Consolas", color=WHITE),
            Text("Natural Language (Chatbots, Translation)", font_size=26, font="Consolas", color=WHITE),
            Text("Predictions (Stocks, Weather, Sales)", font_size=26, font="Consolas", color=WHITE),
            Text("Autonomous Vehicles (Self-Driving)", font_size=26, font="Consolas", color=WHITE),
            Text("Creative AI (Art, Music, Writing)", font_size=26, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        applications.next_to(apps_title, DOWN, buff=0.5)
        
        for app in applications:
            self.play(Write(app), run_time=0.5)
            self.wait(0.1)
        
        self.wait(1)
        self.play(FadeOut(apps_title), FadeOut(applications))

        # === FINAL MESSAGE ===
        final_text = Text("✨ AI Learns from Data! ✨", font_size=48, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)