from django.urls import path
from newsapp.PasswordView.pasword_reset_view import PasswordResetAPI

from .views import *
 

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    #auth
    path('api/v1/register/', RegistrationAPIView.as_view()),
    path('api/v1/login/', AuthorizateView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/logout/', LogoutViewV1.as_view(), name='auth_logout'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/password/reset/',PasswordResetAPI.as_view()),




    #get
    path('', News_Views.as_view()),
    path('api/v1/news/get/main_news',MainNews.as_view()),
    path('api/v1/news/get/last_news',Last_News_Views.as_view()),
    path('api/v1/news/get/content/<int:pk>',GetPost.as_view()),
    path('api/v1/news/get/search',SearchPostAPI.as_view()),
    #profile get
    path('api/v1/user/info',ProfileView.as_view()),
    path('api/v1/news/get/profile',ProfileDetailView.as_view()),
    path('api/v1/news/get/user_post',UserPostView.as_view()),

    


    #post
    path('api/v1/news/post/new_post',Post_News.as_view()),
    path('api/v1/news/post/like',AddLike.as_view()),
    path('api/v1/news/post/identificated',PostApiIdentificated.as_view()),
    path('api/v1/news/post/order',OrderedViewAPI.as_view()),
    


    #delete
    path('api/v1/news/post/delete/<int:pk>',DeletePostApi.as_view()),
    path('api/v1/news/post/order',DeletePostApi.as_view()),
    path('api/v1/category/get/all',CategoryView.as_view()),
    path('api/v1/product/filter/',ProductList.as_view()),
   

  

]
