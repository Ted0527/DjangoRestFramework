from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as lazy


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(lazy('이메일을 입력해 주세요'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(lazy('관리자는 is_staff=True 여야 합니다'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(lazy('관리자는 is_superuser=True 여야 합니다'))
        return self.create_user(email, password, **extra_fields)