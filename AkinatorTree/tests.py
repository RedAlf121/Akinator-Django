from django.test import TestCase

from services.arbol_preguntas import QuestionTree

# Create your tests here.
QuestionTree.height(QuestionTree.get_root())