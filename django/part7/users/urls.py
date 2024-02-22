from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

urlpatterns =[
    path("",views.Users.as_view()),
    path("myinfo",views.MyInfo.as_view()),

    # Authentication
    path("getToken",obtain_auth_token), #DRF token
    path("login",views.Login.as_view()), #django session login
    path("logout",views.Logout.as_view()), #django session logout

    # JWT Authentication
    path("login/jwt",views.JWTLogin.as_view()),
    path("login/jwt/info",views.UserDetailView.as_view()),

    # 프론트엔드에게 설명을 잘 해야함/장고 jwt2/2 영상참고
    # Simple JWT Authentication
    # 사용자가 처음으로 로그인할 때 사용
    path("login/simpleJWT",TokenObtainPairView.as_view()),
    # 엑세스 토큰이 만료되었을 때 사용
    path("login/simpleJWT/refresh",TokenRefreshView.as_view()),
    # 토큰의 유효성을 검증할 필요가 있을 때 사용
    path("login/simpleJWT/verify",TokenVerifyView.as_view()),
]
