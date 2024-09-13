from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.
class ToDoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = ToDo.objects.filter(user = request.user.id)
        serializer = ToDoSerializer(todos, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'user': request.user.id
        }


        serializer = ToDoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)