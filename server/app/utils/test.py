# REST-Framework
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
# Internal Imports


def get_credentials(user):
    auth_field = 'Token %s' % Token.objects.get(user=user).key
    return auth_field


def check_response(response, expected):
    assert response.status_code == expected, \
        ("%d - %s" % (response.status_code, response.content))


def base_view_test(url, user, response, data=None):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=get_credentials(user))
    if data is None:
        resp = client.get(url)
    else:
        resp = client.post(url, data)
    check_response(resp, response)
