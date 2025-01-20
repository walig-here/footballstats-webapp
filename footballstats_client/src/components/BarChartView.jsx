import { Button, Icon, IconButton } from "actify";
import { useCallback, useRef, useState } from "react";
import { Bar, BarChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { useCurrentPng } from "recharts-to-png";

export function BarChartView({data, argumentKey, valueKey}) {
    const [getPng, {ref, isLoading}] = useCurrentPng();
    const [isDownloading, setIsDownloading] = useState(false);

    const handleDownload = useCallback(async () => {
        setIsDownloading(true);
        const png = await getPng();
        if (png)
            saveAs(png, "chart.png");
        setIsDownloading(false);
    }, [getPng]);

    const chartHeight = data ? data.length * 50 + 50 : 1;
    const maxLabelLength = (
        data ?
        data.map(dataSeries => dataSeries[argumentKey]).sort((a, b) => {
            return b.length - a.length;
        })[0].length :
        0
    )
    const yAxisWidth = maxLabelLength * 10;

    return (
        <>
            <div className="flex flex-row justify-end">
            {
                !isDownloading ?
                <IconButton onPress={handleDownload}><Icon>download</Icon></IconButton>
                :
                <h1>Eksportowanie wykresu...</h1>
            }
            </div>
            <ResponsiveContainer width="99%" height={chartHeight}>
                <BarChart
                    ref={ref}
                    layout='vertical'
                    data={data}
                >
                    <XAxis type="number"/>
                    <YAxis 
                        type="category" 
                        dataKey={argumentKey}
                        tickMargin={8}
                        tickFormatter={(value) => value} 
                        width={yAxisWidth}
                    />
                    <Bar dataKey={valueKey} fill='#165531'/>
                    <Tooltip/>
                </BarChart>
            </ResponsiveContainer>
        </>
    )
}