<img src="https://github.com/hoytlui/Experiments/blob/main/Inheritance%20-%20pong/image.png" width="400" height="300">

#### Notes:

- Arguments referred from outside the class do not need `self`
  ```
  class Paddle(Turtle):
      def __init__(self, position):
          .
          .
          self.goto(position)
  ```

- Methods vs attributes inside class
  ```
  class Scoreboard(Turtle):
      def __init__(self):
          .
          .
          self.penup()
          self.hideturtle()
          self.l_score = 0
          self.r_score = 0
  ```
