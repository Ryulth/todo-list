from django.db import models

# Create your models here.
class TodoTb(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True ,default=0)
    author_id = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True, default=1) #0이 삭제된것
    success = models.IntegerField(blank=True, null=True, default=0) #0이 안한거
    class Meta:
        managed = False
        db_table = 'todo_tb'
