#### Tricks explored in the blackjack project

- Global variable
  - Add global inside a function
  ```
  profit = 0
  .
  .
  def print_report():
    global profit
    .
    .
  def process_payment(choice):
    global profit
  ```
