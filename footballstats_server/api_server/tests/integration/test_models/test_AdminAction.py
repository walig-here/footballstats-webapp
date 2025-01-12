from django.contrib.auth.models import User
from django.test import TestCase

from api_server.models import AdminAction


class Test__AdminAction__on_referenced_user_deleted(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_referenced_user_deleted_then_set_referenced_user_to_NULL(self):
        target_action: AdminAction = AdminAction.objects.all().first()
        target_action.user.delete()
        action_id: int = target_action.pk
        
        self.assertIsNone(AdminAction.objects.get(pk=action_id).user)