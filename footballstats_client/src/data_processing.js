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
                metric: {
                    ...filter.metric,
                    metricType: Object.keys(constants.MetricsNames).find(
                        key => constants.MetricsNames[key] === filter.attribute
                    ),
                    targetMatchEvent: constants.MatchEvents[filter.metric.targetMatchEvent],
                },
                filteringCriteria: filter.criteria,
                filterParams: filter.parameters.map(parameter => parseFloat(parameter))
            })
    });
    return [backendTextualFilters, backendMetricFilters];
}

export function capitalize(text) {
    return String(text).charAt(0).toUpperCase() + String(text).slice(1);
}

export function convertSortingToBackendFormat(sorting) {
    const metricParameters = sorting.metric.metricParams.join(' ');
    let targetAttributeName = (
        sorting.metric.targetEventType ?
        Object.keys(constants.MetricsNames).find(
            key => constants.MetricsNames[key] === sorting.targetAttributeName
        ) :
        sorting.targetAttributeName 
    );
    if (sorting.metric.targetEventType) {
        targetAttributeName += (
            metricParameters === "" ?
            ` ${constants.MatchEvents[sorting.metric.targetEventType]}` :
            ` ${constants.MatchEvents[sorting.metric.targetEventType]} ${metricParameters}`
        )
    }
    return {
        targetAttributeName: targetAttributeName,
        direction: sorting.direction,
    }
}

const SECONDS_PER_DAY = 86400;
const DAYS_BETWEEN_YEAR_1_AND_1970 = Date.parse("0001-01-01") / 1E3 / SECONDS_PER_DAY;

/**
 * Converts date string to integer that contains number of days since January 1st 1970.
 */
export function convertDateStringToInteger(dateString) {
    const date = Date.parse(dateString) / 1E3 / SECONDS_PER_DAY - DAYS_BETWEEN_YEAR_1_AND_1970;
    return date;
}

export function convertNumberToDateString(daysSinceYear0) {
    const secondsSince1970 = (daysSinceYear0 + DAYS_BETWEEN_YEAR_1_AND_1970) * SECONDS_PER_DAY * 1E3;
    return new Date(secondsSince1970).toISOString().split("T")[0];
}