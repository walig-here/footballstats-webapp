import { useCallback } from "react";
import { useCurrentPng } from "recharts-to-png";

export function BarChartView({data, argumentKey, valueKey}) {
    const [getPng, {ref, isLoading}] = useCurrentPng();

    const handleDownload = useCallback(async () => {
        const png = await getPng();
        if (png)
            saveAs(png, "chart.png");
    }, [getPng]);

    const chartHeight = calculateMetricResults.data ? Object.entries(calculateMetricResults.data).length * 50 + 50 : 1;
    const maxLabelLength = (
        data ?
        Object.keys(data).sort((a, b) => {
            return b.length - a.length;
        })[0].length :
        0
    )
    const yAxisWidth = maxLabelLength * 15;

    return (
        <>
            <Button onPress={handleDownload}>Pobierz wykres</Button>
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