from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    n_question = Question(text=q_text, answer=q_answer)
    question_bank.append(n_question)

# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")