from django.db import models
from my_user.models import BaseModel
from project.project_list.models import ProjectList


# Create your models here.
class ProjectDetail(BaseModel):
    project_description = models.CharField(max_length=256, help_text="项目描述")
    project_info = models.ForeignKey(to=ProjectList, on_delete=models.DO_NOTHING, db_constraint=False, related_name='project_base', unique=True)

    # 指定数据库表信息
    class Meta:
        db_table = 'project_detail'
        verbose_name = '项目详情信息'
        verbose_name_plural = verbose_name

    # 插拔式连表查询
    @property
    def project_id(self):
        return self.project_info.project_id

    @property
    def project_name(self):
        return self.project_info.project_name
