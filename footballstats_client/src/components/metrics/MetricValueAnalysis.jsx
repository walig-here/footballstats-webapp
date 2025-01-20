import { useCallback, useContext, useRef, useState } from 'react'
import {Bar, BarChart, Rectangle, ResponsiveContainer, XAxis, YAxis, Tooltip} from 'recharts'
import { DateRangeContext } from '../../App';
import { useQuery } from '@apollo/client';
import { QUERY_PLAYER_CALCULATE_METRIC_FOR_DATA_SERIES } from '../../api_client';
import { LoadingView } from '../../views/utilities/LoadingView';
import { DataSeries, MetricTargetObject } from '../../constants';
import { Body } from '../Body';
import { Table } from '../Table';
import { Button } from 'actify';
import {useCurrentPng} from 'recharts-to-png';
import {saveAs} from 'file-saver';
import { BarChartView } from '../BarChartView';


const getQueryForTargetObjectType = (targetObjectType) => {
    switch (targetObjectType) {
        case MetricTargetObject.PLAYER:
            return QUERY_PLAYER_CALCULATE_METRIC_FOR_DATA_SERIES
    }
}


export function MetricValueAnalysis({dataSeries, match, team, metricName, objectId, targetObjectType}) {
    const dateRangeContext = useContext(DateRangeContext);
    const calculateMetricResults = useQuery(...getQueryForTargetObjectType(targetObjectType)(
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