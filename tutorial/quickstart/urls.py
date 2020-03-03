from django.urls import include, path
from django.conf.urls import url
from tutorial.quickstart.views import *

urlpatterns=[

    path('<int:id>/details/',getuserviewset.as_view({'get': 'list'})),
]