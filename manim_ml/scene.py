from manim import *


class ManimML3DScene(ThreeDScene):
    """
    This is a wrapper class for the Manim ThreeDScene.

    It stays thin on purpose: it carries only what every ManimML 3D scene
    needs, and animation logic belongs to the layers themselves.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def play(self):
        """ """
        pass
