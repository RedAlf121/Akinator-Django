from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest

from AkinatorTree.models import Question
from AkinatorTree.services.arbol_preguntas import QuestionTree
from AkinatorTree.services.session_node import get_node_from_session_storage,save_node_to_session_storage
# Create your views here.

def game(request):
    current_node = get_node_from_session_storage(request)
    return render(request, 'game.html', {'question': current_node})



def yes_path(request):
   current_node = get_node_from_session_storage(request)
   current_node = current_node.yes_answer
   save_node_to_session_storage(request,current_node)
   return redirect('/game/')

def no_path(request):
   current_node = get_node_from_session_storage(request)
   current_node = current_node.no_answer
   save_node_to_session_storage(request,current_node)
   return redirect('/game/')

def main_menu(request:HttpRequest):
   save_node_to_session_storage(request,QuestionTree.get_root())
   print(Question.objects.filter(id=request.session['current_node_id']).first())
   return render(request, 'index.html')


