from django.shortcuts import render
from rest_framework import views, viewsets
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
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

    def perform_create(self, serializer):
        if serializer.validated_data.get('file').size < 250000000:
            print 'file size too large'
            return Response({'error', 'file size too large. Upload files below 25 Mb'}, status=413)
        else:

            super(viewsets.ModelViewSet, self).perform_create(serializer)


