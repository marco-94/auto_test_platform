import django_filters
from my_user.models import UserList, UserRole, UserDetail, BaseModel


class BaseFilter(django_filters.rest_framework.FilterSet):
    user_id = django_filters.NumberFilter(field_name='user_id', lookup_expr='exact')
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = BaseModel
        fields = ('user_id', 'username')


class UserListFilter(BaseFilter):

    class Meta:
        model = UserList
        fields = ('user_id', 'username', 'email', 'is_disable', 'updated_tm', 'created_tm',  'is_superuser')


class UserRoleFilter(BaseFilter):
    user_token = django_filters.CharFilter(field_name='user_token', lookup_expr='icontains')

    class Meta:
        model = UserRole
        fields = ('user_id', 'username', 'updated_tm', 'created_tm')


class UserDetailFilter(BaseFilter):
    nickname = django_filters.CharFilter(field_name='nickname', lookup_expr='icontains')
    user_introduction = django_filters.CharFilter(field_name='user_introduction', lookup_expr='icontains')

    class Meta:
        model = UserDetail
        fields = ('user_id', 'username', 'updated_tm', 'created_tm', 'nickname', 'user_introduction')
