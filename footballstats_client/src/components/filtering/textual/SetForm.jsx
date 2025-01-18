import { useContext, useEffect, useState } from "react";
import { QueriesForFilteringAttributesValues } from "../../../constants";
import { getAllUsernames, getAllPlayersNames, getAllPlayersSurnames, getAllTeamsNames, getAllCountriesNames, getAllLeagueNames  } from "../../../api_client";
import { Autocomplete, AutocompleteItem, Button, ChipGroup, ChipItem, Icon } from "actify";
import {DateRangeContext} from '../../../App';
import { LoadingView } from "../../../views/utilities/LoadingView";


export function SetForm({chosenElements, setChosenElements, attribute}) {
    const [possibleElements, setPossibleElements] = useState([]);
    const [newElement, setNewElement] = useState("");
    const [isLoading, setIsLoading] = useState(true);
    const dateRange = useContext(DateRangeContext);

    useEffect(() => {
        if (QueriesForFilteringAttributesValues.QUERY_USERNAMES.includes(attribute))
            getAllUsernames().then((usernames) => {
                setPossibleElements(usernames);
            });
        else if (QueriesForFilteringAttributesValues.QUERY_PLAYERS_NAMES.includes(attribute))
            getAllPlayersNames(dateRange.startDate, dateRange.endDate).then((playerNames) => {
                setPossibleElements(playerNames);
            });
        else if (QueriesForFilteringAttributesValues.QUERY_PLAYERS_SURNAMES.includes(attribute))
            getAllPlayersSurnames(dateRange.startDate, dateRange.endDate).then((playerSurnames) => {
                setPossibleElements(playerSurnames);
            });
        else if (QueriesForFilteringAttributesValues.QUERY_TEAMS_NAMES.includes(attribute))
            getAllTeamsNames(dateRange.startDate, dateRange.endDate).then((teamsNames) => {
                setPossibleElements(teamsNames);
            });
        else if (QueriesForFilteringAttributesValues.QUERY_COUNTRIES.includes(attribute))
            getAllCountriesNames().then((countryNames) => {
                setPossibleElements(countryNames);
            });
        else if (QueriesForFilteringAttributesValues.QUERY_LEAGUES.includes(attribute))
            getAllLeagueNames().then((leagueNames) => {
                setPossibleElements(leagueNames);
            });
        else
            console.log(`Attribute "${attribute}" does not match any queries!`)

        setIsLoading(false);
    }, [])
    if (isLoading)
        return <LoadingView/>;

    const addNewElement = () => {
        if (!newElement)
            return;
        if (chosenElements.includes(newElement))
            return;
        setChosenElements([...chosenElements, newElement]);
    }
    const removeElement = (removeIndex) => {
        console.log(removeIndex)
        setChosenElements(chosenElements.filter((_, index) => index != removeIndex));
    }

    return <>
        <Autocomplete 
            variant="outlined" 
            label="Wybierz element"
            selectedKey={newElement}
            onSelectionChange={(value) => setNewElement(value)}
        >
        {
            possibleElements.map((value, index) => (
                <AutocompleteItem key={value}>{value}</AutocompleteItem>
            ))
        }
        </Autocomplete>
        <Button variant="outlined" onPress={() => addNewElement()}>
            <Icon>add</Icon>
            Dodaj do zbioru
        </Button>
        <ChipGroup textValue={""} label={"Zbiór"} onRemove={(keys) => removeElement(...keys)}>
        {   
            chosenElements.map((element, index) => (
                <ChipItem key={index}>{element}</ChipItem>
            ))
        }
        </ChipGroup>
    </>
}