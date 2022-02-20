from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import StreamPlatformAV, StreamPlatformDetailAV, WatchListAV, WatchDetailAV, ReviewList, ReviewDetail, StreamPlatformViewSet,\
    UserViewSet, PointViewSet, PointInfoViewSet


# from watchlist_app.api.views import MovieListAV, MovieDetailAV
# from watchlist_app.api.views import movie_list, movie_details


router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='platform')
router.register('users', UserViewSet, basename='users')
router.register('points', PointViewSet, basename='points')
router.register('pointinfo', PointInfoViewSet, basename='pointinfo')

urlpatterns = [
    # path('', MovieListAV.as_view(), name='movie-list'),
    # path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
    path('', include(router.urls)),
    # path('', StreamPlatformAV.as_view(), name='stream'),
    # path('<int:pk>', StreamPlatformDetailAV.as_view(), name='detail'),
    
    path('list/', WatchListAV.as_view(), name='list'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name='detail'),
    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]