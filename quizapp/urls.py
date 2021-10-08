from django.conf.urls import url
from django.urls import path
from django.urls import path

from .views import (
    home,
    # ajax_detail,
    questions_detail,
)

urlpatterns =[
    path('', home, name='quizhome'),
    # path('detail/<int:pk>/',ajax_detail, name='ajax-detail'),
    path('questions-detail/<int:pk>/', questions_detail, name='questions_detail' ),
    

]