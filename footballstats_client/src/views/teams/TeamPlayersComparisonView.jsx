import { useQuery } from "@apollo/client";
import { useNavigate, useParams } from "react-router";
import { buildPlayerQuery, buildTeamQuery } from "../../api_client";
import { useEffect, useState } from "react";
import { LoadingView } from "../utilities/LoadingView";
import ContentView from "../../components/ContentView";
import { TabItem, Tabs } from "actify";
import { DataRangeControl } from "../../components/DataRangeControl";
import { PlayersList } from "../../components/lists/pLAYERSList";
import { MatchesList } from "../../components/lists/MatchesList";

export default function TeamPlayersComparisonView() {
    const navigate = useNavigate();
    const {id} = useParams();
    const DEFAULT_PATH = `/team/${id}/players_comparison`;
    const [currentTab, setCurrentTab] = useState(DEFAULT_PATH);
    const {loading, data, error} = useQuery(...buildTeamQuery(Number.parseInt(id)));

    useEffect(() => {
        navigate(currentTab);
    }, [currentTab]);

    if (loading)
        return <LoadingView/>
    if (error)
        return <ContentView title={"Drużyna nie istnieje"}/>

    return (
        <ContentView title={data.team.name}>
            <Tabs
                defaultSelectedKey={DEFAULT_PATH}
                onSelectionChange={(tab) => setCurrentTab(tab)}
            >
                <TabItem title={"Dane"} key={`/team/${id}/data`}/>
                <TabItem title={"Drużyna w czasie"} key={`/team/${id}/through_time`}/>
                <TabItem title={"Reprezentanci i mecze"} key={`/team/${id}/players_comparison`}/>
            </Tabs>
            <DataRangeControl/>
            <MatchesList
                teamId={Number.parseInt(id)}
                title={"Mecze drużyny"}
                subtitle={"Przeglądaj wszystkie mecze rozegrane przez drużynę."}
            />
            <PlayersList
                team={Number.parseInt(id)}
                title={"Reprezentanci drużyny"}
                subtitle={"Przeglądaj wszystkich zawodników, którzy kiedykolwiek reprezentowali drużynę."}
            />
        </ContentView>
    );
}