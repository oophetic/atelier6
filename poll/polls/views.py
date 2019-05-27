from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Question

def index(request):
    questions = Question.objects.all()
    response = render_to_string("polls/list.html",
                                {'questions': questions})
    return HttpResponse(response)

def one(request, question_id):
    question = Question.objects.get(id=question_id)

    return render(request, "polls/one.html", locals())
