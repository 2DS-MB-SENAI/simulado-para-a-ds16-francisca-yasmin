from django.shortcuts import render
from .serializers import LivroSerializer #mudar pra JSON
from .models import Livro
from rest_framework.decorators import api_view #importando o decorador
from rest_framework.response import Response
from rest_framework import status

# listar os livros
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

# task 2 - listar os livros e adicionar os livros
#listar meus livros cadastrados
@api_view(['GET', 'POST'])
def read_livros(request):
    if request.method == 'GET':
        try:
            livro = Livro.objects.all()
        except Livro.DoesNotExist:
            return Response({'erro': 'livro não existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LivroSerializer(livro, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


    
