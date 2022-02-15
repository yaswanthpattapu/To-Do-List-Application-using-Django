from django.urls import path
from .views import *
urlpatterns = [
    path("api/", List),
    path("api/<int:id>/", Post_Single_List),
    path("add/", Post_List),
    path("update/<int:id>/", Update_List),
    path("delete/<int:id>/", Delete_List),
]
