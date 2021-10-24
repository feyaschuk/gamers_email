from django.db.models import Sum
from rest_framework import  viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Game
from .serializers import  GameSerializer
from esp.views import ESP


esp = ESP()

@api_view(['POST'])
def create_new_email(request):    
    
    serializer = GameSerializer(data=request.data)     
    if serializer.is_valid(raise_exception=True):
        email = serializer.validated_data.get('email') 
        email_in_ESP = esp.check_email(email=email)   
        email_in_game = Game.objects.filter(email=email).exists()
        if not email_in_ESP:
                esp.add_email(email=email)      
        if not email_in_game:    
            serializer.save(email=email)            
            games_number = 1                         
            
            return Response(
                {'email_in_ESP':email_in_ESP,
                 'email_in_game':email_in_game, 
                 'games_number': games_number, }, status=status.HTTP_200_OK)
        Game.objects.create(email=email)         
        games_number = Game.objects.filter(email=email).count()
        
        return Response({'email_in_ESP': email_in_ESP,
                     'email_in_game': email_in_game, 
                     'games_number': games_number, }, status=status.HTTP_200_OK)
    