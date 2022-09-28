from rest_framework import mixins, generics
from project.project_detail.models import ProjectDetail


# Create your views here.
class ProjectDetailView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    # 查询未删除的数据，数据排序方式为新增时间倒序，去掉-，即为顺序排序
    queryset = ProjectDetail.objects.filter(is_delete=0).all().order_by('-created_tm')