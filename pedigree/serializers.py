from rest_framework import serializers
from .models import Person, Speciality, Family, FamilyMember, User


class SpecialitySerializer:
    pass


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ('name','id')


class PersonSerializer(serializers.ModelSerializer):
    speciality = serializers.CharField(source='speciality.name')
    speciality = SpecialitySerializer()

    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'speciality',
            'gender',
            'photo'
        )


class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'birth_date',
            'speciality',
            'gender',
            'photo'
        )


class FamilyMemberSerializer(serializers.ModelSerializer):
    family = serializers.CharField(source='family.name')
    member = serializers.CharField(source='member.first_name')

    class Meta:
        model = FamilyMember
        fields = '__all__'


class FamilyMemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'


class FamilySerializer(serializers.ModelSerializer):
    members = FamilyMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Family
        fields = (
            'name',
            'country',
            'members',
            'city'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        print(user)
        user.set_password(password)
        user.save()

        return user
