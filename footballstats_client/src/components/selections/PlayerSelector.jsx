import { useQuery } from "@apollo/client";
import { useContext, useState } from "react";
import { GET_ALL_PLAYERS, GET_PLAYERS } from "../../api_client";
import { DateRangeContext } from "../../App";
import { LoadingView } from "../../views/utilities/LoadingView";
import { Body } from "../Body";
import { Autocomplete, AutocompleteItem } from "actify";

export function PlayerSelector ({nameIsKey, playerKey, setPlayerKey, match}) {
    const [selectedKey, setSelectedKey] = useState(playerKey);
    const playersQuery = useQuery(
        GET_ALL_PLAYERS, 
        {variables: {startDate: null, endDate: null, match: match}}
    );

    if (playersQuery.loading)
        return <LoadingView/>;
    if (playersQuery.error)
        return <Body text={playersQuery.error.cause.message}/>;
    console.log(`Fetched ${playersQuery.data.playersList.length} players`)

    const onKeySelected = (newKey) => {
        setSelectedKey(newKey);
        setPlayerKey(newKey);
    }

    return (
        <Autocomplete
            label="Wyszukaj zawodnika"
            variant="outlined"
            onSelectionChange={playerKey => onKeySelected(playerKey)}
            selectedKey={selectedKey}
        >{
            playersQuery.data.playersList &&
            playersQuery.data.playersList.map(playerData => (
                <AutocompleteItem key={nameIsKey ? `${playerData.name} ${playerData.surname}` : playerData.id}>
                    {`${playerData.name} ${playerData.surname}`}
                </AutocompleteItem>
            ))
        }</Autocomplete>
    )
}