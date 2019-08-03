from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from ping_pong.serializers import PingPongSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class PingPongView(APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('ping',
                          openapi.IN_QUERY,
                          description="please input ping",
                          type=openapi.TYPE_STRING)
    ])
    def get(self, request, format=None):
        serializer = PingPongSerializer(data=request.GET)
        if serializer.is_valid():
            if serializer.data['ping'] == 'ping':
                return Response({'result': 'pong'})
            else:
                return Response({'result': "What's in your head?"})
        else:
            return Response({'error': serializer.errors})
