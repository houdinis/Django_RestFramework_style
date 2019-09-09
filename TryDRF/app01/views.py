from rest_framework import generics
from .models import Publisher, Books
from .serializers import PublisherSerializer, BooksSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

# view
# class Publisher_list(generics.ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class Publisher_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
#
#
# class Books_list(generics.ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# class Books_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# viewset
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
