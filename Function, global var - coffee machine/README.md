#### Tricks explored in the coffee machine project

- Global variable
  - Call the variable with the key word `global` inside a function for adjustment
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
