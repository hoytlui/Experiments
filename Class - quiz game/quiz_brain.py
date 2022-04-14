class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list

    
    def next_q(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        user_ans = input(f"Q.{self.q_number}: {current_q.text} (True/False): ").lower()
        self.check_ans(user_ans, current_q.answer)

    
    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong.")
        print(f"The correct answer is: {correct_ans}.")
        print(f"Your score: {self.score}/{self.q_number}\n")

    
    def still_has_qs(self):
        return self.q_number < len(self.q_list)
