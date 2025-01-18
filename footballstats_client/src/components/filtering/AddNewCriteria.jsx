import { Button, Icon, Select, SelectOption } from "actify";
import { useEffect, useState } from "react";
import { FilteringCriteria, MetricsNames } from "../../constants";
import { filteringCriteriaToText } from "../../data_processing";
import {FullTextSearchForm} from "./textual/FullTextSearchForm";
import { SetForm } from "./textual/SetForm";
import { AddNewMetricCriteria } from "./numeric/AddNewMetricCriteria";

const FILTERING_ATTRIBUTE = "Element filtrujący";
const ADD_FILTER = "Dodaj filtr";
const CANCEL = "Anuluj";


function getDefaultMetricParams(metricName) {
    if (metricName === MetricsNames.ODDS_FOR_MORE_THAN)
        return [""];
    else if (metricName === MetricsNames.ODDS_IN_TIME_RANGE)
        return ["", ""];
    return [];
}

const DEFAULT_METRIC_VALUE = (attribute) => ({
    targetMatchEvent: null,
    metricParams: getDefaultMetricParams(attribute)
})

export function AddNewCriteria({ 
    textualFilteringElements, 
    metricFilteringElements, 
    onClose, 
    onConfirm
}) {
    const [newFilter, setNewFilter] = useState({
        attribute: null,
        criteria: null,
        parameters: [],
        metric: DEFAULT_METRIC_VALUE(null)
    });
    const filteringElements = [...textualFilteringElements, ...metricFilteringElements];

    useEffect(() => {
        setNewFilter(prev => ({...prev, metric: DEFAULT_METRIC_VALUE(prev.attribute)}));
    }, [newFilter.attribute])

    const confirm = () => {
        console.log(newFilter);
        onConfirm(newFilter);
    }

    const criteriaSelect = () => {
        if (textualFilteringElements.includes(newFilter.attribute)) {
            return Object.entries(FilteringCriteria.textual).map(([key]) => (
                <SelectOption key={key}>
                    {filteringCriteriaToText(key)}
                </SelectOption>
            ));
        } else if (metricFilteringElements.includes(newFilter.attribute)) {
            return Object.entries(FilteringCriteria.numeric).map(([key]) => (
                <SelectOption key={key}>
                    {filteringCriteriaToText(key)}
                </SelectOption>
            ));
        }
        return <></>
    };

    const form = () => {
        if (Object.keys(FilteringCriteria.numeric).includes(newFilter.criteria)){
            return <AddNewMetricCriteria 
                newFilter={newFilter} 
                setNewFilter={setNewFilter}
            />;
        }
        switch (newFilter.criteria) {
            case FilteringCriteria.textual.TEXTUAL_FULL_TEXT_SEARCH:
                return <FullTextSearchForm 
                    searchText={newFilter.parameters[0] ? newFilter.parameters[0] : ""} 
                    setNewFilter={setNewFilter}
                />
            case FilteringCriteria.textual.TEXTUAL_IN_SET:
                return <SetForm 
                    attribute={newFilter.attribute}
                    chosenElements={newFilter.parameters} 
                    setChosenElements={(newParams) => setNewFilter(prev => ({...prev, parameters:newParams}))}
                />
            case FilteringCriteria.textual.TEXTUAL_NOT_IN_SET:
                    return <SetForm
                        attribute={newFilter.attribute}
                        chosenElements={newFilter.parameters} 
                        setChosenElements={(newParams) => setNewFilter(prev => ({...prev, parameters:newParams}))}
                    />
        }
        return <></>
    }

    return (
        <div className="flex flex-col justify-between space-y-4">
            <Select
                variant="outlined"
                label={FILTERING_ATTRIBUTE}
                onSelectionChange={
                    (attribute) => setNewFilter(prev => ({
                        ...prev, 
                        attribute: attribute, 
                        criteria: null, 
                        parameters: [], 
                        metric: DEFAULT_METRIC_VALUE(prev.attribute)
                    }))
                }
                selectedKey={newFilter.attribute}
            >
                {
                    filteringElements.map((attribute, index) => (
                        <SelectOption key={attribute}>
                            {attribute}
                        </SelectOption>
                    ))
                }
            </Select>
            {
                newFilter.attribute && 
                <Select 
                    variant="outlined" 
                    label="Kryterium"
                    selectedKey={newFilter.criteria}
                    onSelectionChange={
                        (criteria) => setNewFilter(prev => ({
                            ...prev, criteria: criteria, parameters: []
                        }))
                    }
                >
                    {criteriaSelect()}
                </Select>
            }
            {
                newFilter.criteria &&
                form()
            }
            <div className="flex flex-col space-y-2">
                {
                    newFilter.parameters.length != 0 &&
                    <Button
                        variant="filled"
                        onPress={() => confirm()}
                    >
                        <Icon>check</Icon>{ADD_FILTER}
                    </Button>
                }
                <Button
                    variant="tonal"
                    onPress={onClose}
                >
                    <Icon>close</Icon>{CANCEL}
                </Button>
            </div>
        </div>
    );
}