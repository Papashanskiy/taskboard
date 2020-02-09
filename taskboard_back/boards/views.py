from rest_framework import generics

from .serializers import BoardSerializer, BoardDetailSerializer
from .models import Board


class BoardListView(generics.ListAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardDetailSerializer
    queryset = Board.objects.all()


class BoardCreateView(generics.CreateAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
