<img src="https://github.com/hoytlui/Experiments/blob/main/Tkinter%20-%20Pomodoro%20timer/image.png" width=400>

#### Notes:

- Iterate own function
  ```
  def countdown(count):
    .
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
  ```

- String formatting
  - Display 2 digits
  - `canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")`
