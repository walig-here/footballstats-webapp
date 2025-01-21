import { useQuery } from "@apollo/client";
import { GET_ALL_COUNTRIES } from "../../api_client";
import { LoadingView } from "../../views/utilities/LoadingView";
import { Body } from "../Body";
import { Autocomplete, AutocompleteItem } from "actify";
import { useState } from "react";

export function CountrySelector ({label, nameIsKey, countryKey, setCountryKey}) {
    const [selectedKey, setSelectedKey] = useState(countryKey);
    const countriesQuery = useQuery(GET_ALL_COUNTRIES);

    if (countriesQuery.loading)
        return <LoadingView/>;
    if (countriesQuery.error)
        return <Body text={countriesQuery.error.cause.message}/>

    const onKeySelected = (newKey) => {
        setSelectedKey(newKey);
        setCountryKey(newKey);
    }

    return (
        <Autocomplete
            label={label}
            variant="outlined"
            onSelectionChange={countryKey => onKeySelected(countryKey)}
            selectedKey={selectedKey}
        >{
            countriesQuery.data.countryList &&
            countriesQuery.data.countryList.map(countryData => (
                <AutocompleteItem key={nameIsKey ? countryData.name : countryData.id}>
                    {countryData.name}
                </AutocompleteItem>
            ))
        }</Autocomplete>
    );
}