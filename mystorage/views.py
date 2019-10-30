from rest_framework import viewsets, serializers
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer) :
        serializer.save(author = self.request.user)

    # 현재 request를 보낸 유저 == self.request.user
    # 이것을 뭉텅이로 생각하기
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated :
            qs = qs.filter(author = self.request.user)
        else :
            qs = qs.none()
        return qs

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    # file 오류 해결
    # 1. parser_class 지정 
    # 2. create() 함수 overriding

    # 1. 다양한 media 타입으로 request를 수락하는 방법
    parser_classes = (MultiPartParser, FormParser)
    # 2. API HTTP -> get 오버라이딩 한 것처럼 create() _ POST 요청
    def post(self, request, *args, **kwargs) :
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else :
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
    


