export const API_SERVER_URL = "http://127.0.0.1:8000/api_server/"
export const ACCESS_TOKEN = "jwt_access_token"
export const REFRESH_TOKEN = "jwt_refresh_token"
export const USERNAME = "username"

export const LOGIN_PAGE_PATH = "/auth/login"
export const ADD_MATCH_PAGE_PATH = "/form/add_match"
export const PLAYERS_LIST_PAGE_PATH = "/list/players"
export const MATCH_LIST_PAGE_PATH = "/list/matches"
export const TEAM_LIST_PAGE_PATH = "/list/teams"
export const ADMINS_LIST_PAGE_PATH = "/list/admins"
export const REGISTRATION_TOKENS_PAGE_PATH = "/auth/generate_registration_token";
export const UNAUTHORIZED_PAGE = "/auth/unauthorized";

export const TOKEN_EXPIRED_ERROR = "Signature has expired";
export const REFRESH_TOKEN_INVALID = "Invalid refresh token";
export const ACCESS_TOKEN_INVALID = "Error decoding signature";
export const NOT_AUTHORIZED = "You do not have permission to perform this action";

export const OWNER_USERNAME = "owner";
export const UNAUTHENTICATED_USERNAME = null;
export const DEFAULT_USERNAME = null;

export const ERROR_OCCURRED_TOAST = "Wystąpił błąd, odśwież stronę!"

export const PermissionTypes = {
    DELETE: "DELETE",
    EDIT: "EDIT",
    CREATE: "CREATE"
}

export const FilterType = {
    TEXTUAL: "TEXTUAL",
    NUMERIC: "NUMERIC",
    METRIC: "METRIC"
}

export const FilteringCriteria = {
    textual: {
        TEXTUAL_FULL_TEXT_SEARCH: "TEXTUAL_FULL_TEXT_SEARCH",
        TEXTUAL_IN_SET: "TEXTUAL_IN_SET",
        TEXTUAL_NOT_IN_SET: "TEXTUAL_NOT_IN_SET"
    },
    numeric: {
        NUMERIC_EQUALS: "NUMERIC_EQUALS",
        NUMERIC_IN_CLOSED_RANGE: "NUMERIC_IN_CLOSED_RANGE",
        NUMERIC_NOT_IN_CLOSED_RANGE: "NUMERIC_NOT_IN_CLOSED_RANGE"
    }
};

export const Metrics = {
    SUM: "SUM",
    AVERAGE: "AVERAGE",
    ODDS_FOR: "ODDS_FOR",
    ODDS_FOR_MORE_THAN: "ODDS_FOR_MORE_THAN",
    MINUTES_UNTIL: "MINUTES_UNTIL",
    ODDS_IN_TIME_RANGE: "ODDS_IN_TIME_RANGE"
}

export const MetricsNames = {
    SUM: "Suma",
    AVERAGE: "Średnia",
    ODDS_FOR: "Szansa na",
    ODDS_FOR_MORE_THAN: "Szansa na więcej niż",
    MINUTES_UNTIL: "Minut do pierwszego",
    ODDS_IN_TIME_RANGE: "Szansa w przedziale czasowym"
}


export const QueriesForFilteringAttributesValues = {
    QUERY_USERNAMES: ["login"],
    QUERY_PLAYERS_NAMES: ["imie", "imie reprezentującego zawodnika", "imie uczestniczącego zawodnika"],
    QUERY_PLAYERS_SURNAMES: ["nazwisko", "nazwisko reprezentującego zawodnika", "nazwisko uczestniczącego zawodnika"],
    QUERY_TEAMS_NAMES: ["nazwa drużyny", "nazwa reprezentowanej drużyny", "nazwa uczestniczącej drużuny"],
    QUERY_COUNTRIES: ["nazwa kraju pochodzenia", "nazwa kraju pochodzenia ligi"],
    QUERY_LEAGUES: ["nazwa ligii z udziałem drużyny", "nazwa ligi", "nazwa ligi z udziałem zawodnika"],
}

export const MatchEvents = {
    "1": "FAILED_PASS",
    "2": "SUCCESSFUL_PASS",
    "3": "CORNER",
    "4": "YELLOW_CARD",
    "5": "RED_CARD",
    "6": "GOAL",
    "7": "SHOT_ON_TARGET",
    "8": "SHOT_NOT_ON_TARGET",
    "9": "DEFENSE",
    "10": "WIN",
    "11": "DEFEAT",
    "12": "DRAW"
}