import { useQuery } from "@apollo/client";
import { GET_ALL_COUNTRIES, GET_ALL_EVENT_TYPES } from "../../api_client";
import { LoadingView } from "../../views/utilities/LoadingView";
import { Body } from "../Body";
import { Autocomplete, AutocompleteItem } from "actify";
import { useState } from "react";

export function EventTypeSelector ({label, nameIsKey, eventTypeKey, setEventTypeKey}) {
    const [selectedKey, setSelectedKey] = useState(eventTypeKey);
    const eventTypesQuery = useQuery(GET_ALL_EVENT_TYPES);

    if (eventTypesQuery.loading)
        return <LoadingView/>;
    if (eventTypesQuery.error)
        return <Body text={eventTypesQuery.error.cause.message}/>

    const onKeySelected = (newKey) => {
        setSelectedKey(newKey);
        setEventTypeKey(newKey);
    }

    return (
        <Autocomplete
            label={label}
            variant="outlined"
            onSelectionChange={countryKey => onKeySelected(countryKey)}
            selectedKey={selectedKey}
        >{
            eventTypesQuery.data.eventTypesList &&
            eventTypesQuery.data.eventTypesList.map(eventType => (
                <AutocompleteItem key={nameIsKey ? eventType.name : eventType.id}>
                    {eventType.name}
                </AutocompleteItem>
            ))
        }</Autocomplete>
    );
}