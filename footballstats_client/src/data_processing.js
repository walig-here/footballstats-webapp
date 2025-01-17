import { use } from "react";
import * as constants from "./constants"

export function isOwner(username) {
    return username === constants.OWNER_USERNAME;
}

export function isAuthenticated(username) {
    return username !== null;
}

export function validateTextInput(text) {
    if (text === "")
        return [false, "Pole nie może być puste."]
    return [true, null]
}

export function validateUsername(username) {
    const textInputValidation = validateTextInput(username);
    if (!textInputValidation[0])
        return textInputValidation;
    return [true, null];
}

export function validatePassword(password) {
    const textInputValidation = validateTextInput(password);
    if (!textInputValidation[0])
        return textInputValidation;
    return [true, null];
} 