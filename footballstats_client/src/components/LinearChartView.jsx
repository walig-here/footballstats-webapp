import { Icon, IconButton } from "actify";
import { saveAs } from "file-saver";
import { useCallback, useState } from "react";
import { Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { useCurrentPng } from "recharts-to-png";

function getRandomColorInRange(startColor, endColor) {
    const hexToRgb = (hex) => {
        const bigint = parseInt(hex.slice(1), 16);
        return {
            r: (bigint >> 16) & 255,
            g: (bigint >> 8) & 255,
            b: bigint & 255,
        };
    };

    const rgbToHex = ({ r, g, b }) => {
        const toHex = (value) => value.toString(16).padStart(2, "0");
        return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
    };

    const getRandomInRange = (start, end) =>
        Math.floor(Math.random() * (end - start + 1)) + start;

    const startRgb = hexToRgb(startColor);
    const endRgb = hexToRgb(endColor);

    const randomRgb = {
        r: getRandomInRange(startRgb.r, endRgb.r),
        g: getRandomInRange(startRgb.g, endRgb.g),
        b: getRandomInRange(startRgb.b, endRgb.b),
    };

    return rgbToHex(randomRgb);
}

export function LinearChartView({data, argumentKey, valuesKeys}) {
    const [getPng, {ref, isLoading}] = useCurrentPng();
    const [isDownloading, setIsDownloading] = useState(false);

    const handleDownload = useCallback(async () => {
        setIsDownloading(true);
        const png = await getPng();
        if (png)
            saveAs(png, "chart.png")
        setIsDownloading(false);
    }, [getPng])

    return (
        <>
            <div className="flex flex-row justify-end">
            {
                !isDownloading ?
                <IconButton onPress={handleDownload}><Icon>Download</Icon></IconButton> :
                <h1>Esportowani wykresu...</h1>
            }
            </div>
            <ResponsiveContainer width="99%" height={400}>
                <LineChart
                    data={data}
                    ref={ref}
                >
                    <XAxis dataKey={argumentKey}/>
                    <YAxis/>
                    {
                        valuesKeys.map(valueKey => (
                            <Line 
                                dataKey={valueKey} 
                                activeDot={{r: 5}} 
                                stroke={getRandomColorInRange("#0E341E", "#29A378")}
                                strokeWidth={3}
                            />
                        ))
                    }            
                    <Tooltip/>
                    <Legend></Legend>
                </LineChart>
            </ResponsiveContainer>
        </>
    )
}