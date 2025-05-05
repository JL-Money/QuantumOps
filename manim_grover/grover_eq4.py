from manim import *
from unit_circle_triangle import UnitCircleTriangle

class GroverEq4(Scene):
    def construct(self):
        # First equation
        eq1 = MathTex(r"G^t(\cos \theta |e\rangle + \sin \theta |a\rangle)")
        
        # Second equation - split into parts
        eq2_parts = MathTex(
            r"\cos((2t+1)\theta)|e\rangle",
            r"+",
            r"\sin((2t+1)\theta)|a\rangle"
        )
        
        # Third equation
        eq3 = MathTex(r"P_a = \sin^2((2t+1)\theta) \approx 1")
        
        # Fourth equation
        eq4 = MathTex(r"(2t+1)\theta \approx \frac{\pi}{2} \Rightarrow t \approx \frac{\pi}{4\theta} - \frac{1}{2}")
        
        # Group equations with eq2_parts instead of original eq2
        equations = VGroup(eq1, eq2_parts, eq3, eq4).arrange(DOWN, buff=1)
        
        # Create rectangle around sin|a> term
        rect = SurroundingRectangle(eq2_parts[2], color=GREEN)
        
        # Create arrows
        arrows = VGroup(*[
            Arrow(
                start=equations[i].get_bottom(),
                end=equations[i+1].get_top(),
                color=BLUE
            )
            for i in range(3)
        ])
        
        # Display everything
        self.play(Write(eq1))
        for i in range(3):
            self.play(
                Create(arrows[i]),
                Write(equations[i+1])
            )
            if i == 0:  # After eq2 is written
                self.play(Create(rect))
        
        self.wait(2)
