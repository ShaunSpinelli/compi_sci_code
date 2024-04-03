from manim import *


class ArraysExample(Scene):
    def construct(self):
        # Create matrices
        
        m1 = [0, 1, 1, 1, 2, 3, 4,4,5,6,6]
        # m1 = [1, 1, 1, 2]
        matrix1 = Matrix([m1])  # Adjust rows and columns as needed
        
        
        equation =  Text(f"Remove Duplicates From Ordered Array", font_size=40)
        equation.next_to(matrix1, UP*4)
        self.play(Write(equation))
        
  

        # Show elements and labels
        self.play(Create(matrix1))
        
        fast_rect = SurroundingRectangle(matrix1.get_columns()[1], color=RED)
        matrix1.add(fast_rect)
        
        text_f = Text("Fast", font_size=28).next_to(fast_rect, UP)
        self.play(Write(text_f))
        self.play(FadeOut(text_f),run_time=0.5)
        
        
        slow_rect = SurroundingRectangle(matrix1.get_columns()[0])
        matrix1.add(slow_rect)
        text_s = Text("Slow", font_size=28).next_to(slow_rect, UP)
        self.play(Write(text_s))
        self.play(FadeOut(text_s),run_time=0.5)
        
        
        # fast_rect.move_to(next_position)
        self.wait(0.5)
        
        slow = 0
        
           # # Iterate through the array
        for fast in range(1, len(m1)):
            # If the current element is not equal to the previous one
            # next_column = matrix1.get_columns()[fast]
            next_position_F = matrix1.get_columns()[fast].get_center()
            fast_rect.move_to(next_position_F)
          
            
            if m1[fast] != m1[slow]:
                t1 = Text(f"{m1[fast]} != {m1[slow]} so we step slow one and assign fast value", font_size=30).next_to(matrix1, DOWN)
                self.play(Write(t1))
                
                slow += 1
                next_position_S = matrix1.get_columns()[slow].get_center()
                slow_rect.move_to(next_position_S)
                # Replace the next element with the unique element
                m1[slow] = m1[fast]
                # switch
                num = Text(str(m1[fast]), font_size=30).shift(matrix1.get_columns()[fast].get_center())
                self.add(num)
                self.play(FadeOut(matrix1[0][slow]), run_time=0.5)
                self.play(Transform(num, Text(str(m1[fast]), font_size=30).shift(matrix1.get_columns()[slow].get_center())))
                self.play(FadeOut(t1),run_time=0.25)
                
                self.wait(0.25)
            else:
                t =  Text(f"{m1[fast]} == {m1[slow]} so we do nothing", font_size=30).next_to(matrix1, DOWN)
                self.play(Write(t))
                self.play(FadeOut(t),run_time=0.25)
                
                
                
            self.wait(0.25)
                