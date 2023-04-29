from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from rest_framework.viewsets import GenericViewSet

from .models import Person, Family, FamilyMember, Speciality, User
from .serializers import PersonSerializer, FamilySerializer, FamilyMemberSerializer, PersonCreateSerializer, \
    FamilyMemberCreateSerializer, SpecialitySerializer, UserSerializer

from rest_framework.permissions import AllowAny, IsAdminUser


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes_by_action = {'list': [permissions.AllowAny],
                                    'retrieve': [permissions.AllowAny]}

    def get_serializer_class(self):
        if self.action == 'list':
            return PersonSerializer
        elif self.action == 'create':
            return PersonCreateSerializer
        else:
            return PersonSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]


class FamilyMemberViewSet(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.RetrieveModelMixin,
                          GenericViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return FamilyMemberSerializer
        elif self.action == 'create':
            return FamilyMemberCreateSerializer
        else:
            return FamilyMemberSerializer


class SpecialityViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
