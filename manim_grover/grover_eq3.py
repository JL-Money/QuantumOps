from manim import *
from unit_circle_triangle import UnitCircleTriangle

class GroverEq3(Scene):
    def construct(self):
        M = MathTex("M")
        MMatrix = MathTex("\\begin{pmatrix} \\frac{|e| - |a|}{N} & -\\frac{2\\sqrt{|e| \\cdot |a|}}{N} \\\\ \\frac{2\\sqrt{|e| \\cdot |a|}}{N} & \\frac{|e| - |a|}{N} \\end{pmatrix}")
        MsqrtMatrix = MathTex("\\begin{pmatrix} \\sqrt{\\frac{|e|}{N}} & -\\sqrt{\\frac{|a|}{N}} \\\\ \\sqrt{\\frac{|a|}{N}} & \\sqrt{\\frac{|e|}{N}} \\end{pmatrix}")
        MsqrtMatrix2 = MathTex("\\begin{pmatrix} \\sqrt{\\frac{|e|}{N}} & -\\sqrt{\\frac{|a|}{N}} \\\\ \\sqrt{\\frac{|a|}{N}} & \\sqrt{\\frac{|e|}{N}} \\end{pmatrix}^2")
        eq1 = VGroup(M.copy(), MathTex("="), MMatrix.copy(), MathTex("="), MsqrtMatrix2.copy()).arrange(RIGHT)

        rotMatrix = MathTex("\\begin{pmatrix} cos(\\theta) & -sin(\\theta) \\\\ sin(\\theta) & cos(\\theta) \\end{pmatrix}")
        eq2 = VGroup(MsqrtMatrix.copy(), MathTex("="), rotMatrix.copy()).arrange(RIGHT).scale(0.6).to_edge(LEFT, buff=1)

        thetaEq = VGroup(
            MathTex("\\theta = sin^{-1} (\\sqrt{\\frac{|a|}{N}})"),
            MathTex("\\theta = cos^{-1} (\\sqrt{\\frac{|e|}{N}})")
        ).arrange(DOWN).scale(0.6).shift(DOWN * 2)

        rotMatrix2 = MathTex("\\begin{pmatrix} cos(2\\theta) & -sin(2\\theta) \\\\ sin(2\\theta) & cos(2\\theta) \\end{pmatrix}")

        eq3 = VGroup(M.copy(), MathTex("="), rotMatrix2.copy()).arrange(RIGHT).scale(0.7).shift(DOWN * 2 + 2 * RIGHT)

        angleConserve = MathTex("sin(\\theta)^2 + cos(\\theta)^2 = 1").scale(0.6)
        amplitudeConserve = MathTex("(\\sqrt{\\frac{|e|}{N}})^2 + (\\sqrt{\\frac{|a|}{N}})^2 = 1").scale(0.6)

        conserve_group = VGroup(amplitudeConserve, angleConserve).arrange(DOWN, aligned_edge=LEFT)
        conserve_group.next_to(eq2, RIGHT, buff=1)

        for part in eq1:
            self.play(Write(part))
        self.wait(2)
        self.play(eq1.animate.scale(0.6).to_edge(UP, buff=1).to_edge(LEFT, buff=1))

        self.play(Write(eq2[0]))  # Draw left-hand side of eq2
        self.wait(1)

        self.play(Write(amplitudeConserve))  # Draw amplitudeConserve
        self.wait(1)

        self.play(Write(eq2[1]), Write(eq2[2]))  # Draw right-hand side of eq2
        self.wait(1)

        self.play(Write(angleConserve))  # Draw angleConserve
        self.wait(2)


        triangle = UnitCircleTriangle(np.sqrt(3)/2, 1/2)
        # triangle.move_to(3 * DOWN + 8 * RIGHT)
        triangle.move(2 * UP + 3 * RIGHT)
        self.play(Create(triangle))
        self.wait(2)

        # self.play(triangle.animate.update_lengths(np.sqrt(2)/2, np.sqrt(2)/2))
        # self.wait(2)


        self.play(Write(thetaEq))
        self.wait(2)

        self.play(thetaEq.animate.to_edge(LEFT, buff=1))
        self.wait(1)

        self.play(Write(eq3))
        # self.play(Transform(eq3, VGroup(eq3[0], eq3[1], rotMatrix2.copy().move_to(eq3[2]).scale(0.6))))  # Transform eq3 to show the rotation matrix
        self.wait(2)