from django.urls import path
from api.views import SignUp, GetToken

urlpatterns = [
    path('token/', GetToken.as_view()),
    path('signup/', SignUp.as_view()),

]
