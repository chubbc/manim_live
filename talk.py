from manim_slide import *
import math

config.background_color = "#161c20"

temp = TexTemplate()
temp.add_to_preamble(r"\usepackage{stmaryrd,mathtools}")
temp.add_to_preamble(r"\newcommand{\comm}[2]{\left\llbracket#1,#2\right\rrbracket}")
temp.add_to_document(r"\fontfamily{lmss}\selectfont")
# temp.add_to_document(r"\fontfamily{phv}\selectfont")
# temp = MyTexTemplate()
temp.add_to_preamble(r"\usepackage{marvosym} \usepackage{fontawesome}")

def MyTex(*x,tex_environment="center",tex_template="",color=WHITE,scale=1.0):
    return Tex(*x,
        tex_template=temp,
        tex_environment=tex_environment,
        color=color
    ).scale(scale)

toc=VGroup(
    # MyTex(r"\bfseries Lecture 1").scale(1.2),
    MyTex(r"1.~Slide 1"),
    MyTex(r"2.~Slide 2"),
    MyTex(r"3.~Slide 3"),
    MyTex(r"4.~Conclusion"),
).arrange(DOWN,buff=0.5,aligned_edge=LEFT).move_to(ORIGIN)

footer=VGroup(
    MyTex(r"\faGithubSquare~$\texttt{chubbc/manim\_slides}$"),
    MyTex(r"\faExternalLinkSquare~$\texttt{christopherchubb.com/manim\_slides}$"),
    MyTex(r"\faTwitterSquare~\faYoutubePlay~$\texttt{@QuantumChubb}$"),
).arrange(RIGHT,buff=3).to_corner(DOWN).shift(0.5*DOWN).scale(1/2).set_opacity(.5)



# footer=MathTex("\\texttt{christopherchubb.com/manim\_slides}").scale(1/2).to_corner(DOWN).set_opacity(.5)

# 0 Done
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
           self.play(toc[i].animate.scale(1.2).set_color(YELLOW),toc[i-1].animate.scale(1/1.2).set_color(WHITE))
           self.slide_break()

        self.play(toc[-1].animate.scale(1/1.2).set_color(WHITE))

class Slide1(SlideScene):
    def construct(self):
        tocindex=0
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
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

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))


class Slide2(SlideScene):
    def construct(self):
        tocindex=1
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
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

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))


class Slide3(SlideScene):
    def construct(self):
        tocindex=2
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
        self.slide_break()

        text=MathTex(
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

        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))


class Conclusion(SlideScene):
    def construct(self):
        tocindex=3
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
        self.slide_break()

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{marvosym} \usepackage{fontawesome}")

        summary=Tex("Summary of ","what ","is ","going on").scale(.75).move_to([0,1,0])
        summary[1].set_color(YELLOW)
        summary[3].set_color(RED)

        arxiv=Tex(r"\texttt{\bfseries arXiv:~????.?????}").next_to(summary,DOWN,buff=1).scale(.8)
        package=Tex(r"\texttt{\bfseries github:~chubbc/manim\_slides}").next_to(arxiv,DOWN,buff=.5).scale(.8)

        self.play(Write(summary))
        self.slide_break()
        self.play(Write(arxiv),Write(package))
        self.slide_break()
        
        self.remove(footer)
        concfooter=footer.copy()
        self.add(concfooter)
        footer_big=concfooter.copy().arrange(RIGHT,buff=.375).to_corner(DOWN).shift(0.25*UP).scale(1.25).set_opacity(1)
        self.play(Transform(concfooter,footer_big))
