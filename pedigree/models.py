from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager


# Create your models here.

class Speciality(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Пользователь", max_length=20, unique=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class Person(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'Муж'),
        ('FEMALE', 'Жен'),
    )

    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birth_date = models.DateField('Дата рождения')
    speciality = models.ForeignKey('Speciality', verbose_name="Специальность",
                                   on_delete=models.CASCADE, related_name="persons", null=True)
    gender = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES)
    photo = models.ImageField('Фото персоны', upload_to="person_photo", null=True, blank=True)

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Family(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Семья"
        verbose_name_plural = "Семьи"

    def __str__(self):
        return self.name


class FamilyMember(models.Model):
    member_name = models.CharField(max_length=10)
    member = models.ForeignKey(Person, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='members', null=True)

    class Meta:
        verbose_name = "Название части семейства"
        verbose_name_plural = "Названия части семейства"

    def __str__(self):
        return self.member_name
