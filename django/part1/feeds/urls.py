from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),  # 'hello/' URL에 대한 패턴
    path('<int:feed_id>/<str:feed_content>', views.all_feed),  # 동적 변수를 포함하는 패턴
]