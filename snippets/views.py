from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from http import HTTPStatus

from .models.snippet import Snippet
from .serializers.snippet_serializer import SnippetSerializer


@csrf_exempt
def snippets(request):
    request_method = request.method

    match request_method:
        case "GET":
            return list_snippets(request=request)
        case "POST":
            pass
        case _:
            return HttpResponseNotAllowed(permitted_methods=["GET", "POST"])


def list_snippets(request):
    return JsonResponse(data=[], safe=False, status=HTTPStatus.OK)
