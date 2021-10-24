from django.urls import include, path


from .views import create_new_email


urlpatterns = [
    
    path('v1/email/', create_new_email),  
    
]
