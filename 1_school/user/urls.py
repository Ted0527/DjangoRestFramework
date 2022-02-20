from django.urls  import path
from user.views import StudentModelViewSet, TeacherModelViewSet, ScoreModelViewSet

teacher_list = TeacherModelViewSet.as_view({
    'get'  : 'list',
    'post' : 'create'
})

teacher_detail = TeacherModelViewSet.as_view({
    'get'    : 'retrieve',
    'put'    : 'update',
    'patch'  : 'partial_update',
    'delete' : 'destroy'
})

student_list = StudentModelViewSet.as_view({
    'get'  : 'list',
    'post' : 'create'
})

student_detail = StudentModelViewSet.as_view({
    'get'    : 'retrieve',
    'put'    : 'update',
    'patch'  : 'partial_update',
    'delete' : 'destroy'
})

score_list = ScoreModelViewSet.as_view({
    'get'  : 'list',
    'post' : 'create'
})

score_detail = ScoreModelViewSet.as_view({
    'get'    : 'retrieve',
    'put'    : 'update',
    'patch'  : 'partial_update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('teacher/', teacher_list),
    path('teacher/<int:pk>/', teacher_detail),
    path('students/', student_list),
    path('student/<int:pk>/', student_detail),
    path('score/', score_list),
    path('score/<int:pk>/', score_detail),
]