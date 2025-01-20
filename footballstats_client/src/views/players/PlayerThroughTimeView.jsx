import { useQuery } from "@apollo/client";
import ContentView from "../../components/ContentView";
import { buildPlayerQuery } from "../../api_client";
import { useNavigate, useParams } from "react-router";
import { useEffect, useState } from "react";
import { LoadingView } from "../utilities/LoadingView";
import { Button, Icon, TabItem, Tabs } from "actify";
import { DataRangeControl } from "../../components/DataRangeControl";
import { MetricView } from "../../components/metrics/MetricView";
import { MetricTargetObject, MetricViewTypes } from "../../constants";

export default function PlayerThroughTimeView() {
    const navigate = useNavigate();
    const {id} = useParams();
    const {loading, data, error} = useQuery(...buildPlayerQuery(Number.parseInt(id)));
    const DEFAULT_PATH = `/player/${id}/through_time`;
    const [currentTab, setCurrentTab] = useState(DEFAULT_PATH);
    const [metricViews, setMetricViews] = useState([]);

    const removeMetricView = (removeIndex) => {
        setMetricViews(prev => prev.filter((element, index) => index !== removeIndex));
    };
    const addMetricView = () => {
        const newView = <MetricView
            type={MetricViewTypes.HISTORY}
            targetType={MetricTargetObject.PLAYER}
            match={-1}
            team={-2}
            objectId={Number.parseInt(id)}
            onDelete={() => removeMetricView(metricViews.length)}
        />
        setMetricViews(prev => [newView, ...prev]);
    };

    useEffect(() => {
        navigate(currentTab);
    }, [currentTab]);

    if (loading)
        return <LoadingView/>;

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
            <Button 
                variant="outlined"
                onPress={() => addMetricView()}
            >
                <Icon>add_circle</Icon>
                Nowa analiza zmian wartości miar w czasie
            </Button>
            {...metricViews}
        </ContentView>
    );
}