from django.urls import path, re_path
from . import views



app_name = 'apps.personal'


urlpatterns = [
      path('listarPersonal/', views.AddPersonal.as_view() ,name="listarPersonal"),
]
   