from AkinatorTree.models import Question
from django.db import transaction

class QuestionTree:
    @staticmethod
    def get_root():
        return Question.objects.filter(parent=None).first()
    @staticmethod
    @transaction.atomic
    def create_new_question(self, selected_character, difference, current_question, previous_question):
        character_question = Question.objects.create(sentence=selected_character)
        new_question = Question.objects.create(
            sentence=difference,
            yes_answer=character_question,
            no_answer=current_question
        )
        if previous_question:
            if previous_question.yes_answer == current_question:
                previous_question.yes_answer = new_question
            else:
                previous_question.no_answer = new_question
            previous_question.save()
        else:
            self.root = new_question
        return new_question
    @staticmethod
    def height(node:Question):
        if node.yes_answer is not None:
            yes_height = QuestionTree.height(node.yes_answer)
            no_height = QuestionTree.height(node.no_answer)
            return max(yes_height, no_height) + 1
        return -1


