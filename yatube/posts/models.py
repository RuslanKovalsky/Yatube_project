from django.db import models

# Create your models here.
from django.db import models
# Из модуля auth импортируем функцию get_user_model
from django.contrib.auth import get_user_model
#Для работы с моделями импортируется модуль models,
# а для создания поля со ссылкой на модель User
# импортируется и эта модель: она встроена в
# Django и отвечает за управление пользователями.
#Официальная документация рекомендует
#обращаться к модели User через функцию g
#et_user_model. Следуем этой рекомендации:

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )