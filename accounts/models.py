from email.headerregistry import Group
from django.contrib.auth.models import AbstractUser

from SPARTAMARKET_DRF.products import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="accounts_user_groups",  # 역참조 이름 추가
    )
