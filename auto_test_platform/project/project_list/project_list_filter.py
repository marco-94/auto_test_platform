import django_filters
from my_user.models import BaseModel
from project.project_list.models import ProjectList


class BaseFilter(django_filters.rest_framework.FilterSet):
    project_id = django_filters.NumberFilter(field_name='project_id', lookup_expr='exact')
    project_name = django_filters.CharFilter(field_name='project_name', lookup_expr='icontains')

    class Meta:
        model = BaseModel
        fields = ('project_id', 'project_name')


class ProjectListFilter(BaseFilter):

    class Meta:
        model = ProjectList
        fields = ('project_id', 'project_name', 'updated_tm', 'created_tm')

