import pdb

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view

from .models.snippet import Snippet
from .serializers.snippet_serializer import SnippetSerializer


@csrf_exempt
@api_view(http_method_names=['GET', 'POST'])
def snippets(request):
    request_method = request.method

    match request_method:
        case 'GET':
            return list_snippets(request=request)
        case 'POST':
            return create_snippets(request=request)
        case _:
            # Alreay handle by api_view
            pass


def list_snippets(request):
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(instance=snippets, many=True)
    data = serializer.data

    return JsonResponse(data=data, safe=False, status=status.HTTP_200_OK)


def create_snippets(request):
    serializer = SnippetSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
