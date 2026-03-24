from django.contrib import admin
from django.urls import include, path
from quickstart.views import student_list  # 👈 adiciona isso

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quickstart.urls")),  # 👈 corrigido
    path("students/", student_list, name="student"),
]
