import { useQuery } from "@apollo/client";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router";
import { buildPlayerQuery, GET_ALL_TEAMS } from "../../api_client";
import { LoadingView } from "../utilities/LoadingView";
import ContentView from "../../components/ContentView";
import { TabItem, Tabs } from "actify";
import { DataRangeControl } from "../../components/DataRangeControl";
import { TeamsList } from "../../components/lists/TeamsList";
import { MatchesList } from "../../components/lists/MatchesList";


export default function PlayerMatchesAndTeamsView() {
    const navigate = useNavigate();
    const {id} = useParams();
    const DEFAULT_PATH = `/player/${id}/matches_and_teams`;
    const [currentTab, setCurrentTab] = useState(DEFAULT_PATH);
    const {loading, data, error} = useQuery(...buildPlayerQuery(Number.parseInt(id)));

    useEffect(() => {
        navigate(currentTab);
    }, [currentTab]);

    if (loading) {
        return <LoadingView/>;
    }
    if (error) {
        return <ContentView title={"Zawodnik nie istnieje!"}/>
    }

    return (
        <ContentView title={`${data.player.name} ${data.player.surname}`}>
            <Tabs
                defaultSelectedKey={DEFAULT_PATH} 
                onSelectionChange={(tab) => setCurrentTab(tab)}
            >
                <TabItem title={"Dane"} key={`/player/${id}/data`}/>
                <TabItem title={"Zawodnik w czasie"} key={`/player/${id}/through_time`}/>
                <TabItem title={"Mecze i drużyny"} key={`/player/${id}/matches_and_teams`}/>
            </Tabs>
            <DataRangeControl/>
            <TeamsList
                playerId={Number.parseInt(id)}
                title={"Drużyny zawodnika"}
                subtitle={"Przeglądaj wszystkie drużyny reprezentowane przez zawodnika z aktualnym zakresie dat."}
            />
            <MatchesList
                playerId={Number.parseInt(id)}
                title={"Mecze zawodnika"}
                subtitle={"Przeglądaj wszystkie mecze, w których grał zaowdnik"}
            />
        </ContentView>
    )
}