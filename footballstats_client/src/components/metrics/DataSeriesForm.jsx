import { useQuery } from "@apollo/client";
import { GET_ALL_EVENT_TYPES } from "../../api_client";
import { LoadingView } from "../../views/utilities/LoadingView";
import { Autocomplete, AutocompleteItem, Button, Icon, TextField } from "actify";
import { useEffect, useState } from "react";
import { DataSeries, MetricsNames } from "../../constants";
import { toast } from "react-toastify";

const getParamsArrayForMetricType = (metricName) => {
    switch (metricName) {
        case MetricsNames.ODDS_FOR_MORE_THAN:
            return [""];
        case MetricsNames.ODDS_IN_TIME_RANGE:
            return ["", ""];
    }
    return [];
}

export function DataSeriesForm({dataSeries, setDataSeries, metricName,}) {
    const eventTypesQuery = useQuery(GET_ALL_EVENT_TYPES);
    const [newDataSeries, setNewDataSeries] = useState(
        new DataSeries(null, getParamsArrayForMetricType(metricName))
    );

    useEffect(() => {
        setNewDataSeries(new DataSeries(null, getParamsArrayForMetricType(metricName)));
    }, [metricName]);

    const saveNewDataSeries = () => {
        setDataSeries(prev => [...prev, newDataSeries])
    }

    if (eventTypesQuery.loading)
        return <LoadingView/>

    const getFormForMetricParams = () => {
        const submitButton = (
            <Button 
                onPress={() => saveNewDataSeries()} 
                variant="filled"
            >
                <Icon>check</Icon>
                Zatwierdź
            </Button>
        );
        switch (metricName) {
            case MetricsNames.ODDS_FOR_MORE_THAN:
                return (
                    <>
                        <TextField 
                            label={"Więcej niż"} 
                            variant="outlined" 
                            type="number"
                            value={newDataSeries.metricParams[0]}
                            onChange={(value) => {
                                setNewDataSeries(prev => new DataSeries(prev.eventName, [value]))
                            }}
                        />
                        {newDataSeries.metricParams[0] && submitButton}
                    </>
                );
            case MetricsNames.ODDS_IN_TIME_RANGE:
                return (
                    <>
                        <TextField 
                            label={"Początek przediału (min)"} 
                            variant="outlined" 
                            type="number"
                            value={newDataSeries.metricParams[0]}
                            onChange={(value) => {
                                setNewDataSeries(prev => new DataSeries(
                                    prev.eventName, [value, prev.metricParams[1]]
                                ))
                            }}
                        />
                        <TextField 
                            label={"Koniec przedziału (min)"} 
                            variant="outlined" 
                            type="number"
                            value={newDataSeries.metricParams[1]}
                            onChange={(value) => {
                                setNewDataSeries(prev => new DataSeries(
                                    prev.eventName, [prev.metricParams[0], value]
                                ))
                            }}
                        />
                        {
                            (newDataSeries.metricParams[0] && newDataSeries.metricParams[1]) &&
                            submitButton
                        }
                    </>
                );
        }
        return submitButton;
    }

    return (<>
        <Autocomplete
            label="Wybierz zdarzenie"
            selectedKey={newDataSeries.eventName}
            onSelectionChange={
                (eventName) => setNewDataSeries(prev => new DataSeries(eventName, prev.metricParams))
            }
            variant="outlined"
        >
            {
                eventTypesQuery.data ?
                eventTypesQuery.data.eventTypesList.map(eventType => (
                    <AutocompleteItem key={eventType.name}>{eventType.name}</AutocompleteItem>
                )) :
                eventTypesQuery.error.cause.message
            }
        </Autocomplete>
        {
            newDataSeries.eventName &&
            getFormForMetricParams()
        }
    </>)
}