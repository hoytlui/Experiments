![image](https://github.com/hoytlui/Experiments/blob/main/Instance%20-%20turtle%20racing/image.png)

`You win. Turtle 1 is the winner!`

#### Notes:

- Instance
  - Different instances have different states
  ```
  turtle_list = []
  for i in range(num_turtle):
      new_turtle = Turtle(shape='turtle')
      new_turtle.color(color_list[i])
      new_turtle.penup()
      new_turtle.goto(x=-230, y=y_pos[i])
      turtle_list.append(new_turtle)
    ```

- Screen
  - Set up screen and get prompt from user
  ```
  screen = Screen()
  screen.setup(width=500, height=400)
  bet = screen.numinput(title='Make Your Bet', prompt='Select your favourite turtle to win: (1-7)')
  ```

- xcor, ycor
  - Simple algebra to get index from constant numbers
  ```
  y_pos = [-90, -60, -30, 0, 30, 60, 90]
  .
  .
  game = True
  while game:
      for turtle in turtle_list:
          if turtle.xcor() > finish_line - 20:
              game = False
              winning_idx = (turtle.ycor() + 90) / 30
  ```
  
