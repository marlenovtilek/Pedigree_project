from django.urls import re_path, include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework.permissions import AllowAny

import pedigree
from pedigree import views, admin
from pedigree.models import Person, Family, FamilyMember, User
from pedigree.views import FamilyMemberViewSet, SpecialityViewSet

pedigree_router = routers.DefaultRouter()
pedigree_router.register(r'person', views.PersonViewSet, basename=Person.__name__)
pedigree_router.register(r'family', views.FamilyViewSet, basename=Family.__name__)
pedigree_router.register(r'familyMember', views.FamilyMemberViewSet, basename=FamilyMemberViewSet.__name__)
pedigree_router.register(r'speciality', views.SpecialityViewSet, basename=SpecialityViewSet.__name__)
pedigree_router.register(r'user', views.UserViewSet, basename=User.__name__)
router = routers.DefaultRouter()

