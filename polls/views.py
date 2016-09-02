from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request: HttpRequest, question_id: str) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request: HttpRequest, question_id: str) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request: HttpRequest, question_id: str) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)