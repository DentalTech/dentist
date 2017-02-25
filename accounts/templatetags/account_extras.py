from django import template
from accounts.models import Family


register = template.Library()

@register.assignment_tag
def get_full_name(user):

    all_family = Family.objects.filter(account_name_id=user.id)

    full_name = all_family[0].full_name

    return full_name


