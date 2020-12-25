from typing import Optional
from tortoise import fields, models
from pydantic import BaseModel, EmailStr, Field
from app.core.utils import model_str

from app.settings import settings as s
from app.AuthControl.models import UserDB



class DTMixin(object):
    deleted_at = fields.DatetimeField(null=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)


class UserPermissions(DTMixin, models.Model):
    user = fields.ForeignKeyField('models.UserMod', related_name='user_permissions')
    permission = fields.ForeignKeyField('models.Permission', related_name='user_permissions')
    
    class Meta:
        table = 'auth_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class UserGroups(DTMixin, models.Model):
    user = fields.ForeignKeyField('models.UserMod', related_name='user_groups')
    group = fields.ForeignKeyField('models.Group', related_name='user_groups')
    
    class Meta:
        table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)
    

class Group(models.Model):
    name = fields.CharField(max_length=191, index=True, unique=True)
    summary = fields.TextField(default='')
    deleted_at = fields.DatetimeField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    
    # This table is automatically created with the name from 'through'. But if you want to
    # customize it then create a model and give it the same table name as the 'through'. Add any
    # fields you need in that custom model.
    permissions: models.ManyToManyRelation['Permission'] = \
        fields.ManyToManyField('models.Permission', related_name='groups',
                               through='auth_group_permissions')
    
    class Meta:
        table = 'auth_group'
    
    def __str__(self):
        return model_str(self, 'name')
    

class Permission(models.Model):
    name = fields.CharField(max_length=191, unique=True)
    code = fields.CharField(max_length=191, unique=True)
    deleted_at = fields.DatetimeField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = 'auth_permission'
    
    def __str__(self):
        return model_str(self, 'name')


class GroupPermissions(models.Model):
    group = fields.ForeignKeyField('models.Group', related_name='group_permissions')
    permission = fields.ForeignKeyField('models.Permission', related_name='group_permissions')
    
    class Meta:
        table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)
    
    def __str__(self):
        return f'<{self.__class__.__name__}[{self.id}]>'    # noqa


class Option(models.Model):
    name = fields.CharField(max_length=20)
    value = fields.CharField(max_length=191)
    user = fields.ForeignKeyField('models.UserMod', related_name='options', null=True)
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        table = 'core_options'
    
    def __str__(self):
        return model_str(self, 'name')


class Taxonomy(DTMixin, models.Model):
    name = fields.CharField(max_length=191)
    type = fields.CharField(max_length=20)
    sort = fields.SmallIntField(default=100)
    author = fields.ForeignKeyField('models.UserMod', related_name='tax_author')
    parent = fields.ForeignKeyField('models.Taxonomy', related_name='tax_parent')
    
    class Meta:
        table = 'core_taxonomy'
    
    def __str__(self):
        return model_str(self, 'name')


"""
Pydantic
"""


class RefreshToken(BaseModel):
    pass


class UniqueFieldsRegistration(BaseModel):
    email: Optional[EmailStr]
    username: Optional[str] = Field(None, min_length=s.USERNAME_LEN)
    password: Optional[str] = Field(None, min_length=s.PASSWORD_LEN)


class OptionCreate(BaseModel):
    name: str
    value: str
    user: Optional[UserDB]

class OptionUpdate(BaseModel):
    id: int
    value: str
    user: Optional[UserDB]
    
class OptionDelete(BaseModel):
    id: int
    user: Optional[UserDB]

# class Category(Taxonomy):
#     author = fields.ForeignKeyField('models.User', on_delete=fields.CASCADE,
#                                     related_name='category_author')
#
#     class Meta:
#         abstract = True
#
#
# class Tag(Taxonomy):
#     author = fields.ForeignKeyField('models.User', on_delete=fields.CASCADE,
#                                     related_name='tag_author')
#
#     class Meta:
#         abstract = True
#
#
# class Choice(Taxonomy):
#     author = fields.ForeignKeyField('models.User', on_delete=fields.CASCADE,
#                                     related_name='choice_author')
#
#     class Meta:
#         abstract = True
