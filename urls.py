from django.urls import path
from shop import views
urlpatterns=[
      path('index/',views.index,name="index"),
      path('register/',views.reg,name="reg"),
      path('',views.home,name="home"),
      path('login/',views.login,name="login"),
]