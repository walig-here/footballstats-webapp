from django.test import TestCase

from api_server.models import Country
from api_server.tests.integration.testconf import delete_all_objects_referencing_country


ID_BRAZIL: int = 15


class Test__Country__automatic_delete(TestCase):
    fixtures = ["5matches_2admins"]

    def test_when_country_is_not_referenced_by_any_other_object_then_delete_country(self):
        country = Country.objects.get(pk=ID_BRAZIL)
        delete_all_objects_referencing_country(country)
        self.assertEqual(len(Country.objects.filter(pk=ID_BRAZIL)), 0)