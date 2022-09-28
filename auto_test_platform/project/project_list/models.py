from django.db import models
from my_user.models import BaseModel
# Create your models here.


class ProjectList(BaseModel):
    project_id = models.AutoField(help_text="项目id", primary_key=True)
    project_name = models.CharField(max_length=128, help_text="项目名称")
    is_disable = models.BooleanField(default=False, help_text='是否禁用')
    is_delete = models.BooleanField(default=False, help_text='逻辑删除')

    # 指定数据库表信息
    class Meta:
        db_table = 'project_list'
        verbose_name = '项目基本信息'
        verbose_name_plural = verbose_name

    def delete(self, using=None, keep_parents=False):
        """重写数据库删除方法实现逻辑删除"""
        self.is_delete = True
        self.save()
