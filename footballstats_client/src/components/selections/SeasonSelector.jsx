import { useQuery } from "@apollo/client";
import { buildLeagueSeasonsQuery, GET_ALL_LEAGUE_SEASONS } from "../../api_client";
import { LoadingView } from "../../views/utilities/LoadingView";
import { Body } from "../Body";
import { Autocomplete, AutocompleteItem } from "actify";
import { useState } from "react";

export function SeasonSelector ({nameIsKey, seasonKey, setSeasonKey, leagueId}) {
    const [selectedKey, setSelectedKey] = useState(seasonKey);
    const seasonQuery = useQuery(...buildLeagueSeasonsQuery(leagueId));

    if (seasonQuery.loading)
        return <LoadingView/>;
    if (seasonQuery.error)
        return <Body text={seasonQuery.error.cause.message}/>;

    const onKeySelected = (newKey) => {
        setSelectedKey(newKey);
        setSeasonKey(newKey);
    }

    return (
        <Autocomplete
            label="Sezon"
            variant="outlined"
            onSelectionChange={seasonKey => onKeySelected(seasonKey)}
            selectedKey={selectedKey}
        >{
            seasonQuery.data.leagueSeasonsList &&
            seasonQuery.data.leagueSeasonsList.map(seasonData => (
                <AutocompleteItem key={nameIsKey ? seasonData.name : seasonData.id}>
                    {seasonData.name}
                </AutocompleteItem>
            ))
        }</Autocomplete>
    )
}