import django_filters
from project.project_detail.models import ProjectDetail
from project.project_list.project_list_filter import BaseFilter


class ProjectDetailFilter(BaseFilter):
    project_description = django_filters.CharFilter(field_name='project_description', lookup_expr='icontains')

    class Meta:
        model = ProjectDetail
        fields = ('project_id', 'project_name', 'updated_tm', 'project_description')

