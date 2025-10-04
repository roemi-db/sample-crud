#urls 

from django.urls import path
from . import views

urlpatterns = [
    path('individu/', views.IndividuListView.as_view(), name='individu_list'),
    path('individu/create/', views.IndividuCreateView.as_view(), name='individu_create'),
    path('individu/<int:pk>/', views.IndividuDetailView.as_view(), name='individu_detail'),
    path('individu/<int:pk>/update/', views.IndividuUpdateView.as_view(), name='individu_update'),
    path('individu/<int:pk>/delete/', views.IndividuDeleteView.as_view(), name='individu_delete'),
]

# menghubungkan di roemi/urls.py:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

