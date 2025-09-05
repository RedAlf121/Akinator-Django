from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest

from AkinatorTree.forms.learn_form import LearnForm
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
   if current_node is not None:
      save_node_to_session_storage(request,current_node)
      return redirect('/game/')
   return render(request,'win.html')

def no_path(request):
   current_node = get_node_from_session_storage(request)
   current_node = current_node.no_answer
   if current_node is not None:
      save_node_to_session_storage(request,current_node)
      return redirect('/game/')
   return render(request,'lost.html',context={'form':LearnForm})

def learn(request:HttpRequest):
   current_node = get_node_from_session_storage(request)
   learn_form = LearnForm(request.POST)
   body = learn_form.data
   QuestionTree.create_new_question(current_question=current_node,selected_character=body['character'],difference=body['difference'])
   return redirect('/')

def main_menu(request:HttpRequest):
   save_node_to_session_storage(request,QuestionTree.get_root())
   return render(request, 'index.html')


