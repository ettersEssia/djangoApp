# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# le point pour chercher les fichiers viexs ds tous les app(les dossier de mon projet)
from . import views
from django.urls import path
from django.contrib.auth.views import login, logout
urlpatterns = [
    path('', views.home),
    path('login/', login),
    path('logout/', logout),
    path('new_project/', views.new_project),
    path('list_project/', views.list_project),
    path('save_project/', views.save_project),
    path('delete_project/', views.delete_project),
    # path('list_projects/', views.list_projects),
]
