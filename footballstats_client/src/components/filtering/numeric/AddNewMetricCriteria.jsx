import { Autocomplete, AutocompleteItem, TextField } from "actify";
import {LoadingView} from "../../../views/utilities/LoadingView"
import EqualsForm from "./EqualsForm";
import { useQuery } from "@apollo/client";
import { GET_ALL_EVENT_TYPES } from "../../../api_client";
import { FilteringCriteria, MetricsNames } from "../../../constants";
import { RangeForm } from "./RangeForm";


export function AddNewMetricCriteria({newFilter, setNewFilter}) {
    const eventTypeQuery = useQuery(GET_ALL_EVENT_TYPES);

    if (eventTypeQuery.loading)
        return <LoadingView/>

    const setParameter = (parameterIndex, newValue) => {
        setNewFilter(prev => ({
            ...prev,
            metric: {
                ...prev.metric,
                metricParams: prev.metric.metricParams.map((param, index) => (
                    index === parameterIndex ? newValue : param
                ))
            }
        }));
    }

    const metricParamsForm = () => {
        const metricName = newFilter.attribute;
        if (metricName === MetricsNames.ODDS_FOR_MORE_THAN) {
            return <TextField
                label={"Szansa na więcej niż"}
                type="number"
                variant="outlined"
                value={newFilter.metric.metricParams[0]}
                onChange={(value) => setParameter(0, value)}
            />
        } else if (metricName === MetricsNames.ODDS_IN_TIME_RANGE)
            return <>
                <TextField
                    label={"Czas początkowy (min)"}
                    type="number"
                    variant="outlined"
                    value={newFilter.metric.metricParams[0]}
                    onChange={(value) => setParameter(0, value)}
                />
                <TextField
                    label={"Czas końcowy (min)"}
                    type="number"
                    variant="outlined"
                    value={newFilter.metric.metricParams[1]}
                    onChange={(value) => setParameter(1, value)}
                />
            </>
        return <></>
    }

    const form = () => {
        switch (newFilter.criteria) {
            case FilteringCriteria.numeric.NUMERIC_EQUALS:
                return <EqualsForm 
                    value={newFilter.parameters[0] ? newFilter.parameters[0] : ""} 
                    setFilter={setNewFilter}
                />;
            case FilteringCriteria.numeric.NUMERIC_IN_CLOSED_RANGE:
                return <RangeForm
                    from={newFilter.parameters[0] ? newFilter.parameters[0] : ""}
                    to={newFilter.parameters[1] ? newFilter.parameters[1] : ""}
                    setFilter={setNewFilter}
                />
            case FilteringCriteria.numeric.NUMERIC_NOT_IN_CLOSED_RANGE:
                return <RangeForm
                    from={newFilter.parameters[0] ? newFilter.parameters[0] : ""}
                    to={newFilter.parameters[1] ? newFilter.parameters[1] : ""}
                    setFilter={setNewFilter}
                />
        }
        return <></>
    };

    return (<>
        <Autocomplete
            variant="outlined"
            searchText={true}
            label={"Wybierz zdarzenie"}
            selectedKey={newFilter.metric.targetMatchEvent}
            onSelectionChange={(event) => setNewFilter(prev => ({
                ...prev, 
                metric: {
                    ...prev.metric,
                    targetMatchEvent: event
                }
            }))}
        >
        {
            eventTypeQuery.data &&
            eventTypeQuery.data.eventTypesList.map((eventType) => (
                <AutocompleteItem key={eventType.id}>
                    {eventType.name}
                </AutocompleteItem>
            ))
        }
        </Autocomplete>
        {
            newFilter.metric.targetMatchEvent &&
            metricParamsForm()
        }
        {
            newFilter.metric.targetMatchEvent &&
            form()
        }
    </>)
}