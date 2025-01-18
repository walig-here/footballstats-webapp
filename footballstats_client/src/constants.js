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

export const PermissionTypes = {
    DELETE: "DELETE",
    EDIT: "EDIT",
    CREATE: "CREATE"
}