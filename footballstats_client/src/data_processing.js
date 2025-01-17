import * as constants from "./constants"

export function isOwner(username) {
    return username === constants.OWNER_USERNAME;
}

export function isAuthenticated(username) {
    return username !== null;
}