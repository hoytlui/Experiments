#### Tricks explored in the blackjack project

- Recursion
  ```
  while input("Type 'y' to start the game. ").lower() == 'y':
    .
    .
    play_game()
  ```

- Global variable
  - There's no explicit way to define a global variable, use CAPITAL LETTER to represent global variables
  ```
  CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  DECK_OF_CARDS = CARDS * 4
  .
  def deal_card():
    card_drawn = random.choice(DECK_OF_CARDS)
  ```
