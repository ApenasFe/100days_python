from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q_dict in question_data:
    question = q_dict['text']
    answer = q_dict['answer']
    new_q = Question(question, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

quiz.still_has_questions()
print('Parabéns por concluir o Quiz!')
print(f'Você acertou {quiz.score} de {quiz.question_number} perguntas.')