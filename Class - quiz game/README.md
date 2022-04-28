#### Notes:

- Call the attributes outside the class
  ```
  class Question:

      def __init__(self, text, answer):
          self.text = text
          self.answer = answer

  q_1 = Question("some text", "some answer")
  print(q_1.text)
  print(q_1.answer)
  ```

- Use `self` when referring to the same attributes inside the same class
  ```
  def __init__(self, q_list):
    self.score = 0
    .
    .
  def check_ans(self, user_ans, correct_ans):
      if user_ans.lower() == correct_ans.lower():
          self.score += 1
  ```

- Don't use `self` if attributes are not created
  ```
  def check_ans(self, user_ans, correct_ans):
      if user_ans.lower() == correct_ans.lower():
          .
      else:
          .
      print(f"The correct answer is: {correct_ans}.")
  ```
