from django.urls import path, include

from pets import views

app_name = 'pets'

urlpatterns = [
    path('', views.pet_add_view, name='add'),
    path('<str:username>/pet/<str:pet_slug>/', include([
        path('', views.pet_details_view, name='details'),
        path('edit/', views.pet_edit_view, name='edit'),
        path('delete/', views.pet_delete_view, name='delete'),
    ])),
]