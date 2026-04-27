from manim import *

class Day26(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Day 26: RSA Encryption", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === SUBTITLE ===
        subtitle = Text("The Math Behind Secure Communication", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # === STEP 1: CHOOSE TWO PRIME NUMBERS ===
        step1_title = Text("Step 1: Choose Two Prime Numbers", font_size=36, color=BLUE)
        step1_title.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(step1_title))
        
        p_value = Text("p = 7", font_size=48, font="Consolas", color=GREEN)
        q_value = Text("q = 11", font_size=48, font="Consolas", color=GREEN)
        values = VGroup(p_value, q_value).arrange(RIGHT, buff=1)
        values.next_to(step1_title, DOWN, buff=0.5)
        
        self.play(Write(values))
        self.wait(1)

        # === STEP 2: CALCULATE N (PUBLIC MODULUS) ===
        step2_title = Text("Step 2: Calculate n = p × q", font_size=36, color=BLUE)
        step2_title.to_edge(UP).shift(DOWN * 0.5)
        
        n_calculation = Text("n = 7 × 11 = 77", font_size=48, font="Consolas", color=YELLOW)
        n_calculation.next_to(step2_title, DOWN, buff=0.5)
        
        self.play(
            Transform(step1_title, step2_title),
            FadeOut(values),
            Write(n_calculation)
        )
        self.wait(1)

        # === STEP 3: CALCULATE PHI (EULER'S TOTIENT) ===
        step3_title = Text("Step 3: Calculate φ(n) = (p-1)(q-1)", font_size=32, color=BLUE)
        step3_title.to_edge(UP).shift(DOWN * 0.5)
        
        phi_calculation = Text("φ(n) = 6 × 10 = 60", font_size=48, font="Consolas", color=PURPLE)
        phi_calculation.next_to(step3_title, DOWN, buff=0.5)
        
        self.play(
            Transform(step2_title, step3_title),
            Transform(n_calculation, phi_calculation)
        )
        self.wait(1)

        # === STEP 4: CHOOSE PUBLIC KEY (e) ===
        step4_title = Text("Step 4: Choose Public Key e", font_size=36, color=BLUE)
        step4_title.to_edge(UP).shift(DOWN * 0.5)
        
        e_info = VGroup(
            Text("e must be coprime to φ(n)", font_size=24, font="Consolas", color=WHITE),
            Text("e = 13 (chosen)", font_size=48, font="Consolas", color=GREEN)
        ).arrange(DOWN, buff=0.3)
        e_info.next_to(step4_title, DOWN, buff=0.5)
        
        self.play(
            Transform(step3_title, step4_title),
            FadeOut(phi_calculation),
            Write(e_info)
        )
        self.wait(1)

        # === STEP 5: CALCULATE PRIVATE KEY (d) ===
        step5_title = Text("Step 5: Calculate Private Key d", font_size=36, color=BLUE)
        step5_title.to_edge(UP).shift(DOWN * 0.5)
        
        d_info = VGroup(
            Text("d × e ≡ 1 (mod φ(n))", font_size=24, font="Consolas", color=WHITE),
            Text("d × 13 ≡ 1 (mod 60)", font_size=24, font="Consolas", color=WHITE),
            Text("d = 37", font_size=48, font="Consolas", color=RED)
        ).arrange(DOWN, buff=0.3)
        d_info.next_to(step5_title, DOWN, buff=0.5)
        
        self.play(
            Transform(step4_title, step5_title),
            FadeOut(e_info),
            Write(d_info)
        )
        self.wait(1)

        # === KEY SUMMARY ===
        self.play(FadeOut(step5_title), FadeOut(d_info))
        
        keys_title = Text("Key Summary", font_size=48, color=YELLOW)
        keys_title.to_edge(UP)
        
        public_key = VGroup(
            Text("🔓 PUBLIC KEY", font_size=32, color=GREEN, font="Consolas"),
            Text("(e, n) = (13, 77)", font_size=36, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3)
        public_key.next_to(keys_title, DOWN, buff=0.5).shift(LEFT * 3)
        
        private_key = VGroup(
            Text("🔒 PRIVATE KEY", font_size=32, color=RED, font="Consolas"),
            Text("(d, n) = (37, 77)", font_size=36, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3)
        private_key.next_to(keys_title, DOWN, buff=0.5).shift(RIGHT * 3)
        
        self.play(Write(keys_title), Write(public_key), Write(private_key))
        self.wait(1)
        self.play(FadeOut(keys_title), FadeOut(public_key), FadeOut(private_key))

        # === ENCRYPTION DEMO ===
        encrypt_title = Text("Encryption Demo", font_size=48, color=YELLOW)
        encrypt_title.to_edge(UP)
        self.play(Write(encrypt_title))
        
        # Message to encrypt
        message = Text("Message: M = 5", font_size=36, font="Consolas", color=WHITE)
        message.next_to(encrypt_title, DOWN, buff=0.5)
        
        # Encryption formula
        encrypt_formula = Text("C = M^e mod n", font_size=36, font="Consolas", color=GREEN)
        encrypt_formula.next_to(message, DOWN, buff=0.5)
        
        # Calculation
        encrypt_calc = Text("C = 5^13 mod 77 = 26", font_size=36, font="Consolas", color=YELLOW)
        encrypt_calc.next_to(encrypt_formula, DOWN, buff=0.5)
        
        self.play(Write(message), Write(encrypt_formula), Write(encrypt_calc))
        self.wait(1)
        self.play(FadeOut(message), FadeOut(encrypt_formula), FadeOut(encrypt_calc))

        # === DECRYPTION DEMO ===
        decrypt_title = Text("Decryption Demo", font_size=48, color=YELLOW)
        decrypt_title.to_edge(UP)
        self.play(Write(decrypt_title))
        
        # Ciphertext
        ciphertext = Text("Ciphertext: C = 26", font_size=36, font="Consolas", color=WHITE)
        ciphertext.next_to(decrypt_title, DOWN, buff=0.5)
        
        # Decryption formula
        decrypt_formula = Text("M = C^d mod n", font_size=36, font="Consolas", color=RED)
        decrypt_formula.next_to(ciphertext, DOWN, buff=0.5)
        
        # Calculation
        decrypt_calc = Text("M = 26^37 mod 77 = 5 ✓", font_size=36, font="Consolas", color=GREEN)
        decrypt_calc.next_to(decrypt_formula, DOWN, buff=0.5)
        
        self.play(Write(ciphertext), Write(decrypt_formula), Write(decrypt_calc))
        self.wait(1)
        self.play(FadeOut(decrypt_title), FadeOut(ciphertext), FadeOut(decrypt_formula), FadeOut(decrypt_calc))

        # === WHY RSA IS SECURE ===
        security_title = Text("Why is RSA Secure?", font_size=48, color=YELLOW)
        security_title.to_edge(UP)
        self.play(Write(security_title))
        
        security_reasons = VGroup(
            Text("🔐 Based on prime factorization", font_size=28, font="Consolas", color=WHITE),
            Text("🔐 Easy to multiply primes", font_size=28, font="Consolas", color=WHITE),
            Text("🔐 Hard to factor large numbers", font_size=28, font="Consolas", color=WHITE),
            Text("🔐 2048-bit keys = virtually unbreakable", font_size=28, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        security_reasons.next_to(security_title, DOWN, buff=0.5)
        
        for reason in security_reasons:
            self.play(Write(reason), run_time=0.7)
            self.wait(0.2)
        
        self.wait(1)
        self.play(FadeOut(security_title), FadeOut(security_reasons))

        # === REAL-WORLD APPLICATIONS ===
        apps_title = Text("Real-World Applications", font_size=48, color=YELLOW)
        apps_title.to_edge(UP)
        self.play(Write(apps_title))
        
        applications = VGroup(
            Text("🔒 HTTPS/SSL (Secure Websites)", font_size=28, font="Consolas", color=WHITE),
            Text("🔒 Digital Signatures", font_size=28, font="Consolas", color=WHITE),
            Text("🔒 Email Encryption (PGP)", font_size=28, font="Consolas", color=WHITE),
            Text("🔒 Secure Messaging (WhatsApp, Signal)", font_size=28, font="Consolas", color=WHITE),
            Text("🔒 Blockchain & Cryptocurrency", font_size=28, font="Consolas", color=WHITE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        applications.next_to(apps_title, DOWN, buff=0.5)
        
        for app in applications:
            self.play(Write(app), run_time=0.5)
            self.wait(0.1)
        
        self.wait(1)
        self.play(FadeOut(apps_title), FadeOut(applications))

        # === FINAL MESSAGE ===
        final_text = Text("✨ Math Secures the Internet! ✨", font_size=48, color=YELLOW)
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)