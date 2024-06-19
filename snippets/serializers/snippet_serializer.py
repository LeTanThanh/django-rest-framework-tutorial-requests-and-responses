from rest_framework.serializers import ModelSerializer

from ..models.snippet import Snippet
from ..models.snippet import LANGUAGE_CHOICES
from ..models.snippet import STYLE_CHOICES

class SnippetSerializer(ModelSerializer):
    model = Snippet
    fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
