<img src="https://github.com/hoytlui/Experiments/blob/main/Inheritance%20-%20snake/image.png" width="300" height="300">

#### Notes:

- Initialize super class `Turtle`
  ```
  class Scoreboard(Turtle):
      def __init__(self):
          super().__init__()
          self.score = 0
  ```

- Create attribute from attribute
  ```
  class Snake():
      def __init__(self):
          self.block_list = []
          .
          .
          self.head = self.block_list[0]
  ```
