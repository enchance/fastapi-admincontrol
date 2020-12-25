from fastapi import APIRouter, Response, Depends
from app.AuthControl import fapi_user
from pydantic import UUID4


router = APIRouter()
# TODO: Replace fapi_user.get_current_superuser with something for admin


"""
User
"""
@router.get('/user', dependencies=[Depends(fapi_user.get_current_superuser)])
def user_all(response: Response):
    pass


@router.get('/user/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def user_read(response: Response, user_id: UUID4):
    pass


@router.post('/user/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def user_add(response: Response):
    pass


@router.patch('/user/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def user_update(response: Response, user_id: UUID4):
    pass


@router.delete('/user/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def user_delete(response: Response, user_id: UUID4):
    pass


"""
Group
"""
@router.get('/group', dependencies=[Depends(fapi_user.get_current_superuser)])
def group_all(response: Response):
    pass


@router.get('/group/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def group_read(response: Response, user_id: UUID4):
    pass


@router.post('/group', dependencies=[Depends(fapi_user.get_current_superuser)])
def group_add(response: Response):
    pass


@router.patch('/group/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def group_update(response: Response, user_id: UUID4):
    pass


@router.delete('/group/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def group_delete(response: Response, user_id: UUID4):
    pass


"""
Permission
"""
@router.get('/permission', dependencies=[Depends(fapi_user.get_current_superuser)])
def permission_all(response: Response):
    pass


@router.get('/permission/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def permission_read(response: Response, user_id: UUID4):
    pass


@router.post('/permission', dependencies=[Depends(fapi_user.get_current_superuser)])
def permission_add(response: Response):
    pass


@router.patch('/permission/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def permission_update(response: Response, user_id: UUID4):
    pass


@router.delete('/permission/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def permission_delete(response: Response, user_id: UUID4):
    pass


"""
Taxonomy
"""
@router.get('/taxonomy', dependencies=[Depends(fapi_user.get_current_superuser)])
def taxonomy_all(response: Response):
    pass


@router.get('/taxonomy/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def taxonomy_read(response: Response, user_id: UUID4):
    pass


@router.post('/taxonomy', dependencies=[Depends(fapi_user.get_current_superuser)])
def taxonomy_add(response: Response):
    pass


@router.patch('/taxonomy/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def taxonomy_update(response: Response, user_id: UUID4):
    pass


@router.delete('/taxonomy/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def taxonomy_delete(response: Response, user_id: UUID4):
    pass


"""
Option
"""
@router.get('/option', dependencies=[Depends(fapi_user.get_current_superuser)])
def option_all(response: Response):
    pass


@router.get('/option/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def option_read(response: Response, user_id: UUID4):
    pass


@router.post('/option', dependencies=[Depends(fapi_user.get_current_superuser)])
def option_add(response: Response):
    pass


@router.patch('/option/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def option_update(response: Response, user_id: UUID4):
    pass


@router.delete('/option/{user_id}', dependencies=[Depends(fapi_user.get_current_superuser)])
def option_delete(response: Response, user_id: UUID4):
    pass