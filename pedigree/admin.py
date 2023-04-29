from django.contrib import admin

from .models import Person, Speciality, Family, FamilyMember, User

admin.site.register(Person)
admin.site.register(Speciality)
admin.site.register(Family)
admin.site.register(FamilyMember)
admin.site.register(User)
