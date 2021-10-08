import json
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core import serializers
from .models import Question,Choice,Category
from django.http.response import JsonResponse
import json

from django.contrib.auth.forms import  UserCreationForm


# Returns dictionary format of any passed question object
def question_to_dict(question):
    data = {}
    data['question_text']= question.question_text
    data['category']= question.category.name
    data['correct'] = question.choice_set.get(is_correct=True).data
    return data
def choice_to_dict(q_choice):
    
    choices = []
    for i in q_choice:
        x = {}
        x['data'] = i.data
        x['is_correct'] = i.is_correct
        choices.append(x)
    return choices

# Create your views here.
def home(request):
    categories = Category.objects.all()
    return render(request, 'quiz/quiz.html', context = {'categories':categories})

def questions_json(request,pk):
    category = Category.objects.get(pk=pk)
    questions = Question.objects.filter(category = category)
    
    return
# def ajax_detail(request, pk):
#     if request.method == 'POST' and request.is_ajax:
#         category = Category.objects.get(pk=pk)
#         questions = Question.objects.get(category = category)
#         data= []
#         for q in questions:
#             choices = Choice.objects.filter(choice = q)
#             print(f'choices in queryset : {choices}')
#             print(f'choices in dict : {choice_to_dict(choices)}')
#             data.append(question_to_dict(q))
#         for x in data:
#             x.update(answers = choice_to_dict(choices))
#             print(question_to_dict(q))
#             print(data)
#         return JsonResponse(data,safe=False)
#     else:
#         return HttpResponse(request, '<h1>Welcome to my quiz app')


def questions_detail(request,pk):
    category = Category.objects.get(pk=pk)
    answered_questions = []
    if request.method == 'POST':
        print(request.POST)
        questions = Question.objects.filter(category=category).order_by('?')
        score = 0
        wrong =0
        correct = 0
        total = 0
        for q in questions:
            total+=1
            print(request.POST.get(q.question_text))
            ans = q.choice_set.get(is_correct=True).data
            print(ans)
            print(type(ans))
            if ans == request.POST.get(q.question_text):
                correct += 1
                score += 10
            else:
                wrong += 1
        context = {
            'category':category,
            'questions':questions,
            'correct':correct,
            'wrong':wrong,
            'score':score
        }
        return render(request, 'quiz/result.html',context)
    else:
        questions = Question.objects.filter(category=category)
        context={
            'questions':questions
        }
        return render(request, 'quiz/questions.html',context)
