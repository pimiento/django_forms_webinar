"""forms_webinar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path


urlpatterns = [
    path('', views.NamesListView.as_view(), name='list_names'),
    path('name/', views.NameCreateView.as_view(), name='create_name'),
    path('name/<int:pk>/view/', views.name_detail, name='name'),
    path('name/<int:pk>/update/', views.NameUpdateView.as_view(), name='update_name'),
    path('name/<int:pk>/delete/', views.NameDeleteView.as_view(), name='delete_name'),
]
