from operator import eq
from pdb import run
from runpy import run_path
from manim import *

class GroverTemp(Scene):
    def construct(self):
        # First set of equations
        eqE = MathTex(r"e = \{x \in \Sigma^n : f(x) = 0\}")
        eqA = MathTex(r"a = \{x \in \Sigma^n : f(x) = 1\}")

        def_group = VGroup(eqE, eqA).arrange(DOWN)

        self.play(*[Write(eq) for eq in [eqE, eqA]])
        self.wait()
        self.play(def_group.animate.scale(0.6).shift(UP * 2))
        self.wait()

        eq1 = MathTex(r"|e|", r"=", r"N-1")
        eq1[0].set_color(RED)
        eq2 = MathTex(r"|a|", r"=", r"1")
        eq2[0].set_color(BLUE)
        
        # Second set of equations
        eq3 = MathTex(r"|e\rangle = \frac{1}{\sqrt{", r"|e|", r"}} \sum_{x \in e} |x\rangle")
        eq3[1].set_color(RED)
        eq4 = MathTex(r"|a\rangle = \frac{1}{\sqrt{", r"|a|", r"}} \sum_{x \in a} |x\rangle")
        eq4[1].set_color(BLUE)

        # Uniform equation in terms of |e> and |a>
        eq5 = MathTex(r"|u\rangle = \sqrt{", r"\frac{|e|}{N}", r"|e\rangle + \sqrt{", r"\frac{|a|}{N}", r"}|a\rangle")
        eq5[1].set_color(RED)
        eq5[3].set_color(BLUE)
        
        # Group equations
        first_group = VGroup(eq1, eq2).arrange(DOWN, aligned_edge=LEFT)
        second_group = VGroup(eq3, eq4).arrange(DOWN, aligned_edge=LEFT)
        third_group = VGroup(eq5).arrange(DOWN, aligned_edge=LEFT)
        
        # Arrange all equations
        left_equations = VGroup(first_group, second_group, third_group).arrange(DOWN, buff=1, aligned_edge=LEFT)
        
        # Animate equations appearing simultaneously
        self.play(*[Write(eq) for eq in [eq1, eq2]])
        self.wait()
        
        self.play(*[Write(eq) for eq in [eq3, eq4]],)
        self.wait()

        self.play(*[Write(eq) for eq in [eq5]],)
        self.wait(2)

        # Shrink and move original equations to the left
        self.play(left_equations.animate.scale(0.6).shift(LEFT * 4))
        
        # Transform |e| to N-1
        eq3_sube = MathTex(r"|e\rangle =", r"\frac{1}{\sqrt{N-1}} \sum_{x \in e} |x\rangle").scale(0.6).move_to(eq3)
        eq5_sube = MathTex(r"|u\rangle = \sqrt{\frac{N-1}{N}}|e\rangle + \sqrt{", r"\frac{|a|}{N}}", r"|a\rangle").scale(0.6).move_to(eq5)
        eq5[1].set_color(BLUE)
        eq1_rhs1 = eq1[2].copy()
        eq1_rhs2 = eq2[2].copy()
        self.play(ReplacementTransform(eq1_rhs1, eq3[1]), ReplacementTransform(eq1_rhs2, eq5[1]), run_time=1.5)
        self.remove(eq1_rhs1, eq1_rhs2)
        self.play(Transform(eq3, eq3_sube), Transform(eq5, eq5_sube), run_time=1.5)
        self.wait()

        # Transform |a| to 1
        eq4_suba = MathTex(r"|a\rangle =", r"\frac{1}{\sqrt{1}} \sum_{x \in a} |x\rangle").scale(0.6).move_to(eq4)
        eq5_subea = MathTex(r"|u\rangle = \sqrt{\frac{N-1}{N}}", r"|e\rangle", r"+ \sqrt{\frac{1}{N}}|a\rangle").scale(0.6).move_to(eq5)
        eq2_rhs1 = eq2[2].copy()
        eq2_rhs2 = eq2[2].copy()
        self.play(ReplacementTransform(eq2_rhs1, eq4[1]), ReplacementTransform(eq2_rhs2, eq5_sube[1]), run_time=1.5)
        self.remove(eq2_rhs1, eq2_rhs2)
        self.play(Transform(eq4, eq4_suba), Transform(eq5, eq5_subea), run_time=1.5)
        self.wait()

        # Add a black square
        black_rectangle = Rectangle(color=BLACK, fill_opacity=1, width=6, height=2).move_to(eq5)
        self.add(black_rectangle)
        # Ensure eq5 is on top of the black square
        self.bring_to_front(eq5)
        self.wait()

        eq5_subEa = MathTex(r"|u\rangle = \sqrt{\frac{N-1}{N}}", r"\frac{1}{\sqrt{N-1}} \sum_{x \in e} |x\rangle", r"+ \sqrt{\frac{1}{N}}|a\rangle").scale(0.6).move_to(eq5)
        eq3_rhs = eq3_sube[1].copy()
        self.play(ReplacementTransform(eq3_rhs, eq5_subea[1]), run_time=1.5)
        self.remove(eq3_rhs)
        self.play(Transform(eq5, eq5_subEa), run_time=1.5)
        eq5_subENa = MathTex(r"|u\rangle = \frac{1}{\sqrt{N}} \sum_{x \in e} |x\rangle + \sqrt{\frac{1}{N}}", r"|a\rangle").scale(0.6).move_to(eq5)
        self.play(Transform(eq5, eq5_subENa), run_time=1.5)
        self.wait()

        # Add a black square
        black_rectangle = Rectangle(color=BLACK, fill_opacity=1, width=6, height=2).move_to(eq5)
        self.add(black_rectangle)
        # Ensure eq5 is on top of the black square
        self.bring_to_front(eq5)
        self.wait()

        eq5_final = MathTex(r"|u\rangle = \frac{1}{\sqrt{N}} \sum_{x \in e} |x\rangle + \sqrt{\frac{1}{N}} \sum_{x \in a} |x\rangle").scale(0.6).move_to(eq5)
        eq4_rhs = eq4_suba[1].copy()
        self.play(ReplacementTransform(eq4_rhs, eq5_subENa[1]), run_time=1.5)
        self.remove(eq4_rhs)
        self.play(Transform(eq5, eq5_final), run_time=1.5)
        self.wait()

        # Add a black square
        black_rectangle = Rectangle(color=BLACK, fill_opacity=1, width=6, height=2).move_to(eq5)
        self.add(black_rectangle)
        # Ensure eq5 is on top of the black square
        self.bring_to_front(eq5)
        self.wait()
        
        eq5_final = MathTex(r"|u\rangle = H^{\otimes n}|0\rangle^n").scale(0.6).move_to(eq5)
        self.play(Transform(eq5, eq5_final), run_time=1.5)
        self.wait()
        

        # Right side equations
        eq1_right = MathTex(r"|e| = N - M")
        eq2_right = MathTex(r"|a| = M")
        
        # Second set of right equations
        eq3_right = MathTex(r"|e\rangle = \frac{1}{\sqrt{|e|}} \sum_{x \in e} |x\rangle")
        eq4_right = MathTex(r"|a\rangle = \frac{1}{\sqrt{|a|}} \sum_{x \in a} |x\rangle")

        # Uniform equation in terms of |e> and |a>
        eq5_right = MathTex(r"|u\rangle = \sqrt{\frac{|e|}{N}}|e\rangle + \sqrt{\frac{|a|}{N}}|a\rangle")
        
        # Group right equations
        first_group_right = VGroup(eq1_right, eq2_right).arrange(DOWN, aligned_edge=RIGHT)
        second_group_right = VGroup(eq3_right, eq4_right).arrange(DOWN, aligned_edge=RIGHT)
        third_group_right = VGroup(eq5_right).arrange(DOWN, aligned_edge=RIGHT)
        
        # Arrange right equations
        right_equations = VGroup(first_group_right, second_group_right, third_group_right).arrange(DOWN, buff=1, aligned_edge=RIGHT)

        # Scale and shift right side equations
        right_equations.scale(0.6).shift(RIGHT * 4)

        # Animate right side equations
        self.play(*[Write(eq) for eq in [eq1_right, eq2_right]],)
        self.wait()
        
        self.play(*[Write(eq) for eq in [eq3_right, eq4_right]],)
        self.wait()

        self.play(*[Write(eq) for eq in [eq5_right]],)
        self.wait(2)

        eq3_right_1 = MathTex(r"|e\rangle = \frac{1}{\sqrt{N - M}} \sum_{x \in e} |x\rangle").scale(0.6).move_to(eq3_right)
        eq5_right_1 = MathTex(r"|u\rangle = \sqrt{\frac{N-M}{N}}|e\rangle + \sqrt{\frac{|a|}{N}}|a\rangle").scale(0.6).move_to(eq5_right)
        self.play(Transform(eq3_right, eq3_right_1), Transform(eq5_right, eq5_right_1), run_time=1.5)
        self.wait()

        eq4_right_1 = MathTex(r"|a\rangle = \frac{1}{\sqrt{M}} \sum_{x \in a} |x\rangle").scale(0.6).move_to(eq4_right)
        eq5_right_2 = MathTex(r"|u\rangle = \sqrt{\frac{N-M}{N}}|e\rangle + \sqrt{\frac{M}{N}}|a\rangle").scale(0.6).move_to(eq5_right)
        self.play(Transform(eq4_right, eq4_right_1), Transform(eq5_right, eq5_right_2), run_time=1.5)
        self.wait()

        eq5_right_3 = MathTex(r"|u\rangle = \sqrt{\frac{N-M}{N}} \frac{1}{\sqrt{N-M}} \sum_{x \in e} + \sqrt{\frac{M}{N}}|a\rangle").scale(0.6).move_to(eq5_right)
        self.play(Transform(eq5_right, eq5_right_3), run_time=1.5)
        self.wait(.5)

        eq5_right_4 = MathTex(r"|u\rangle = \frac{1}{\sqrt{N}} \sum_{x \in e} + \sqrt{\frac{M}{N}}|a\rangle").scale(0.6).move_to(eq5_right)
        self.play(Transform(eq5_right, eq5_right_4), run_time=1.5)
        self.wait()

        eq5_right_5 = MathTex(r"|u\rangle = \frac{1}{\sqrt{N}} \sum_{x \in e} + \sqrt{\frac{M}{N}} \frac{1}{\sqrt{M}} \sum_{x \in a} |x\rangle").scale(0.6).move_to(eq5_right)
        self.play(Transform(eq5_right, eq5_right_5), run_time=1.5)
        self.wait(.5)

        eq5_right_6 = MathTex(r"|u\rangle = \frac{1}{\sqrt{N}} \sum_{x \in e} + \frac{1}{\sqrt{N}} \sum_{x \in a} |x\rangle").scale(0.6).move_to(eq5_right)
        self.play(Transform(eq5_right, eq5_right_6), run_time=1.5)
        self.wait()

        eq5_right_final = MathTex(r"H^{\otimes n}|0\rangle^n").scale(0.6).move_to(eq5_right)
        self.play(Transform(eq5_right, eq5_right_final), run_time=1.5)
        self.wait()