from manim_slide import *
import math

################################################################################

# BG = "#161c20"
BG = "#101518"
# BG = "#0b0e10"

config.background_color = BG

################################################################################

temp = TexTemplate()
temp.add_to_preamble(r"""
    \usepackage{stmaryrd,mathtools,marvosym,fontawesome}
    \newcommand{\comm}[2]     {\left\llbracket#1,#2\right\rrbracket}
    \newcommand{\bra}[1]      {\left\langle #1\right|}
    \newcommand{\ket}[1]      {\left|#1\right\rangle}
    \newcommand{\braket}[2]   {\left\langle #1\middle|#2\right\rangle}
    \newcommand{\ketbra}[2]   {\left|#1\middle\rangle\!\middle\langle#2\right|}
    \newcommand{\braopket}[3] {\left\langle #1\middle|#2\middle|#3\right\rangle}
    \newcommand{\proj}[1]     {\left| #1\middle\rangle\!\middle\langle#1\right|}
    \newcommand{\abs}[1]      {\left| #1 \right|}
    \newcommand{\norm}[1]     {\left\| #1 \right\|}
    \newcommand{\Tr}          {\mathrm{Tr}}
""")
temp.add_to_document(r"""
    \fontfamily{lmss}\selectfont
""")

def MyTex(*x,tex_environment="center",color=WHITE):
    return Tex(*x,
        tex_template=temp,
        tex_environment=tex_environment,
        color=color
    )

def MyMathTex(*x,tex_environment="align*",color=WHITE):
    return MyTex(*x,
        tex_environment=tex_environment,
        color=color
    )

def OffsetBezier(p1,o1,p2,o2,*x):
    return CubicBezier(
        p1,p1+o1,p2+o2,p2,*x)

# self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=toc and mob!=footer])

################################################################################

project_name = "manim\_slides"


toc=VGroup(
    MyTex(r"1.~Slide 1"),
    MyTex(r"2.~Slide 2"),
    MyTex(r"3.~Slide 3"),
    MyTex(r"4.~Conclusion"),
).arrange(DOWN,buff=0.5,aligned_edge=LEFT).move_to(ORIGIN)

footer=VGroup(
    MyTex(r"\faGithubSquare~$\texttt{chubbc/%s}$" % project_name),
    MyTex(r"\faExternalLinkSquare~$\texttt{christopherchubb.com/%s}$" % project_name),
    MyTex(r"\faTwitterSquare~\faYoutubePlay~$\texttt{@QuantumChubb}$"),
).arrange(RIGHT,buff=3).to_corner(DOWN).shift(0.5*DOWN).scale(1/2).set_opacity(.5)

################################################################################

class Title(SlideScene):
    def construct(self):
        title = MyTex(r"\bfseries\textsc{Title}").scale(1.25).shift(2.5*UP)
        arxiv = MyTex(r"\bfseries\texttt{arXiv:????.?????}").scale(.75).shift(1.5*UP)
        name = MyTex("Christopher T.\ Chubb")
        ethz=SVGMobject("ethz_logo_white.svg").scale(1/3).next_to(1.5*DOWN,LEFT,buff=1.5)
        udes=SVGMobject("Université_de_Sherbrooke_(logo).svg").scale(1/3).next_to(1.5*DOWN,RIGHT,buff=1.5)
        footer_big=footer.copy().arrange(RIGHT,buff=.375).to_corner(DOWN).shift(0.25*UP).scale(1.25).set_opacity(1)

        self.add(name,title,arxiv,ethz,udes,footer_big)
        
        self.play(Unwrite(title),Unwrite(arxiv),Unwrite(name),Unwrite(ethz),Unwrite(udes))
        self.play(ReplacementTransform(footer_big,footer))
        self.wait()
        self.play(FadeIn(toc))
        self.slide_break()

        self.play(toc[0].animate.scale(1.2).set_color(YELLOW))
        self.slide_break()

        for i in range(1,len(toc)):
            self.play(
                toc[i].animate.scale(1.2).set_color(YELLOW),
                toc[i-1].animate.scale(1/1.2).set_color(WHITE),
            )
            self.slide_break()

        self.play(toc[-1].animate.scale(1/1.2).set_color(WHITE))

################################################################################

class Slide1(SlideScene):
    def construct(self):
        tocindex=0
        heading = toc[tocindex]
        self.add(toc,footer)
        toc.save_state()
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)
        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)
        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.slide_break()

        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.slide_break()

        self.play(FadeOut(circle),FadeOut(line),FadeOut(dot))
        self.slide_break()

        self.play(Restore(toc))

################################################################################

class Slide2(SlideScene):
    def construct(self):
        tocindex=1
        heading = toc[tocindex]
        self.add(toc,footer)
        toc.save_state()
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        square = Square(color=BLUE, fill_opacity=1)
        self.play(FadeIn(square))
        self.play(square.animate.shift(LEFT))
        self.slide_break()

        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))
        self.slide_break()

        self.play(FadeOut(square))
        self.slide_break()

        self.play(Restore(toc))

################################################################################

class Slide3(SlideScene):
    def construct(self):
        tocindex=2
        heading = toc[tocindex]
        self.add(toc,footer)
        toc.save_state()
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        text=MyMathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        self.slide_break()

        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.slide_break()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.slide_break()

        self.play(FadeOut(text),FadeOut(framebox2))
        self.slide_break()

        self.play(Restore(toc))


class Conclusion(SlideScene):
    def construct(self):
        tocindex=3
        heading = toc[tocindex]
        self.add(toc,footer)
        toc.save_state()
        self.play(
            toc.animate.set_opacity(0),
            heading.animate.scale(2).to_corner(UP).set_x(0),
        )
        heading.set_opacity(1)
        self.slide_break()

        summary=MyTex("Summary of ","what ","is ","going on").scale(.75).move_to([0,1,0])
        summary[1].set_color(YELLOW)
        summary[3].set_color(RED)

        arxiv=MyTex(r"\texttt{\bfseries arXiv:~????.?????}").next_to(summary,DOWN,buff=1).scale(.8)
        package=MyTex(r"\texttt{\bfseries github:~chubbc/manim\_slides}").next_to(arxiv,DOWN,buff=.5).scale(.8)

        self.play(Write(summary))
        self.slide_break()
        self.play(Write(arxiv),Write(package))
        self.slide_break()
        
        self.remove(footer)
        concfooter=footer.copy()
        self.add(concfooter)
        footer_big=concfooter.copy().arrange(RIGHT,buff=.375).to_corner(DOWN).shift(0.25*UP).scale(1.25).set_opacity(1)
        self.play(Transform(concfooter,footer_big))
