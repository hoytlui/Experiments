#### Notes:


- Tkinter
  - Set variable outside function
  ```
  card_background = canvas.create_image(400, 263, image=card_front_img)
  ```
  - Change variable inside function
  ```
  def next_card():
    .
    canvas.itemconfig(card_background, image=card_front_img)
  
  def flip_card():
    .
    canvas.itemconfig(card_background, image=card_back_img)
  ```

- Global variable
  - call and change global variable inside function
  ```
  flip_timer = window.after(3000, func=flip_card)
  
  def next_card():
      global flip_timer
      # start flip timer
      window.after_cancel(flip_timer)
      .
      # reset flip timer and call flip_card function
      flip_timer = window.after(3000, func=flip_card)
  ```
