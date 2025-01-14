from django.contrib.auth.models import User

from api_server.constants import PermissionType


def user_has_permission(user_id: int, permission: PermissionType) -> bool:
    """
    Checks wether user has given permission.

    Params
    - `user_id` (`int`): User's id.
    - `permission` (`PermissionType`): Permission type to check.
    """
    target_user: User = User.objects.get(pk=user_id)
    if target_user.is_superuser:
        return True
    groups: dict[str, str] = list(target_user.groups.all().values_list('id', flat=True))
    return permission.value in groups