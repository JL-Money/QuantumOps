from manim import *
from unit_circle_triangle import UnitCircleTriangle

class GroverEq5(Scene):
    def construct(self):
        # First equation
        eq1 = MathTex(r"t = \left\lfloor\frac{\pi}{4\theta}\right\rfloor")
        
        # Second equation
        eq2 = MathTex(r"=", r"\left\lfloor\frac{\pi}{4\sin^{-1}\sqrt{\frac{M}{N}}}\right\rfloor")
        
        # Third equation
        eq3 = MathTex(r"=", r"\left\lfloor\frac{\pi\sqrt{N}}{4\sqrt{M}}\right\rfloor")
        
        # Group equations and scale to fit
        eq_group = VGroup(eq1, eq2, eq3).arrange(RIGHT, buff=0.5)
        eq_group.scale(0.8)  # Scale down to fit screen
        eq_group.move_to(ORIGIN)  # Center on screen
        
        # Position equations after scaling
        eq2.next_to(eq1, RIGHT, buff=0.5)
        eq3.next_to(eq2, RIGHT, buff=0.5)

        # Create theta equation below
        theta_eq = MathTex(r"\theta = \sin^{-1}\left(\sqrt{\frac{M}{N}}\right)").scale(0.5)
        ineq = MathTex(r"\sin^{-1}\left(\sqrt{\frac{M}{N}}\right) \geq \sqrt{\frac{M}{N}}").scale(0.5)
        theta_eq.next_to(eq2[0], DOWN, buff=1) #.align_to(eq2[0], LEFT)
        ineq.next_to(eq3[0], DOWN, buff=1)
        
        # Create upward arrows from theta equation to equal signs
        up_arrow1 = Arrow(
            start=theta_eq.get_top(),
            end=eq2[0].get_bottom(),
            buff=0.2,
            stroke_width=2  # Add smaller stroke width
        )
        up_arrow2 = Arrow(
            start=ineq.get_top(),
            end=eq3[0].get_bottom(),
            buff=0.2,
            stroke_width=2  # Add smaller stroke width
        )
        
        # Animate everything
        self.play(Write(eq1))
        self.play(Write(theta_eq), Create(up_arrow1))
        self.play(Write(eq2))
        self.play(
            Write(ineq), Create(up_arrow2)
        )
        self.play(Write(eq3))
        self.wait()

        complexity = MathTex(r"O\left(\sqrt{\frac{N}{M}}\right)")

        complexity.next_to(eq2, UP, buff=1)

        self.play(Write(complexity))
        self.wait(2)