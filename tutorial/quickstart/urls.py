from django.urls import include, path
from django.conf.urls import url
from tutorial.quickstart.views import *

urlpatterns=[

    path('details/',getuserviewset.as_view({'get': 'list'})),
    path('test/',testviewset.as_view({'get': 'list'})),
]