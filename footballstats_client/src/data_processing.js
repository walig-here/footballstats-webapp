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

/**
 * Converts filtering criteria to text.
 * @param {FilteringCriteria} criteria 
 * @returns 
 */
export function filteringCriteriaToText(criteria) {
    switch (criteria) {
        case constants.FilteringCriteria.textual.TEXTUAL_FULL_TEXT_SEARCH:
            return "Wyszukiwanie pełnotekstowe";
        case constants.FilteringCriteria.textual.TEXTUAL_IN_SET:
            return "W zbiorze";
        case constants.FilteringCriteria.textual.TEXTUAL_NOT_IN_SET:
            return "Nie w zbiorze";
        case constants.FilteringCriteria.numeric.NUMERIC_EQUALS:
            return "Równy";
        case constants.FilteringCriteria.numeric.NUMERIC_IN_CLOSED_RANGE:
            return "Należy do przedziału";
        case constants.FilteringCriteria.numeric.NUMERIC_NOT_IN_CLOSED_RANGE:
            return "Nie należy do przedziału";
    }
    return "N/A";
}

/**
 * Converts filter object from front-end format to back-end format.
 */
export function convertFiltersToBackendFormat(filters) {
    const backendTextualFilters = [];
    const backendMetricFilters = [];
    filters.forEach((filter) => {
        if (Object.keys(constants.FilteringCriteria.textual).includes(filter.criteria))
            backendTextualFilters.push({
                targetAttributeName: filter.attribute,
                filteringCriteria: filter.criteria,
                filterParams: filter.parameters
            });
        else if (Object.keys(constants.FilteringCriteria.numeric).includes(filter.criteria))
            backendMetricFilters.push({
                metric: filter.attribute,
                filteringCriteria: filter.criteria,
                filterParams: filter.parameters
            })
    });
    return [backendTextualFilters, backendMetricFilters];
}

export function capitalize(text) {
    return String(text).charAt(0).toUpperCase() + String(text).slice(1);
}
