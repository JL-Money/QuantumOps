from pdb import run
from re import L
from manim import *

class GroverEq2(Scene):
    def construct(self):
        Zf = MathTex(r"Z_f").set_color(GREEN)
        ZfEq = MathTex(r"Z_f", r": |x\rangle \mapsto (-1)^{f(x)} |x\rangle \quad \forall x \in \Sigma^n").set_color_by_tex("Z_f", GREEN)

        self.play(Write(ZfEq))
        self.wait(1.5)
        self.play(ZfEq.animate.to_edge(UP))
        self.wait(2)


        Zf1 = Zf.copy()
        EKet = MathTex(r"|e\rangle=")
        ERight = MathTex(r"\frac{1}{\sqrt{|e|}} \sum_{x \in e} |x\rangle")

        EGroup = VGroup(Zf1, EKet, ERight).arrange(RIGHT)

        # size_group = VGroup(ESize, ASize).arrange(DOWN)
        # left_group = VGroup(size_group).arrange(DOWN, buff=1)
        # left_group.scale(0.6).shift(LEFT * 4)

        # self.play(Write(size_group))
        # self.wait(1.5)

        self.play(Write(EKet), Write(ERight))
        self.wait(3)

        self.play(Write(Zf1))
        self.play(Transform(ERight, MathTex(r"\frac{1}{\sqrt{|e|}} \sum_{x \in e} Z_f |x\rangle").move_to(ERight).shift(RIGHT * 0.2)))
        self.wait(2)

        self.play(Transform(ERight, MathTex(r"\frac{1}{\sqrt{|e|}} \sum_{x \in e} (-1)^{f(x)} |x\rangle").move_to(ERight).shift(RIGHT * 0.6)))
        self.wait(2)

        self.play(Transform(ERight, MathTex(r"\frac{1}{\sqrt{|e|}} \sum_{x \in e} (-1)^{0} |x\rangle").move_to(ERight).shift(LEFT * 0.3)))
        self.wait(2)

        self.play(Transform(ERight, MathTex(r"\frac{1}{\sqrt{|e|}} \sum_{x \in e} |x\rangle").move_to(ERight).shift(LEFT * 0.4)))
        self.wait(2)

        self.play(EGroup.animate.shift(UP * 2).scale(0.6))


        Zf2 = Zf.copy()
        AKet = MathTex(r"|a\rangle=")
        ARight = MathTex(r"\frac{1}{\sqrt{|a|}} \sum_{x \in a} |x\rangle")

        AGroup = VGroup(Zf2, AKet, ARight).arrange(RIGHT)

        self.play(Write(AKet), Write(ARight))
        self.wait(3)

        self.play(Write(Zf2))
        self.play(Transform(ARight, MathTex(r"\frac{1}{\sqrt{|a|}} \sum_{x \in a} Z_f |x\rangle").move_to(ARight).shift(RIGHT * 0.2)))
        self.wait(2)

        self.play(Transform(ARight, MathTex(r"\frac{1}{\sqrt{|a|}} \sum_{x \in a} (-1)^{f(x)} |x\rangle").move_to(ARight).shift(RIGHT * 0.6)))
        self.wait(2)

        self.play(Transform(ARight, MathTex(r"\frac{1}{\sqrt{|a|}} \sum_{x \in a} (-1)^{1} |x\rangle").move_to(ARight).shift(LEFT * 0.3)))
        self.wait(2)

        self.play(Transform(ARight, MathTex(r"\frac{1}{\sqrt{|a|}} \sum_{x \in a} -|x\rangle").move_to(ARight).shift(LEFT * 0.4)))
        self.wait(2)

        self.play(Transform(ARight, MathTex(r"-\frac{1}{\sqrt{|a|}} \sum_{x \in a} |x\rangle").move_to(ARight)))
        self.wait(2)

        self.play(AGroup.animate.shift(UP * 1).scale(0.6))


        ESize = MathTex(r"|e|=N-1").to_edge(LEFT * .2 + UP * .5).scale(0.6)
        ASize = MathTex(r"|a|=1").to_edge(LEFT * .5 + UP * 1.5).scale(0.6)
        ESizeR = MathTex(r"|e|=N-M").to_edge(RIGHT * .2 + UP * .5).scale(0.6)
        ASizeR = MathTex(r"|a|=M").to_edge(RIGHT * .5 + UP * 1.5).scale(0.6)

        self.play(Write(ESize), Write(ASize), Write(ESizeR), Write(ASizeR))
        self.wait(2)

        EGroupR = EGroup.copy()
        AGroupR = AGroup.copy()

        self.play(
            ZfEq.animate.shift(UP * .3).scale(0.7),
            EGroup.animate.shift(LEFT * 5),
            AGroup.animate.shift(LEFT * 5),
            EGroupR.animate.shift(RIGHT * 5),
            AGroupR.animate.shift(RIGHT * 5)
        )
        self.wait(2)

        ESize1 = ESize.copy()
        ASize1 = ASize.copy()
        ESizeR1 = ESizeR.copy()
        ASizeR1 = ASizeR.copy()
        self.play(ESize1.animate.move_to(EGroup[2]), ASize1.animate.move_to(AGroup[2]),
                  ESizeR1.animate.move_to(EGroupR[2]), ASizeR1.animate.move_to(AGroupR[2]))
        self.play(FadeOut(ESize1), FadeOut(ASize1), FadeOut(ESizeR1), FadeOut(ASizeR1),
                  Transform(EGroup[2], MathTex(r"\frac{1}{\sqrt{N-1}} \sum_{x \in e} |x\rangle").move_to(EGroup[2]).scale(0.6)),
                  Transform(AGroup[2], MathTex(r"-\sum_{x \in a} |x\rangle").move_to(AGroup[2]).scale(0.6)),
                  Transform(EGroupR[2], MathTex(r"\frac{1}{\sqrt{N-M}} \sum_{x \in e} |x\rangle").move_to(EGroupR[2]).scale(0.6)),
                  Transform(AGroupR[2], MathTex(r"-\frac{1}{\sqrt{M}} \sum_{x \in a} |x\rangle").move_to(AGroupR[2]).scale(0.6))
        )
        self.remove(ESize1, ASize1, ESizeR1, ASizeR1)
        self.wait(2)


        D = MathTex(r"Diff").set_color(RED)
        Diff = VGroup(D.copy(), MathTex(r"=", r"H^{\otimes n}", r"\left( 2|0^n\rangle\langle 0^n| - I \right)", r"H^{\otimes n}")).arrange(RIGHT)

        self.play(Write(Diff))
        self.wait(1.5)
        self.play(
            Transform(Diff[1][1], MathTex("")),
            Transform(Diff[1][2], MathTex(r"2|u^n\rangle\langle u^n| - I")),
            Transform(Diff[1][3], MathTex("")),
            run_time=2
        )
        self.wait(1.5)
        self.play(Transform(Diff, VGroup(D, MathTex(r"=2|u^n\rangle\langle u^n| - I")).arrange(RIGHT)))
        self.wait(1.5)
        self.play(Diff.animate.to_edge(UP*2).scale(0.7))
        self.wait(2)

        G = MathTex(r"G").set_color(BLUE)
        GEq = VGroup(G.copy(), MathTex("="), D.copy(), MathTex(r"\cdot"), Zf).arrange(RIGHT)
        self.play(Write(GEq))
        self.wait(1)

        self.play(GEq.animate.to_edge(UP*3).scale(0.7))
        self.wait(1)


        # EGroup.add(G.copy().scale(0.6)).arrange(LEFT)
        self.play(Transform(EGroup, VGroup(G.copy().scale(0.6), EGroup[0], EGroup[1], EGroup[2]).arrange(RIGHT).move_to(EGroup)))

        # self.play(Write(EGroup)) # Write the G in the EGroup
        self.wait(1.5)