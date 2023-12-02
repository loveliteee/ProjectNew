from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class Product(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField("Наименование товара", max_length=255)

    price = models.FloatField("Стоимость")

    quantity = models.IntegerField("Количество")

    vendor_code = models.CharField("Артикул")

    description = models.TextField("Описание")

    image = models.ImageField("Изображение", upload_to='products')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



# models.py
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# models.py
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# models.py
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Добавьте свои пользовательские поля, если нужно

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin
