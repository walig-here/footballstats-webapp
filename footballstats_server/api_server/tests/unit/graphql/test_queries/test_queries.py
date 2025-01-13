from django.db.models import QuerySet
from django.test import SimpleTestCase

from api_server.graphql.queries import _get_page_from_query_set

from api_server.tests.unit.__data__.graphql.queries import queries as data


class Test__get_page_from_query_set(SimpleTestCase):
    def test_when_result_list_has_more_than_50_objects_and_page_0_then_return_25_objects(self):
        query_set_page: QuerySet = _get_page_from_query_set(data.QUERY_WITH_MORE_THAN_25_OBJECTS, 0)
        self.assertEqual(query_set_page, data.QUERY_WITH_MORE_THAN_25_OBJECTS[:25])

    def test_when_result_list_has_more_than_50_objects_and_page_not_0_then_return_25_objects(self):
        query_set_page: QuerySet = _get_page_from_query_set(data.QUERY_WITH_MORE_THAN_25_OBJECTS, 1)
        self.assertEqual(query_set_page, data.QUERY_WITH_MORE_THAN_25_OBJECTS[25:50])

    def test_when_result_list_has_less_than_25_objects_and_page_0_then_return_less_all_possible_objects(self):
        query_set_page: QuerySet = _get_page_from_query_set(data.QUERY_SET_WITH_LESS_THAN_25_OBJECTS, 0)
        self.assertEqual(query_set_page, data.QUERY_SET_WITH_LESS_THAN_25_OBJECTS)

    def test_when_result_list_has_less_than_25_objects_and_page_not_0_then_return_nothing(self):
        query_set_page: QuerySet = _get_page_from_query_set(data.QUERY_SET_WITH_LESS_THAN_25_OBJECTS, 2)
        self.assertEqual(query_set_page, [])

    def test_when_result_number_of_objects_not_divisible_by_page_length_then_return_all_possible_objects(self):
        query_set_page: QuerySet = _get_page_from_query_set(data.QUERY_WITH_MORE_THAN_25_OBJECTS, 2)
        self.assertEqual(query_set_page, data.QUERY_WITH_MORE_THAN_25_OBJECTS[50:])
