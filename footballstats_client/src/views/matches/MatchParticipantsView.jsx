import { useQuery } from "@apollo/client";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router";
import { LoadingView } from "../utilities/LoadingView";
import ContentView from "../../components/ContentView";
import { DataRangeControl } from "../../components/DataRangeControl";
import { PlayersList } from "../../components/lists/pLAYERSList";
import { TeamsList } from "../../components/lists/TeamsList";
import { GET_MATCH_CRUCIAL_DATA, GET_PLAYERS } from "../../api_client";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat } from "../../data_processing";
import { TabItem, Tabs } from "actify";

const PLAYER_LIST_DESC = "Przeglądaj zawodników reprezentujących drużynę w meczu.";

const QUERY_PLAYERS = (sorting, filters, page, startDate, endDate, match, team) => {
    const [textualFilters, metricFilters] = convertFiltersToBackendFormat(filters);
    return [
        GET_PLAYERS,
        {
            variables: {
                page: page - 1,
                textualFilters: textualFilters,
                metricFilters: metricFilters,
                sorting: convertSortingToBackendFormat(sorting),
                startDate: startDate,
                endDate: endDate,
                match: match,
                team: team
            },
        }
    ]
}

const GET_MATCH_QUERY = (matchId) => [
    GET_MATCH_CRUCIAL_DATA,
    {variables: {id: matchId}}
]

export default function MatchParticipantsView() {
    const navigate = useNavigate();
    const {id} = useParams();
    const [currentTab, setCurrentTab] = useState(`/match/${id}/participants`);
    const {loading, data, error} = useQuery(...GET_MATCH_QUERY(Number.parseInt(id)));

    useEffect(() => {
        navigate(currentTab)
    }, [currentTab]);

    if (loading)
        return <LoadingView/>;
    if (error)
        console.log(error);

    return (
        <ContentView title={`${data.match.teamsScores[0].teamName} vs ${data.match.teamsScores[1].teamName}`}>
            <Tabs onSelectionChange={(e) => setCurrentTab(e)} defaultSelectedKey={`/match/${id}/participants`}>
                <TabItem title={"Dane"} key={`/match/${id}/data`}></TabItem>
                <TabItem title={"Uczestnicy"} key={`/match/${id}/participants`}></TabItem>
            </Tabs>
            <PlayersList
                title={`Zawodnicy drużyny ${data.match.teamsScores[0].teamName}`}
                subtitle={PLAYER_LIST_DESC}
                buildQueryFunction={QUERY_PLAYERS}
                team={data.match.teamsScores[0].teamId}
                match={Number.parseInt(id)}
            />
            <PlayersList
                title={`Zawodnicy drużyny ${data.match.teamsScores[1].teamName}`}
                subtitle={PLAYER_LIST_DESC}
                buildQueryFunction={QUERY_PLAYERS}
                team={data.match.teamsScores[1].teamId}
                match={Number.parseInt(id)}
            />
        </ContentView>
    )
}