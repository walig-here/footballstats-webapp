from django.test import SimpleTestCase
from graphene.test import Client as GraphQlClient

from api_server.views import schema

from api_server.tests.__data__.graphql.queries import PlayerQuery as global_data
from api_server.tests import testconf as global_testconf


class Test__PlayerQuery__player_sorting_attributes(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_when_client_queries_then_return_sorting_attributes(self):
        response: dict = self.client.execute(
            global_data.PLAYER_SORTING_ATTRIBUTES_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, global_data.PLAYER_SORTING_ATTRIBUTES_RESPONSE)


class Test__PlayerQuery__player_filtering_attributes(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_when_client_queries_then_return_filtering_attributes(self):
        response: dict = self.client.execute(
            global_data.PLAYER_FILTERING_ATTRIBUTES_REQUEST,
            context=global_testconf.get_graphql_context_with_viewer_user()
        )
        self.assertEqual(response, global_data.PLAYER_FILTERING_ATTRIBUTES_RESPONSE)


class Test__PlayerQuery__player(SimpleTestCase):
    def setUp(self):
        self.client: GraphQlClient = GraphQlClient(schema=schema)

    def test_when_client_provided_id_of_not_existing_player_then_return_error(self):
        ...

    def test_when_client_provided_invalid_match_for_metric_calculation_then_return_error(self):
        ...

    def test_when_client_provided_invalid_team_for_metric_calculation_then_return_error(self):
        ...

class Test__PlayerQuery__player_list(SimpleTestCase):
    def test_when_client_provided_too_many_arguments_for_full_tex_search_filtering_then_return_error(self):
        ...

    def test_when_client_provided_too_little_arguments_for_full_tex_search_filtering_then_return_error(self):
        ...

    def test_when_result_list_has_less_than_25_objects_and_page_0_then_return_less_all_possible_objects(self):
        ...

    def test_when_result_list_has_less_than_25_objects_and_page_not_0_then_return_nothing(self):
        ...

    def test_when_result_number_of_objects_not_divisible_by_page_length_then_return_all_possible_objects(self):
        ...

    def test_when_no_match_found_while_querying_for_match_players_return_error(self):
        ...

    def test_when_no_team_found_while_querying_for_team_players_return_error(self):
        ...

    def test_when_to_little_params_passed_for_equals_metric_filter_then_return_error(self):
        ...

    def test_when_to_many_params_passed_for_equals_metric_filter_then_return_error(self):
        ...

    def test_when_invalid_number_of_params_passed_for_in_range_then_return_error(self):
        ...

    def test_when_invalid_number_of_params_passed_for_not_in_range_then_return_error(self):
        ...