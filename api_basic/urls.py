from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

appname = 'api_basic'

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', article_list., name='article_list'),
    path('article/', ArticleAPIView.as_view(), name='article_list'),
    # path('article_detail/<int:pk>', article_detail, name='article_detail'),
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('generic/article/<int:id>/', GenericAPIView.as_view(), name='generic_detail'),
    path('generic/article/', GenericAPIView.as_view(), name='generic_list'),

]