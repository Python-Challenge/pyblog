# https://qiita.com/okoppe8/items/86776b8df566a4513e96
import os
from django import template


register = template.Library()


@register.filter
def get_filename(value):
    return os.path.basename(value.file.name)
