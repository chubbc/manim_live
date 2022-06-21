from manim_slide import *

config.background_color = "#161c20"

toc=Group(
    Tex("1.~Slide 1"),
    Tex("2.~Slide 2"),
    Tex("3.~Slide 3"),
    Tex("4.~Conclusion"),
).arrange(DOWN,aligned_edge=LEFT,buff=0.5).move_to(ORIGIN)

footer=MathTex("\\texttt{christopherchubb.com/manim\_slides}").scale(1/2).to_corner(DOWN).set_opacity(.5)

# 0 Done
class Title(SlideScene):
    def construct(self):
        title = Tex(r"\bfseries\textsc{Title}").scale(1.25).shift(2.5*UP)
        arxiv = Tex(r"\bfseries\texttt{arXiv:????.?????}").scale(.75).shift(1.5*UP)
        name = Tex("Christopher T.\ Chubb")
        ethz=SVGMobject("ethz_logo_white.svg").scale(1/3).next_to(1.5*DOWN,LEFT,buff=2.5)
        udes=SVGMobject("Université_de_Sherbrooke_(logo).svg").scale(1/3).next_to(1.5*DOWN,RIGHT,buff=2.5)
        self.add(name,title,arxiv,ethz,udes,footer)
        
        self.play(Unwrite(title),Unwrite(arxiv),Unwrite(name),Unwrite(ethz),Unwrite(udes))
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
        tocindex=1-1
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
        tocindex=2-1
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
        tocindex=3-1
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
        tocindex=-1
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
        self.slide_break()

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{marvosym} \usepackage{fontawesome}")

        summary=Tex("Summary of ","what ","is ","going on").scale(.75).move_to([0,2,0])
        summary[1].set_color(YELLOW)
        summary[3].set_color(RED)
        
        arxiv=Tex(r"\texttt{\bfseries arXiv:~????.?????}").next_to(summary,DOWN,buff=1).scale(.8)
        package=Tex(r"\texttt{\bfseries github:~chubbc/manim\_slides}").next_to(arxiv,DOWN,buff=.25).scale(.8)

        email=Tex(r"\faEnvelope~~\texttt{me@christopherchubb.com}", tex_template=temp)
        website=Tex(r"\faLink~~\texttt{christopherchubb.com}", tex_template=temp)
        twitter=Tex(r"\faTwitter~~\texttt{@QuantumChubb}", tex_template=temp)
        github=Tex(r"\faGithub~~\texttt{chubbc}", tex_template=temp)
        socials=VGroup(github,twitter,website,email).arrange(DOWN).scale(0.75).shift(2*DOWN)

        self.play(Write(summary))
        self.slide_break()
        self.play(Write(arxiv),Write(package))
        self.slide_break()
        self.play(Write(socials))
        self.slide_break()
