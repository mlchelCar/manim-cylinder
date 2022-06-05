import manim
from manim import *


def cylinder(cilinder_height=2, cilinder_radius=2, stroke=4, color=GREEN, height=1.5):

    ellipse1 = Ellipse(
        width=cilinder_radius*2, height=height, fill_opacity=0.2, color=color, stroke_width=stroke
    )
    ellipse2 = ellipse1.copy().move_to([0, cilinder_height, 0])

    line1 = Line([-cilinder_radius, 0, 0], [-cilinder_radius,
                                            cilinder_height, 0], stroke_width=stroke).set_color(color)
    line2 = Line([cilinder_radius, 0, 0], [cilinder_radius,
                                           cilinder_height, 0], stroke_width=stroke).set_color(color)

    cilinder_group = VGroup(ellipse1, ellipse2, line1,
                            line2)
    return cilinder_group


class Animation(Scene):
    def construct(self):
        text1 = Text("Temos um cilindro de raio 'r' e altura 'h'")
        text2 = MarkupText(f'Nos podemos alterar a <span fgcolor="{GREEN}">altura</span> do cilindro',
                           font_size=30).move_to([2.5, 3.5, 0])
        h = Text("h = ", color=GREEN).move_to([-6.5, 3.5, 0])
        r = Text("r = ", color=GREEN).move_to([-6.5, 2.5, 0])

        hei = ValueTracker(2)
        rad = ValueTracker(2)
        hei_number = Text("2.0", color=GREEN).move_to([-5, 3.5, 0])
        rad_number = Text("2.0", color=GREEN).move_to([-5, 2.5, 0])

        cilinder1 = cylinder().move_to([0, -1, 0])

        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1, cilinder1))
        self.play(FadeIn(h, r, hei_number, rad_number))
        self.wait(0.5)
        self.play(
            Write(text2))
        self.wait(1)

        hei_number.add_updater(
            lambda num: num.become(Text(str(round(hei.get_value(), 3)), color=GREEN).move_to([-5, 3.5, 0])))
        rad_number.add_updater(
            lambda num: num.become(Text(str(round(rad.get_value(), 3)), color=GREEN).move_to([-5, 2.5, 0])))
        text1.add_updater(
            lambda cil: cil.become(cylinder(cilinder_height=hei.get_value(), cilinder_radius=rad.get_value()).move_to([0, -1+(hei.get_value()-2)/2, 0])))

        self.play(ApplyMethod(hei.set_value, 4, run_time=2))
        self.play(ApplyMethod(hei.set_value, 0.5, run_time=2))
        self.play(ApplyMethod(hei.set_value, 2, run_time=2))
        self.wait(0.5)
        self.play(Transform(text2, MarkupText(
            f'Tambem podemos alterar o <span fgcolor="{GREEN}">raio</span> do cilindro', font_size=30).move_to([2.5, 3.5, 0])))
        self.wait(0.5)
        self.play(ApplyMethod(rad.set_value, 4, run_time=2))
        self.play(ApplyMethod(rad.set_value, 0.5, run_time=2))
        self.play(ApplyMethod(rad.set_value, 2, run_time=2))
        self.wait(0.5)
        hei_number.clear_updaters()
        rad_number.clear_updaters()
        self.play(FadeOut(text2, h, r, hei_number, rad_number))


class AnimationEnglish(Scene):
    def construct(self):
        text1 = Text(
            "Here we have a cylinder of radius 'r' and height 'h'", font_size=35)
        text2 = MarkupText(f'We can change its <span fgcolor="{GREEN}">height</span>',
                           font_size=30).move_to([2.5, 3.5, 0])
        h = Text("h = ", color=GREEN).move_to([-6.5, 3.5, 0])
        r = Text("r = ", color=GREEN).move_to([-6.5, 2.5, 0])

        hei = ValueTracker(2)
        rad = ValueTracker(2)
        hei_number = Text("2.0", color=GREEN).move_to([-5, 3.5, 0])
        rad_number = Text("2.0", color=GREEN).move_to([-5, 2.5, 0])

        cilinder1 = cylinder().move_to([0, -1, 0])

        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1, cilinder1))
        self.play(FadeIn(h, r, hei_number, rad_number))
        self.wait(0.5)
        self.play(
            Write(text2))
        self.wait(1)
        hei_number.add_updater(
            lambda num: num.become(Text(str(round(hei.get_value(), 3)), color=GREEN).move_to([-5, 3.5, 0])))
        rad_number.add_updater(
            lambda num: num.become(Text(str(round(rad.get_value(), 3)), color=GREEN).move_to([-5, 2.5, 0])))
        text1.add_updater(
            lambda cil: cil.become(cylinder(cilinder_height=hei.get_value(), cilinder_radius=rad.get_value()).move_to([0, -1+(hei.get_value()-2)/2, 0])))

        self.play(ApplyMethod(hei.set_value, 4, run_time=2))
        self.play(ApplyMethod(hei.set_value, 0.5, run_time=2))
        self.play(ApplyMethod(hei.set_value, 2, run_time=2))
        self.wait(0.5)
        self.play(Transform(text2, MarkupText(
            f'We can also change its <span fgcolor="{GREEN}">radius</span>', font_size=30).move_to([2.5, 3.5, 0])))
        self.wait(0.5)
        self.play(ApplyMethod(rad.set_value, 4, run_time=2))
        self.play(ApplyMethod(rad.set_value, 0.5, run_time=2))
        self.play(ApplyMethod(rad.set_value, 2, run_time=2))
        self.wait(0.5)
        hei_number.clear_updaters()
        rad_number.clear_updaters()
        self.play(FadeOut(text2, h, r, hei_number, rad_number))
