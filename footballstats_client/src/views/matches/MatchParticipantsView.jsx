import { useMutation, useQuery } from "@apollo/client";
import { useContext, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router";
import { LoadingView } from "../utilities/LoadingView";
import ContentView from "../../components/ContentView";
import { DataRangeControl } from "../../components/DataRangeControl";
import { PlayersList } from "../../components/lists/pLAYERSList";
import { TeamsList } from "../../components/lists/TeamsList";
import { DELETE_PLAYER_FROM_MATCH, GET_MATCH_CRUCIAL_DATA, GET_PLAYERS, requestMutation } from "../../api_client";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat } from "../../data_processing";
import { TabItem, Tabs } from "actify";
import { ModalContext } from "../../components/modals/ModalManager";

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
    const modalContext = useContext(ModalContext);
    const navigate = useNavigate();
    const {id} = useParams();
    const [currentTab, setCurrentTab] = useState(`/match/${id}/participants`);
    const {loading, data, error} = useQuery(...GET_MATCH_QUERY(Number.parseInt(id)));
    const [deletePlayerMutation, deletePlayerResponse] = useMutation(DELETE_PLAYER_FROM_MATCH);

    const deletePlayerFromMatch = (playerId) => {
        requestMutation(
            {
                playerId: Number.parseInt(playerId),
                matchId: Number.parseInt(id)
            },
            deletePlayerMutation,
            "Usunięto zawodnika z meczu",
            "Nie udało się usunąć zawodnika z meczu",
            "removePlayerFromMatch"
        )
    }

    useEffect(() => {
        navigate(currentTab)
    }, [currentTab]);

    if (loading || deletePlayerResponse.loading)
        return <LoadingView/>;
    if (error){
        return <ContentView title={"Mecz nie istnieje"}></ContentView>;
    }

    return (
        <ContentView title={`${data.match.teamsScores[0].teamName} vs ${data.match.teamsScores[1].teamName}`}>
            <Tabs onSelectionChange={(e) => setCurrentTab(e)} defaultSelectedKey={`/match/${id}/participants`}>
                <TabItem title={"Dane"} key={`/match/${id}/data`}></TabItem>
                <TabItem title={"Uczestnicy"} key={`/match/${id}/participants`}></TabItem>
            </Tabs>
            <TeamsList
                title={"Uczestniczące w meczu drużyny"}
                subtitle={"Przeglądaj uczestniczące w meczu drużyny"}
                matchId={Number.parseInt(id)}
            />
            <PlayersList
                title={`Zawodnicy drużyny ${data.match.teamsScores[0].teamName}`}
                subtitle={PLAYER_LIST_DESC}
                team={data.match.teamsScores[0].teamId}
                match={Number.parseInt(id)}
                onDelete={(playerId) => modalContext.openModal(
                    "Czy chcesz usunąć zawodnika z meczu?",
                    () => deletePlayerFromMatch(playerId)
                )}
            />
            <PlayersList
                title={`Zawodnicy drużyny ${data.match.teamsScores[1].teamName}`}
                subtitle={PLAYER_LIST_DESC}
                team={data.match.teamsScores[1].teamId}
                match={Number.parseInt(id)}
                onDelete={(playerId) => modalContext.openModal(
                    "Czy chcesz usunąć zawodnika z meczu?",
                    () => deletePlayerFromMatch(playerId)
                )}
            />
        </ContentView>
    )
}