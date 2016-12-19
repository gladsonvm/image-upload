from .views import FileUploadViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'fileuploads', FileUploadViewSet, base_name='file-upload')

urlpatterns = []
urlpatterns += router.urls