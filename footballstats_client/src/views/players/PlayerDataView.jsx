import { Button, Icon, TabItem, Tabs } from "actify";
import ContentView from "../../components/ContentView";
import { useNavigate, useParams } from "react-router";
import { useEffect, useState } from "react";
import { useQuery } from "@apollo/client";
import { buildPlayerQuery } from "../../api_client";
import { LoadingView } from "../utilities/LoadingView";
import Section from "../../components/Section";
import { Body } from "../../components/Body";
import { MetricView } from "../../components/metrics/MetricView";
import { MetricTargetObject, MetricViewTypes } from "../../constants";
import { DataRangeControl } from "../../components/DataRangeControl";

export default function PlayerDataView() {
    const navigate = useNavigate();
    const {id} = useParams();
    const DEFAULT_PATH = `/player/${id}/data`;
    const [currentTab, setCurrentTab] = useState(DEFAULT_PATH);
    const {loading, data, error} = useQuery(...buildPlayerQuery(Number.parseInt(id)));
    const [metricViews, setMetricViews] = useState([]);
    const [generatedMetrics, setGeneratedMetrics] = useState(0);

    const removeMetricView = (removeIndex) => {
        console.log(removeIndex)
        setMetricViews(prev => prev.filter((element, index) => element.key !== removeIndex));
    };
    const addMetricView = () => {
        const newView = <MetricView
            type={MetricViewTypes.ANALYZE}
            targetType={MetricTargetObject.PLAYER}
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
    if (error){
        return <ContentView title={"Zawodnik nie istnieje"}></ContentView>;
    }

    return (
        <ContentView title={`${data.player.name} ${data.player.surname}`}>
            <Tabs 
                defaultSelectedKey={DEFAULT_PATH} 
                onSelectionChange={(tab) => setCurrentTab(tab)}
            >
                <TabItem title={"Dane"} key={DEFAULT_PATH}/>
                <TabItem title={"Zawodnik w czasie"} key={`/player/${id}/through_time`}/>
                <TabItem title={"Mecze i drużyny"} key={`/player/${id}/matches_and_teams`}/>
            </Tabs>
            <Section
                title={"O zawodniku"}
                subtitle={"Poznaj szczegółowe dane zawodnika."}
                iconName={"info"}
            >
                <div className="space-y-1">
                    <div className="flex flex-row space-x-2">
                        <Body text={"Imie i naziwsko: "} style={"font-medium"}/>
                        <Body text={`${data.player.name} ${data.player.surname}`}/>
                    </div>
                    <div className="flex flex-row space-x-2">
                        <Body text={"Pseudonim: "} style={"font-medium"}/>
                        <Body text={data.player.nickname ? data.player.nickname : "brak"}/>
                    </div>
                    <div className="flex flex-row space-x-2">
                        <Body text={"Kraj pochodzenia: "} style={"font-medium"}/>
                        <Body text={data.player.countryOfOrigin.name}/>
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
            {...metricViews}
        </ContentView>
    );
}