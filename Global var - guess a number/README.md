#### Tricks explored in the blackjack project

- Global variable
  - There's no explicit way to define a global variable, use CAPITAL LETTER to represent global variables
  ```
  CHILL_MODE = 10
  INTENSE_MODE = 5
  .
  def set_attempt():
    level = input("'Chill' mode or 'intense' mode? ").lower()
    if level == "chill":
      return CHILL_MODE
    elif level == "intense":
      return INTENSE_MODE
  ```
