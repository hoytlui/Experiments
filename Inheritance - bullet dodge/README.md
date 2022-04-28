<img src="https://github.com/hoytlui/Experiments/blob/main/Inheritance%20-%20bullet%20dodge/image.png">

#### Notes:

- Create and move lots of elements
  - Define list
    ```
    def __init__(self):
      self.bullet_list = []
    ```
  - Position starting point and add new elements to list
    ```
    def create_bullet(self):
      .
      .
      new_bullet.goto(random.randint(-260, 260), 200)
      self.bullet_list.append(new_bullet)
    ```
  - Iterate and move every element in the list
    ```
    def move_bullet(self):
        for bullet in self.bullet_list:
            bullet.forward(self.bullet_speed)
    ```

- Math tricks
  - Apply probability to reduce occurrence of event
  ```
  random_num = random.randint(2, 4)
  if random_num % 2 == 0:
      new_bullet = Turtle('circle')
  ```
