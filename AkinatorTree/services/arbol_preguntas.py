from AkinatorTree.models import Question
from django.db import transaction

class QuestionTree:
    @staticmethod
    def get_root():
        return Question.objects.filter(parent=None).first()
    @staticmethod
    @transaction.atomic
    def create_new_question(selected_character, difference, current_question):
        previous_question = current_question.parent
        character_question = Question.objects.create(sentence=selected_character)
        new_question = Question.objects.create(
            sentence=difference,
            yes_answer=character_question,
            no_answer=current_question
        )
        character_question.parent = new_question
        current_question.parent = new_question
        character_question.save()
        current_question.save()
        if previous_question is not None:
            if previous_question.yes_answer == current_question:
                previous_question.yes_answer = new_question
            else:
                previous_question.no_answer = new_question
            new_question.parent = previous_question
            new_question.save()
            previous_question.save()
        else:
            print(current_question)
    @staticmethod
    def height(node:Question):
        if node.yes_answer is not None:
            yes_height = QuestionTree.height(node.yes_answer)
            no_height = QuestionTree.height(node.no_answer)
            return max(yes_height, no_height) + 1
        return -1


