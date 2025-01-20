import { useContext } from "react"
import { QUERY_PLAYER_METRIC_HISTORY_FOR_DATA_SERIES } from "../../api_client"
import { DateRangeContext } from "../../App"
import { useQuery } from "@apollo/client"
import { LoadingView } from "../../views/utilities/LoadingView"
import { Body } from "../Body"
import { Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts"
import { DataSeries, MetricTargetObject } from "../../constants"
import { LinearChartView } from "../LinearChartView"
import { Table } from "../Table"

const getQueryBuilderFortargetObjectType = (targetObjectType) => {
    switch (targetObjectType) {
        case MetricTargetObject.PLAYER:
            return QUERY_PLAYER_METRIC_HISTORY_FOR_DATA_SERIES
    }
}

export function MetricHistoryAnalysis({dataSeries, metricName, objectId, targetObjectType}) {
    const dateRangeContext = useContext(DateRangeContext);
    const calculateMetricHistoryResults = useQuery(...getQueryBuilderFortargetObjectType(targetObjectType)(
        objectId, dateRangeContext.startDate, dateRangeContext.endDate, metricName, dataSeries
    ));

    if (calculateMetricHistoryResults.loading)
        return <LoadingView/>

    const convertDataToLineSeries = () => {
        const seriesKeys = Object.keys(calculateMetricHistoryResults.data);
        const timeMap = new Map();
        seriesKeys.forEach(series => {
            calculateMetricHistoryResults.data[series].metricHistory.forEach(item => {
                const { time, value } = item;
    
                if (!timeMap.has(time)) {
                    timeMap.set(time, { Data: time });
                }
                timeMap.get(time)[DataSeries.destringify(series)] = value >= 0 ? value : 90.0;
            });
        });
        return Array.from(timeMap.values());
    }
    const data = convertDataToLineSeries();

    return (
        <>
        {
            calculateMetricHistoryResults.data ?
            <>
                <LinearChartView
                    data={data}
                    argumentKey={"Data"}
                    valuesKeys={Object.keys(calculateMetricHistoryResults.data).map(name => DataSeries.destringify(name))}
                />
                <Table
                    data={data}
                    columnKeys={["Data", ...Object.keys(calculateMetricHistoryResults.data).map(name => DataSeries.destringify(name))]}
                />
            </>
            :
            <Body text={calculateMetricHistoryResults.error.cause.message}/>
        }
        </>
    )
}