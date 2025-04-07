from django.shortcuts import render
from .serializers import BibliotecaSerializer #mudar pra JSON
from .models import Livros
from rest_framework.decorators import api_view #importando o decorador
from rest_framework.response import Response
from rest_framework import status

# listar os livros
def listar_livros(request):
    livros = Livros.objects.all()
    return render(request, 'livros.html', {'livros': livros})

# task 2 - listar os livros e adicionar os livros
#listar meus livros cadastrados
@api_view(['GET'])
def read_livros(request):
    livros = Livros.objects.all()
    serializer = BibliotecaSerializer(livros, many=True)
    return Response(serializer.data)

#criar um livro
@api_view(['POST'])
def create_livros(request):
    if request.method == 'POST':
        serializer = BibliotecaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
