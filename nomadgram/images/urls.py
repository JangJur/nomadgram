from django.conf.urls import path
from . import views
app_name = "images"
urlpatterns = [
    path("", view=views.ListAllImages.as_View(), name='all_images'),
]
