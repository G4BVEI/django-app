from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CursoViewSet, StudentViewSet, curso_list, student_list

router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"cursos", CursoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("student-list/", student_list),
    path("curso-list/", curso_list),
]
