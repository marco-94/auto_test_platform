from my_user.models import UserList, UserRole, UserDetail
from rest_framework import mixins, generics


# Create your views here.
class UserListView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    # 查询未删除的数据，数据排序方式为新增时间倒序，去掉-，即为顺序排序
    queryset = UserList.objects.filter(is_delete=0).all().order_by('-created_tm')


class UserRoleView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    # 查询未删除的数据，数据排序方式为新增时间倒序，去掉-，即为顺序排序
    queryset = UserRole.objects.filter(is_delete=0).all().order_by('-created_tm')


class UserDetailView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    # 查询未删除的数据，数据排序方式为新增时间倒序，去掉-，即为顺序排序
    queryset = UserDetail.objects.filter(is_delete=0).all().order_by('-created_tm')

