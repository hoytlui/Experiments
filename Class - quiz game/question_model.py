class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

q_1 = Question("ask me anything", "ok")
print(q_1.text)
print(q_1.answer)