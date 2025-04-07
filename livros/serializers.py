from rest_framework import serializers
from .models import Livros

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'