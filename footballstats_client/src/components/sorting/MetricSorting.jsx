import { useQuery } from "@apollo/client";
import { Autocomplete, AutocompleteItem, TextField } from "actify";
import { GET_ALL_EVENT_TYPES } from "../../api_client";
import { LoadingView } from "../../views/utilities/LoadingView";

export function MetricSorting({sorting, setSorting}) {
    const eventTypesQuery = useQuery(GET_ALL_EVENT_TYPES);

    if (eventTypesQuery.loading)
        return <LoadingView/>

    return <>
        <Autocomplete
            variant="outlined"
            label="Wybierz zdarzenie"
            selectedKey={sorting.metric.targetEventType}
            onSelectionChange={(eventType) => setSorting(prev => ({
                ...prev,
                metric: {
                    ...prev.metric,
                    targetEventType: eventType
                }
            }))}
        >
            {
                eventTypesQuery.data && eventTypesQuery.data.eventTypesList &&
                eventTypesQuery.data.eventTypesList.map((eventType) => (
                    <AutocompleteItem key={eventType.id}>
                        {eventType.name}
                    </AutocompleteItem>
                ))
            }
        </Autocomplete>
    </>
}