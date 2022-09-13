from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question = Question()



question_bank = []
for i in question_data:
    q_1 = i["question"]
    q_2 = i["correct_answer"]
    new_question = Question(q_1, q_2)
    question_bank.append(new_question)
# print(question_bank)
# new_question.question_list
        
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("The quiz is over")
print(f"You scored: {quiz.score} out of a possible {len(question_bank)}")





