import { useQuery } from "@apollo/client";
import { useNavigate, useParams } from "react-router";
import { buildTeamQuery } from "../../api_client";
import { useEffect, useState } from "react";
import { MetricTargetObject, MetricViewTypes } from "../../constants";
import { LoadingView } from "../utilities/LoadingView";
import ContentView from "../../components/ContentView";
import { Button, Icon, TabItem, Tabs } from "actify";
import { DataRangeControl } from "../../components/DataRangeControl";
import { MetricView } from "../../components/metrics/MetricView";

export default function TeamThroughTimeView() {
    const navigate = useNavigate();
    const {id} = useParams();
    const {loading, data, error} = useQuery(...buildTeamQuery(Number.parseInt(id)));
    const DEFAULT_PATH = `/team/${id}/through_time`;
    const [currentTab, setCurrentTab] = useState(DEFAULT_PATH);
    const [metricViews, setMetricViews] = useState([]);
    const [generatedMetrics, setGeneratedMetrics] = useState(0);

    const removeMetricView = (removeIndex) => {
        console.log(`usuwam zestawienie ${removeIndex}`)
        setMetricViews(prev => prev.filter((element, index) => element.key !== removeIndex));
    };
    const addMetricView = () => {
        const newView = <MetricView
            type={MetricViewTypes.HISTORY}
            targetType={MetricTargetObject.TEAM}
            objectId={Number.parseInt(id)}
            key={generatedMetrics}
            match={-1}
            team={-2}
            onDelete={() => removeMetricView(`${generatedMetrics}`)}
        />
        setMetricViews(prev => [newView, ...prev]);
        setGeneratedMetrics(prev => prev + 1)
    };

    useEffect(() => {
        navigate(currentTab);
    }, [currentTab]);

    if (loading)
        return <LoadingView/>;
    if (error)
        return <ContentView title={"Drużyna nie istnieje"}/>;

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