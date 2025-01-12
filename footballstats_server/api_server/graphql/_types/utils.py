import graphene

import api_server.constants as constants


class SortingType(graphene.InputObjectType):
    target_attribute_name: graphene.String = graphene.String()
    direction: graphene.Enum = graphene.Enum("SortingDirectionType", [("ASCENDING", 0), ("DESCENDING", 1)])()


class NumericFilteringCriteriaType(graphene.Enum):
    NUMERIC_EQUALS = 0
    NUMERIC_IN_CLOSED_RANGE = 1
    NUMERIC_NOT_IN_CLOSED_RANGE = 2


class MetricType(graphene.InputObjectType):
    metric_type: graphene.Enum = graphene.Enum.from_enum(constants.Metrics)()
    target_match_event: graphene.Enum = graphene.Enum.from_enum(constants.MatchEvents)()
    metric_params: graphene.List = graphene.List(graphene.String)


class MetricFilterType(graphene.InputObjectType):
    metric: MetricType = MetricType()
    filtering_criteria: graphene.Enum = graphene.Enum.from_enum(constants.NumericFilteringCriteria)()
    filter_params: graphene.List = graphene.List(graphene.Float)


class NumericalFilterType(graphene.InputObjectType):
    target_attribute_name: graphene.String = graphene.String()
    filtering_criteria: graphene.Enum = graphene.Enum.from_enum(constants.NumericFilteringCriteria)()
    filter_params: graphene.List = graphene.List(graphene.Float)


class TextualFilterType(graphene.InputObjectType):
    target_attribute_name: graphene.String = graphene.String()
    filtering_criteria: graphene.Enum = graphene.Enum.from_enum(constants.TextualFilteringCriteria)()
    filter_params: graphene.List = graphene.List(graphene.String)