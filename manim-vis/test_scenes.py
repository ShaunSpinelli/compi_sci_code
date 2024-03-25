from manim import *


STEP_SIZE = 1.3


def pointer_start(matrix):
    
        m1_len = len(matrix[0])
        
        current = m1_len // 2
        end = m1_len - m2_len
        
        steps = end - current
        
        # m is odd move whole step
        p1_offset = 0.68 if m1_len%2 == 0  else 0
        p1_start = matrix1.get_center() + UP*0.75 - [p1_offset,0,0] + [steps*STEP_SIZE, 0, 0 ]


class ArrayExample(Scene):
    def construct(self):
        # Create matrices
        
        m1 = [1, 3, 4, 5,0, 0, 0, 0]
        m2 = [2,4,5, 6]
        matrix1 = Matrix([m1])  # Adjust rows and columns as needed
        matrix2 = Matrix([m2])
        
        # 
        STEP_SIZE = 1.3
        
        m1_len = len(m1)
        m2_len = len(m2)
        
        current_m1 = m1_len // 2
        end = m1_len - m2_len
        
        steps_m1 = end - current_m1 - (m1_len)%2
        
        # m is odd move whole step
        p1_offset = 0.68 if m1_len%2 == 0  else 0
        p1_start = matrix1.get_center() + UP*0.75 - [p1_offset,0,0] + [steps_m1*STEP_SIZE, 0, 0 ]
                
        
        matrix2.next_to(matrix1, DOWN*4)

        current_m2 = m2_len // 2

        steps_m2 = m2_len - current_m2 - (m2_len)%2
        
        p2_offset = 0.68 if m2_len%2 == 0  else 0

        p2_start = matrix2.get_center() + UP*0.75 -  [p2_offset,0,0] + [steps_m2*STEP_SIZE, 0, 0 ]
        
        
        
        p_dot_start = matrix1.get_center() + UP*0.75 - [p1_offset,0,0] + [(steps_m1+m2_len)*STEP_SIZE, 0, 0 ]
        
        # m is even move whole step plus offset

        # Place matrices on screen
        # matrix1.to_edge(DOWN)

        # Highlight elements (optional)
        p1_dot = Dot(point=p1_start)  # Point above "3"
        
        p2_dot = Dot(point=p2_start)  # Point above last element in arr2
        p_dot = Dot(point=p_dot_start)    # Point above last element in arr1
        
        print(UP)
        
        rect2 = Rectangle(width=0.5, height=0.75, color=RED)
        rect2.next_to(p1_dot, DOWN)
        
        p1G = VGroup(p1_dot, rect2)
        
        # p1G.shift(LEFT*0.68)
        
        # Create labels
        label_p1 = MathTex("p_1", font_size=24).next_to(p1_dot, UP)
        label_p2 = MathTex("p_2", font_size=24).next_to(p2_dot, UP)
        label_p = MathTex("p", font_size=24).next_to(p_dot, UP)

        # Show elements and labels
        self.play(Create(matrix1), Create(matrix2))
        self.play(Create(p1_dot), Create(p2_dot), Create(p_dot))
        self.play(Write(label_p1), Write(label_p2), Write(label_p))
        self.play(Create(rect2))

        # Wait for a bit

        # while True:
        #     if p1 < 0:
        #         break
        #     if p2 < 0:
        #         break
        #     if m1[p1] > m1[p2]:
        #         arr1[p] = arr1[p1]
        #         p1 = p1 - 1
        #     else:
        #         arr1[p] = arr2[p2]
        #         p2 = p2 - 1
        #     p = p - 1
        
        equation =  MathTex("5_p1 < 6_p2", font_size=44)
        equation.next_to(matrix1, UP*4)
        self.play(Write(equation))