from manim import *
import numpy as np

class BlochSphere(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create sphere
        sphere = Surface(
            lambda u, v: np.array([
                np.cos(u) * np.sin(v),
                np.sin(u) * np.sin(v),
                np.cos(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, PI],
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        # Add axes
        axes = ThreeDAxes(x_range=[-1, 1], y_range=[-1, 1], z_range=[-1, 1])
        self.add(sphere, axes)

class GroverComparison(ThreeDScene):
    def construct(self):
        # Title
        title = Text("Grover's Algorithm: 1 vs. s Solutions")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP))

        # Equations
        single_solution = MathTex(r"\text{1 Solution: } \pi\sqrt{\frac{N}{4}}")
        multi_solution = MathTex(r"\text{s Solutions: } \pi\sqrt{\frac{N}{4s}}")
        
        equations = VGroup(single_solution, multi_solution).arrange(DOWN)
        self.play(Write(equations))
        self.wait()

        # 2D Grid for database representation
        grid = NumberPlane(
            x_range=[-4, 4],
            y_range=[-4, 4],
            background_line_style={
                "stroke_opacity": 0.6
            }
        )

        # Bloch sphere demonstration
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        bloch = BlochSphere()
        
        # State vector (can be animated)
        state_vector = Arrow3D(
            start=np.array([0., 0., 0.]),
            end=np.array([1., 0., 0.]),
            color=YELLOW
        )

        self.play(
            Create(bloch),
            Create(state_vector)
        )

        # Animation for single solution rotation
        self.play(
            Rotate(
                state_vector,
                angle=PI,
                axis=UP,
                about_point=ORIGIN
            ),
            run_time=2
        )

        # Add annotations and comparisons
        comparison_text = Text(
            "Single solution requires more iterations",
            font_size=24
        ).to_edge(DOWN)
        
        self.add_fixed_in_frame_mobjects(comparison_text)
        self.play(Write(comparison_text))
        self.wait(2)
