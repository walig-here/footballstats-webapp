import { useCallback, useContext, useRef, useState } from 'react'
import { DateRangeContext } from '../../App';
import { useQuery } from '@apollo/client';
import { QUERY_PLAYER_CALCULATE_METRIC_FOR_DATA_SERIES, QUERY_TEAM_CALCULATE_METRIC_FOR_DATA_SERIES } from '../../api_client';
import { LoadingView } from '../../views/utilities/LoadingView';
import { DataSeries, MetricTargetObject } from '../../constants';
import { Body } from '../Body';
import { Table } from '../Table';
import { BarChartView } from '../BarChartView';


const getQueryBuilderForTargetObjectType = (targetObjectType) => {
    switch (targetObjectType) {
        case MetricTargetObject.PLAYER:
            return QUERY_PLAYER_CALCULATE_METRIC_FOR_DATA_SERIES
        case MetricTargetObject.TEAM:
            return QUERY_TEAM_CALCULATE_METRIC_FOR_DATA_SERIES
    }
}


export function MetricValueAnalysis({dataSeries, match, team, metricName, objectId, targetObjectType}) {
    const dateRangeContext = useContext(DateRangeContext);
    const calculateMetricResults = useQuery(...getQueryBuilderForTargetObjectType(targetObjectType)(
        objectId, dateRangeContext.startDate, dateRangeContext.endDate, match, team,  metricName, dataSeries
    ));

    if (calculateMetricResults.loading)
        return <LoadingView/>;

    return ( 
        <>
        {
            calculateMetricResults.data ?
            <>
                <BarChartView
                    data={Object.entries(calculateMetricResults.data).map(([stringifiedSeries, metricValue]) => ({
                        dataSeries: DataSeries.destringify(stringifiedSeries),
                        [metricName]: metricValue.calculateMetric >= 0 ? metricValue.calculateMetric : 90.0
                    }))}
                    valueKey={metricName}
                    argumentKey={"dataSeries"}
                />
                <Table
                    columnKeys={["Seria danych", metricName]}
                    data={Object.entries(calculateMetricResults.data).map(([stringifiedSeries, metricValue]) => ({
                        "Seria danych": DataSeries.destringify(stringifiedSeries),
                        [metricName]: metricValue.calculateMetric >= 0 ? metricValue.calculateMetric : 90.0
                    }))}
                />
            </>
            :
            <Body text={calculateMetricResults.error.cause.message}/>
        }
        </>
    )
}