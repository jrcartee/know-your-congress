from rest_framework.response import Response
from rest_framework import status


OK_RESPONSE = lambda data: Response(
    status=status.HTTP_200_OK, data=data
)

BAD_RESPONSE = lambda data: Response(
    status=status.HTTP_400_BAD_REQUEST, data=data
)

UNAUTHORIZED = lambda data: Response(
    status=status.HTTP_401_UNAUTHROIZED, data=data
)
