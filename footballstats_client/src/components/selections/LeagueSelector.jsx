import { useQuery } from "@apollo/client";
import { GET_ALL_LEAGUES } from "../../api_client";
import { Autocomplete, AutocompleteItem } from "actify";
import { LoadingView } from "../../views/utilities/LoadingView";
import { Body } from "../Body";
import { useState } from "react";
import { SeasonSelector } from "./SeasonSelector";

export function LeagueSelector({nameIsKey, leagueKey, setLeagueKey, seasonKey, setSeasonKey, disableSeasonSelect}) {
    const [selectedLeagueKey, setSelectedLeagueKey] = useState(leagueKey);
    const [selectedSeasonKey, setSelectedSeasonKey] = useState(seasonKey);
    const leaguesQuery = useQuery(GET_ALL_LEAGUES);

    if (leaguesQuery.loading)
        return <LoadingView/>;
    if (leaguesQuery.error)
        return <Body text={leaguesQuery.error.cause.message}/>

    const onLeagueKeySelected = (newKey) => {
        setSelectedLeagueKey(newKey);
        setLeagueKey(newKey);
    }
    const onSeasonKeySelected = (newKey) => {
        setSelectedSeasonKey(newKey);
        setSeasonKey(newKey);
    }

    return (
        <>
            <Autocomplete 
                label={"Liga"} 
                variant="outlined"
                onSelectionChange={(leagueKey) => onLeagueKeySelected(leagueKey)}
                selectedKey={selectedLeagueKey}
            >{
                leaguesQuery.data.leaguesList &&
                leaguesQuery.data.leaguesList.map(leagueData => (
                    <AutocompleteItem key={nameIsKey ? leagueData.name : leagueData.id}>
                        {leagueData.name}
                    </AutocompleteItem>
                ))
            }</Autocomplete>
            {
                !disableSeasonSelect && leagueKey &&
                <SeasonSelector
                    nameIsKey={nameIsKey}
                    seasonKey={selectedSeasonKey}
                    leagueId={Number.parseInt(selectedLeagueKey)}
                    setSeasonKey={seasonId => onSeasonKeySelected(seasonId)}
                />
            }
        </>
    )
}