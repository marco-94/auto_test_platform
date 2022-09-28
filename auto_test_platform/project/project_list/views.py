from rest_framework import mixins, generics
from project.project_list.models import ProjectList


# Create your views here.
class ProjectListView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    # 查询未删除的数据，数据排序方式为新增时间倒序，去掉-，即为顺序排序
    queryset = ProjectList.objects.filter(is_delete=0).all().order_by('-created_tm')
