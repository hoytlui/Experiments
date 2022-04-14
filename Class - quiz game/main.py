from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for q_dict in question_data:
    new_q = Question(q_dict['text'], q_dict['answer'])
    question_bank.append(new_q)

# pass question_bank into QuizBrain class
quiz = QuizBrain(question_bank)

while quiz.still_has_qs():
    quiz.next_q()

print(f"You've completed the quiz. Your final score: {quiz.score}/{len(question_bank)}")