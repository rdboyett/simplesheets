import datetime

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeData, mark_for_escaping

register = template.Library()


@register.filter
def dayssince(value):
    #"Returns number of days between today and value."
    today = datetime.date.today()
    diff  = today - value
    if diff.days >= 30:
        if int(diff.days/30)>1:
            return '%s months ago' % int(diff.days/30)
        else:
            return '%s month ago' % int(diff.days/30)
    if diff.days >= 7 and diff.days < 30:
        if int(diff.days/7)>1:
            return '%s weeks ago' % int(diff.days/7)
        else:
            return '%s week ago' % int(diff.days/7)
    if diff.days > 1 and diff.days < 7:
        return '%s days ago' % diff.days
    elif diff.days == 1:
        return 'yesterday'
    elif diff.days == 0:
        return 'today'
    else:
        # Date is in the future; return formatted date.
        return value.strftime("%B %d, %Y")

