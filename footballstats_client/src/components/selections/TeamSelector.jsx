import { useQuery } from "@apollo/client";
import { useContext, useState } from "react";
import { GET_ALL_TEAMS } from "../../api_client";
import { LoadingView } from "../../views/utilities/LoadingView";
import { Autocomplete, AutocompleteItem } from "actify";
import { Body } from "../Body";
import { DateRangeContext } from "../../App";

export function TeamSelector ({nameIsKey, teamKey, setTeamKey, label}) {
    const [selectedKey, setSelectedKey] = useState(teamKey);
    const teamsQuery = useQuery(
        GET_ALL_TEAMS,
        {variables: {startDate: null, endDate: null}}
    );

    if (teamsQuery.loading)
        return <LoadingView/>;
    if (teamsQuery.error)
        return <Body text={teamsQuery.error.cause.message}/>;

    const onKeySelected = (newKey) => {
        setSelectedKey(newKey);
        setTeamKey(newKey);
    };

    return (
        <Autocomplete
            label={label}
            variant="outlined"
            onSelectionChange={teamKey => onKeySelected(teamKey)}
            selectedKey={selectedKey}
        >{
            teamsQuery.data.teamsList &&
            teamsQuery.data.teamsList.map(teamData => (
                <AutocompleteItem key={nameIsKey ? teamData.name : teamData.id}>
                    {teamData.name}
                </AutocompleteItem>
            ))
        }</Autocomplete>
    );
}