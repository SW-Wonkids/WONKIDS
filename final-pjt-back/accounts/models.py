from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    school = models.CharField(max_length=10, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    classnum = models.IntegerField(blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        category = data.get("category")
        age = data.get("age")
        school = data.get("school")
        grade = data.get("grade")
        classnum = data.get("classnum")

        user_email(user, email)
        user_username(user, username)

        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)

        if category:
            user.category = category
        if age:
            user.age = age
        if school:
            user.school = school
        if grade:
            user.grade = grade
        if classnum:
            user.classnum = classnum

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()  # user.save() 호출 후에 추가 작업 수행
        return user