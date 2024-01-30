from django import template
from django.contrib.auth.models import User

register = template.Library()


# @register.inclusion_tag('tags/profile_avatar.html')
# def profile_avatar():
#
#     # We added first/last name of the superuser mike in our DB folder 'auth_user'
#     user = User.objects.all().first()  # We take the user
#
#     initials = user.first_name[0] + user.last_name[0]
#
#     # return 'context', much like in view's
#     return {
#         "user_fullname": f"{user.first_name} {user.last_name} - {initials}"  # We use 'user' to takes its names
#     }


# We can use 'takes-context' it is the same logic:
@register.inclusion_tag('tags/profile_avatar.html', takes_context=True)
def profile_avatar(context):
    print(context)
    user = context.request.user

    initials = user.first_name + user.last_name + ' - ' + user.first_name[0] + user.last_name[0] \
        if user.is_authenticated \
        else 'Anonymous'

    return {
        "user_fullname": initials,
    }
