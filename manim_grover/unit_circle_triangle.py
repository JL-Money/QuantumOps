from manim import *

class UnitCircleTriangle(VGroup):
    def __init__(self, adjacent_side_length, opposite_side_length, **kwargs):
        super().__init__(**kwargs)

        self.adjacent_side_length = adjacent_side_length
        self.opposite_side_length = opposite_side_length

        # Ensure the lengths satisfy the Pythagorean theorem for a unit circle
        assert abs(adjacent_side_length**2 + opposite_side_length**2 - 1) < 1e-6, "The lengths do not satisfy the Pythagorean theorem for a unit circle."

        # Create the vertices of the triangle
        self.origin = ORIGIN
        self.adjacent_point = [2 * adjacent_side_length, 0, 0] # Scale factor of 2
        self.opposite_point = [2 * adjacent_side_length, 2 * opposite_side_length, 0] # Scale factor of 2

        # Create the sides of the triangle
        self.hypotenuse = Line(self.origin, self.opposite_point)
        self.adjacent_side = Line(self.origin, self.adjacent_point)
        self.opposite_side = Line(self.adjacent_point, self.opposite_point)

        # Create the labels for the sides
        self.hypotenuse_label = MathTex("1").scale(0.5).move_to(self.hypotenuse.get_center() + 0.2 * UP) # Scale factor of 0.5
        self.adjacent_side_label = MathTex(r"\sqrt{\frac{|e|}{N}}").scale(0.5).next_to(self.adjacent_side, DOWN) # Scale factor of 0.5
        self.opposite_side_label = MathTex(r"\sqrt{\frac{|a|}{N}}").scale(0.5).next_to(self.opposite_side, RIGHT) # Scale factor of 0.5

        # Create the angle theta
        self.theta = Angle(self.adjacent_side, self.hypotenuse, radius=0.5)
        self.theta_label = MathTex(r"\theta").move_to(self.theta.get_center() + 0.1 * UP + 0.3 * RIGHT)

        # Add the elements to the VGroup
        self.add(self.hypotenuse, self.adjacent_side, self.opposite_side,
                 self.hypotenuse_label, self.adjacent_side_label, self.opposite_side_label,
                 self.theta, self.theta_label)
    
    def update_lengths(self, new_adjacent_side_length, new_opposite_side_length):
        self.adjacent_side_length = new_adjacent_side_length
        self.opposite_side_length = new_opposite_side_length

        # Ensure the lengths satisfy the Pythagorean theorem for a unit circle
        assert abs(self.adjacent_side_length**2 + self.opposite_side_length**2 - 1) < 1e-6, "The lengths do not satisfy the Pythagorean theorem for a unit circle."

        # Create the vertices of the triangle
        self.adjacent_point = [2 * self.adjacent_side_length, 0, 0] # Scale factor of 2
        self.opposite_point = [2 * self.adjacent_side_length, 2 * self.opposite_side_length, 0] # Scale factor of 2

        # Update the sides of the triangle
        self.hypotenuse.become(Line(self.origin, self.opposite_point))
        self.adjacent_side.become(Line(self.origin, self.adjacent_point))
        self.opposite_side.become(Line(self.adjacent_point, self.opposite_point))

        # Update the labels for the sides
        self.hypotenuse_label.move_to(self.hypotenuse.get_center() + 0.2 * UP)
        self.adjacent_side_label.next_to(self.adjacent_side, DOWN)
        self.opposite_side_label.next_to(self.opposite_side, RIGHT)

        # Update the angle theta
        self.theta.become(Angle(self.adjacent_side, self.hypotenuse, radius=0.5))
        self.theta_label.move_to(self.theta.get_center() + 0.1 * UP + 0.3 * RIGHT)  # Adjust label position

    def move(self, direction):
        # Update vertex positions
        self.origin = np.array(self.origin) + np.array(direction)
        self.adjacent_point = np.array(self.adjacent_point) + np.array(direction)
        self.opposite_point = np.array(self.opposite_point) + np.array(direction)

        # Update the sides of the triangle
        self.hypotenuse.become(Line(self.origin, self.opposite_point))
        self.adjacent_side.become(Line(self.origin, self.adjacent_point))
        self.opposite_side.become(Line(self.adjacent_point, self.opposite_point))

        # Update the labels for the sides
        self.hypotenuse_label.move_to(self.hypotenuse.get_center() + 0.2 * UP)
        self.adjacent_side_label.next_to(self.adjacent_side, DOWN)
        self.opposite_side_label.next_to(self.opposite_side, RIGHT)

        # Update the angle theta
        self.theta.become(Angle(self.adjacent_side, self.hypotenuse, radius=0.5))
        self.theta_label.move_to(self.theta.get_center() + 0.1 * UP + 0.3 * RIGHT)
        
        return self
