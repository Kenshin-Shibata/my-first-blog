from django.urls import path #djangoのpath関数をインポート
from . import views #blogアプリの全てのビューをインポート 

urlpatterns = [
    #最初のURLパターンを追加する
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]