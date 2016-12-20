from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from PIL import Image
import StringIO
from .models import FileUploads
from .serializers import FileUploadSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class FileUploadViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    queryset = FileUploads.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, )
    lookup_field = 'filename'
