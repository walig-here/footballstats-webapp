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
    const [getPng, {ref, isLoading}] = useCurrentPng();

    const handleDownload = useCallback(async () => {
        const png = await getPng();
        if (png)
            saveAs(png, "chart.png");
    }, [getPng]);

    if (calculateMetricResults.loading)
        return <LoadingView/>;

    const chartHeight = calculateMetricResults.data ? Object.entries(calculateMetricResults.data).length * 50 + 50 : 1;
    const maxLabelLength = (
        calculateMetricResults.data ? 
        Object.keys(calculateMetricResults.data).sort((a, b) => {
            return DataSeries.destringify(b).length - DataSeries.destringify(a).length;
        })[0].length :
        0
    )
    const yAxisWidth = maxLabelLength * 15;

    return ( 
        <>
        {
            calculateMetricResults.data ?
            <>
                <Button onPress={handleDownload}>Pobierz wykres</Button>
                <ResponsiveContainer width="99%" height={chartHeight}>
                        <BarChart
                            ref={ref}
                            layout='vertical'
                            data={Object.entries(calculateMetricResults.data).map(([stringifiedSeries, metricValue]) => ({
                                dataSeries: DataSeries.destringify(stringifiedSeries),
                                [metricName]: metricValue.calculateMetric >= 0 ? metricValue.calculateMetric : 90.0
                            }))}
                        >
                            <XAxis type="number"/>
                            <YAxis 
                                type="category" 
                                dataKey="dataSeries" 
                                tickMargin={8}
                                tickFormatter={(value) => value} 
                                width={yAxisWidth}
                            />
                            <Bar dataKey={metricName} fill='#165531'/>
                            <Tooltip/>
                        </BarChart>
                </ResponsiveContainer>
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