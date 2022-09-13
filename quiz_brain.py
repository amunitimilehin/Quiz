


class QuizBrain():
    def __init__(self, q_list) -> None:
        self.question_index = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_index < len(self.question_list)


    def next_question(self):
        this_question = self.question_list[self.question_index]
        self.question_index += 1
        answer = input(f"Q.{self.question_index}: {this_question.text} (True or False): ")
        self.check_answer(answer, this_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
            
        else:
            print("you got it wrong")
            print(f"The correct answer is {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_index}")
        print("\n")
