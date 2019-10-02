from django.db import models

# Create your models here.


class Todo(models.Model):
    # 데이터를 저장할 colums을 만들어 준다.
    title = models.CharField(max_length=50)
    due_date = models.DateField()
    # 실제로 저장은 너가해
