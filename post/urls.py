from django.urls import path
from .views import home, create_post,delete,update

urlpatterns = [
    path('home/', home, name="home"),
    path('delete/<int:post_id>', delete, name="delete"),
    path('update/<int:post_id>', update, name="update"),
    path('', create_post)
]
