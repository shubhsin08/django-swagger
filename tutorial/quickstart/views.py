from django.contrib.auth.models import *
from rest_framework import viewsets
from tutorial.quickstart.serializers import *
from tutorial.quickstart.models import *

from django_filters import rest_framework as filters
import django_filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.pagination import PageNumberPagination 
from rest_framework.response import Response
from rest_framework import pagination


#     @swagger_auto_schema(operation_description="partial_update description override", responses={404: 'slug not found'})
#     def partial_update(self, request, *args, **kwargs):
#         return None

#     artist_param = openapi.Parameter('artist', in_=openapi.IN_QUERY, description='Artist',
#                                     type=openapi.TYPE_STRING)
    # @swagger_auto_schema(operation_description="get description override", responses={404: 'slug not found'}, manual_parameters=[artist_param])
    # def list(self, request, *args, **kwargs):
    #     # return None






class getuserviewset(viewsets.ModelViewSet):

    limit = openapi.Parameter('limit', in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[limit])
    def list(self,request,*args,**kwargs):
        #search=self.request.GET.get('search','')
        limit=self.request.GET.get('limit','')
        #id=self.kwargs['id']
        queryset= User.objects.all().values_list('name','designation')
        queryset=[{'name':i[0],'designation':i[1]} for i in queryset]
        serializer=getuserserializer(queryset,many=True)

        if limit:
            pagination.PageNumberPagination.page_size=limit

        page = self.paginate_queryset(queryset)
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )
        return self.get_paginated_response(serializer.data)
    
        
        
       
        
    
    serializer_class=getuserserializer   

class testviewset(viewsets.ModelViewSet):
    def get_queryset(self):
        limit=self.request.query_params.get('limit')
        if limit:
                pagination.PageNumberPagination.page_size=limit
        queryset=User.objects.all().values_list('name','designation')
        queryset=[{'name':i[0],'designation':i[1]} for i in queryset]

        return queryset

    serializer_class=getuserserializer