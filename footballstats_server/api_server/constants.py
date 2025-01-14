from enum import Enum


OBJECTS_PER_PAGE: int = 25

# MATCH EVENTS
class MatchEvents(Enum):
    FAILED_PASS = 1
    SUCCESSFUL_PASS = 2
    CORNER = 3
    YELLOW_CARD = 4
    RED_CARD = 5
    GOAL = 6
    SHOT_ON_TARGET = 7
    SHOT_NOT_ON_TARGET = 8
    DEFENSE = 9
    WIN = 10
    DEFEAT = 11
    DRAW = 12

# METRICS
class Metrics(Enum):
    SUM = 0
    AVERAGE = 1
    ODDS_FOR = 2
    ODDS_FOR_MORE_THAN = 3
    MINUTES_UNTIL = 4
    ODDS_IN_TIME_RANGE = 5

class MetricScope(Enum):
    METRIC_FOR_ALL_MATCHES: int = -1
    METRIC_FOR_ANY_TEAM: int = -2

METRIC_UNDEFINED_VALUE: float = -1

# FILTERS
class NumericFilteringCriteria(Enum):
    NUMERIC_EQUALS = "NUMERIC_EQUALS"
    NUMERIC_IN_CLOSED_RANGE = "NUMERIC_IN_CLOSED_RANGE"
    NUMERIC_NOT_IN_CLOSED_RANGE = "NUMERIC_NOT_IN_CLOSED_RANGE"

class TextualFilteringCriteria(Enum):
    TEXTUAL_FULL_TEXT_SEARCH = "TEXTUAL_FULL_TEXT_SEARCH"
    TEXTUAL_IN_SET = "TEXTUAL_IN_SET"
    TEXTUAL_NOT_IN_SET = "TEXTUAL_NOT_IN_SET"

USER_FILTER_ATTRIBUTES: dict[str, str] = {
    "login": "username"
}
PLAYER_FILTER_ATTRIBUTES: dict[str, str] = {
    "imie": "name",
    "nazwisko": "surname",
    "pseudonim": "nickname",
    "nazwa kraju pochodzenia": "country_of_origin__name",
    "nazwa reprezentowanej drużyny": "playerinmatch__team__name",
    "nazwa ligi z udziałem zawodnika": "playerinmatch__match__league_season__league__name",
}
TEAM_FILTER_ATTRIBUTES: dict[str, str] = {
    "nazwa": "name",
    "imie reprezentującego zawodnika": "playerinmatch__player__name",
    "nazwisko reprezentującego zawodnika": "playerinmatch__player__surname",
    "nazwa ligii z udziałem drużyny": "playerinmatch__match__league_season__league__name",
    "nazwa kraju pochodzenia": "country_of_origin__name"
}
MATCH_FILTER_ATTRIBUTES: dict[str, str] = {
    "nazwa ligi": "league_season__league__name",
    "nazwa sezonu ligi": "league_season__name",
    "nazwa uczestniczącej drużuny": "playerinmatch__team__name",
    "imie uczestniczącego zawodnika": "playerinmatch__player__name",
    "nazwisko uczestniczącego zawodnika": "playerinmatch__player__surname",
    "nazwa kraju pochodzenia ligi": "league_season__league__country_of_origin__name",
}

# SORTING
USER_SORT_ATTRIBUTES: dict[str, str] = {
    "login": "username"
}
PLAYER_SORT_ATTRIBUTES: dict[str, str] = {
    "imie": "name",
    "nazwisko": "surname",
    "pseudonim": "nickname",
    "nazwa kraju pochodzenia": "country_of_origin__name",
}
TEAM_SORT_ATTRIBUTES: dict[str, str] = {
    "nazwa": "name",
    "nazwa kraju pochodzenia": "country_of_origin__name"
}
MATCH_SORT_ATTRIBUTES: dict[str, str] = {
    "nazwa ligi": "league_season__league__name",
    "nazwa sezonu ligi": "league_season__name",
    "nazwa kraju pochodzenia ligi": "league_season__league__country_of_origin__name",
    "data rozegrania": "game_date"
}

class SortingDirection(Enum):
    ASCENDING = ""
    DESCENDING = "-"

# PERMISSIONS
class PermissionType(Enum):
    CREATE = 1
    EDIT = 2
    DELETE = 3


MATCH_LENGTH_MINUTES: float = 90.0

OWNER_USERNAME: str = "owner"