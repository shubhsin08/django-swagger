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
# class ListSongsFilter(filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')

#     class Meta:
#         model = Songs
#         fields = ['artist']

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer



# class ListSongsViewSet(viewsets.ModelViewSet):
#     """
#     Provides a get method handler.
#     """
#     queryset = Songs.objects.all()
#     serializer_class = SongsSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_fclass = ListSongsFilter

#     def get_songs(self):
#         try:
#             return Songs.objects.get(artist=self.kwargs['artist'])
#         except Songs.DoesNotExist:
#             return None

# #    def get_queryset(self):
# #            """
# #            Optionally restricts the returned purchases to a given user,
# ###            by filtering against a `username` query parameter in the URL.
# #            """
# #            queryset = Songs.objects.all()
# #            artist = self.request.query_params.get('artist', None)
# #            if artist is not None:
# #                queryset = queryset.filter(songs__artist=artist)
# #            return queryset
#     # def get_queryset(self):
#     #         song = self.get_songs()
#     #         if song is None:
#     #             return self.queryset.none()

#     #         return self.queryset.filter(song=song).filter(artist=self.request.artist)

#     @swagger_auto_schema(operation_description="partial_update description override", responses={404: 'slug not found'})
#     def partial_update(self, request, *args, **kwargs):
#         return None

#     artist_param = openapi.Parameter('artist', in_=openapi.IN_QUERY, description='Artist',
#                                     type=openapi.TYPE_STRING)
    # @swagger_auto_schema(operation_description="get description override", responses={404: 'slug not found'}, manual_parameters=[artist_param])
    # def list(self, request, *args, **kwargs):
    #     # return None
# class PageNumberPagination(pagination.PageNumberPagination):
#     page_size_query_param = "page_size"

#     ##
#     # Returns the paginated Response.
#     #
#     # @param data The data that is to be displayed
#     #
#     # @return The paginated Response.
#     #
#     def get_paginated_response(self, data):
#         return Response({
#             "links":  {
#                 "next":     self.get_next_link(),
#                 "previous": self.get_previous_link()
#             },
#             "count":      self.page.paginator.count,
#             "results":    data,
#             "pageCount":  self.page.paginator.num_pages,
#             "pageNumber": self.page.number,
#             "pageSize":   self.page.paginator.per_page
#         })





class getuserviewset(viewsets.ModelViewSet):

    limit = openapi.Parameter('limit', in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)

    # @swagger_auto_schema(operation_description="get description override", responses={404: 'slug not found'}, manual_parameters=[artist_param])
    # def get_queryset(self):
    #     search=self.request.GET.get('search', None)
    #     queryset= User.objects.filter(name__startswith=search)
    #     return queryset
    @swagger_auto_schema(manual_parameters=[limit])
    def list(self,request,*args,**kwargs):
        #search=self.request.GET.get('search','')
        limit=self.request.GET.get('limit','')
        #id=self.kwargs['id']
        queryset= User.objects.all().values_list('name','designation')
        queryset=[{'name':i[0],'designation':i[1]} for i in queryset]
        #serializer=getuserserializer(queryset,many=True)

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