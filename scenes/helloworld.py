from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, world!", font_size=72)
        self.play(Write(text))
        self.wait(2)
