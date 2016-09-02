from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request: HttpRequest, question_id: str) -> HttpResponse:
    return HttpResponse("You're looking at question %s." % question_id)

def results(request: HttpRequest, question_id: str) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request: HttpRequest, question_id: str) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)