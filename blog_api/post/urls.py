from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet
# from .views import PostDetail, PostList, UserDetail, UserList

router = SimpleRouter()
router.register('', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls

# urlpatterns = [
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('user/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail.as_view()),
# ]
