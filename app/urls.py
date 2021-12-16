from rest_framework.routers import DefaultRouter

from app.views import CustomUserViewSet, ProjectViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = router.urls
