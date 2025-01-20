import { useQuery } from "@apollo/client";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router";
import { buildTeamQuery } from "../../api_client";
import { LoadingView } from "../utilities/LoadingView";
import ContentView from "../../components/ContentView";
import { Button, Icon, TabItem, Tabs } from "actify";
import Section from "../../components/Section";
import { Body } from "../../components/Body";
import { DataRangeControl } from "../../components/DataRangeControl";
import { MetricView } from "../../components/metrics/MetricView";
import { MetricTargetObject, MetricViewTypes } from "../../constants";

export default function TeamDataView() {
    const navigate = useNavigate();
    const {id} = useParams();
    const DEFAULT_PATH = `/team/${id}/data`;
    const [currentTab, setCurrentTab] = useState(DEFAULT_PATH);
    const {loading, data, error} = useQuery(...buildTeamQuery(Number.parseInt(id)));
    const [metricsViews, setMetricViews] = useState([]);
    const [generatedMetrics, setGeneratedMetrics] = useState(0);

    const removeMetricView = (removeIndex) => {
        console.log(removeIndex)
        setMetricViews(prev => prev.filter((element, index) => element.key !== removeIndex));
    };
    const addMetricView = () => {
        const newView = <MetricView
            type={MetricViewTypes.ANALYZE}
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
        return <LoadingView/>
    if (error)
        return <ContentView title={"Zawodnik nie istnieje!"}/>

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
            <Section
                title={"O drużynie"}
                subtitle={"Poznaj szczegółowe dane drużyny"}
                iconName={"info"}
            >
                <div className="space-y-1">
                    <div className="flex flex-row space-x-2">
                        <Body text={"Nazwa drużyny: "} style={"font-medium"}/>
                        <Body text={data.team.name}/>
                    </div>
                    <div className="flex flex-row space-x-2">
                        <Body text={"Kraj pochodzenia: "} style={"font-medium"}/>
                        <Body text={data.team.name}/>
                    </div>
                </div>
            </Section>
            <DataRangeControl/>
            <Button
                variant="outlined"
                onPress={() => addMetricView()}
            >
                <Icon>add_circle</Icon>
                Nowe zestawienie wartości miar
            </Button>
            {...metricsViews}
        </ContentView>
    );
}