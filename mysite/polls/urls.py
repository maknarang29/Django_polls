from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index',path('<int:pk>/')),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.result,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote')
]