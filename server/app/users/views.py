from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from utils.view import OK_RESPONSE, BAD_RESPONSE
from users.forms import LoginForm, RegistrationForm


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    """ Allow an active user to retrieve an access-token """
    form = LoginForm(request.DATA)
    if form.is_valid():
        key = form.get_token()
        data = {
            'token': key
        }
        return OK_RESPONSE(data)
    else:
        return BAD_RESPONSE(form.errors)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    """ Allows creation of a new user.
    """
    form = RegistrationForm(request.DATA)
    if form.is_valid():
        key = form.save()
        data = {
            'token': key
        }
        return OK_RESPONSE(data)
    else:
        return BAD_RESPONSE(form.errors)
