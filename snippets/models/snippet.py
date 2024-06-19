from django.db.models import Model
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import BooleanField

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(Model):
    created = DateTimeField(auto_now_add=True)
    title = CharField(max_length=100, blank=True, default='')
    code = TextField()
    linenos = BooleanField(default=False)
    language = CharField(choices=STYLE_CHOICES, default='python', max_length=100)
    styles = CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
