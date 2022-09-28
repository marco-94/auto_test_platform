from rest_framework import serializers
from my_user.models import UserList, UserRole, UserDetail, BaseModel


class BaseSerializers(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(source="created_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True,
                                            help_text='创建时间')
    update_time = serializers.DateTimeField(source="updated_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True,
                                            help_text='更新时间')

    class Meta:
        model = BaseModel
        fields = ('create_time', 'update_time')


class UserListSerializer(BaseSerializers):
    # 设置只读只写
    is_disable = serializers.BooleanField(read_only=True)
    is_delete = serializers.BooleanField(write_only=True, required=False, help_text='是否删除')
    password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=True)

    # 设置非必填
    user_introduction = serializers.CharField(required=False)
    nickname = serializers.CharField(required=False)

    class Meta:
        model = UserList

        # 定义需要返回的字段及顺序
        exclude = ('created_tm', 'updated_tm')  # 过滤字段


class UserRoleSerializer(BaseSerializers):
    """用户登录信息"""

    class Meta:
        model = UserRole

        # 定义需要返回的字段及顺序
        fields = ('id',
                  'user_id',
                  'user_name',
                  'user_token',
                  'create_time',
                  'update_time')


class UserDetailSerializer(BaseSerializers):
    """用户详情信息"""

    class Meta:
        model = UserDetail

        # 定义需要返回的字段及顺序
        fields = ('id',
                  'user_id',
                  'user_name',
                  'nickname',
                  'user_email',
                  'user_introduction',
                  'create_time',
                  'update_time')
