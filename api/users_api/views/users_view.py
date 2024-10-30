from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.users_api.serializers.users_serializer import UserSerializer
from custom_user.models.user import User


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def user_detail(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, pk):
    user = User.objects.all()
    user = User.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)