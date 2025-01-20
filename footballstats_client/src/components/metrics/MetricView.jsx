import { useEffect, useState } from "react";
import Section from "../Section";
import { MetricsNames, MetricTargetObject, MetricViewTypes } from "../../constants";
import { getMetricWithName } from "../../data_processing";
import { Button, Icon, IconButton } from "actify";
import { MetricForm } from "./MetricForm";
import { MetricValueAnalysis } from "./MetricValueAnalysis";
import { DataSeriesForm } from "./DataSeriesForm";


const MetricViewState = {
    CREATION: {
        title: (metricName, type) => "Stwórz nowe zestawienie",
        desc: "Wybierz miarę, której ma dotyczyć zestawienie"
    },
    ADD_NEW_SERIES : {
        title: (metricName, type) => `${type}: ${metricName} (dodawanie serii danych)`,
        desc: "Dodaj nową serie danych."
    },
    DISPLAY: {
        title: (metricName, type) => `${type}: ${metricName}`,
        desc: "Przeglądaj wygenerowane zestawienie."
    }
}

/**
 *  Renders metric view section.
 * @param {MetricViewTypes} type Type of metric view.
 * @param {MetricTargetObject} targetType Points to object that is a target of metric calculation.
 * @param {int} match Select a match or all possible matches (null) to provide events source.
 * @param {int} team Select a matches of team or all possible teams (null) to provide events source.
 */
export function MetricView ({type, targetType, match, team, onDelete, objectId}) {
    const [metricName, setMetricName] = useState(null);
    const [state, setState] = useState(MetricViewState.CREATION);
    const [dataSeries, setDataSeries] = useState([]);

    useEffect(() => {
        if (dataSeries.length === 0)
            return;
        setState(MetricViewState.DISPLAY);
    }, [dataSeries])

    const content = () => {
        switch (state) {
            case MetricViewState.CREATION:
                return <MetricForm
                    metricName={metricName}
                    setMetricName={setMetricName}
                    dataSeries={dataSeries}
                    setDataSeries={setDataSeries}
                />;
            case MetricViewState.DISPLAY:
                return <MetricValueAnalysis 
                    objectId={objectId}
                    metricName={metricName}
                    match={match}
                    team={team}
                    targetObjectType={targetType}
                    dataSeries={dataSeries}
                />;
            case MetricViewState.ADD_NEW_SERIES:
                return <>
                    <DataSeriesForm
                        metricName={metricName}
                        setDataSeries={setDataSeries}
                        dataSeries={dataSeries}
                    />
                    <Button
                        onPress={() => setState(MetricViewState.DISPLAY)}
                        variant="tonal"
                    >
                        Anuluj
                    </Button>
                </>
        }
        return <></>;
    }

    const getTopRightContent = () => {
        return <div className="flex flex-row space-x-1">
            {
                state === MetricViewState.DISPLAY &&
                <Button variant="filled" onPress={() => setState(MetricViewState.ADD_NEW_SERIES)}>
                    <Icon>add_circle</Icon>
                </Button>
            }
            {
                onDelete &&
                <Button variant="filled" onPress={onDelete}>
                    <Icon>delete</Icon>
                </Button>
            }
        </div>
    }

    return (
        <Section 
            title={state.title(metricName, type)}
            subtitle={state.desc}
            topRightContent={getTopRightContent()}
        >
        {content()}
        </Section>
    );
}