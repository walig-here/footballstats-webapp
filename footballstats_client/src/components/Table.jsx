import { Button, Card, Divider, Icon, IconButton } from "actify";
import { saveAs } from "file-saver";
import { useCallback, useState } from "react";


const TableSortingDirection = {
    ASCENDING: 0,
    DESCENDING: 1
}


export function Table({data, columnKeys}) {
    const [isDownloading, setIsDownloading] = useState(false);

    const downloadTableAsCsv = useCallback(() => {
        setIsDownloading(true);
        const headers = columnKeys;
        const lines = [];
        lines.push(headers.join(','));
        data.forEach(element => lines.push(Object.values(element).join(",")));
        const csvData = lines.join('\n');
        const blob = new Blob([csvData], { type: 'text/csv' });
        saveAs(blob, 'table.csv');
        setIsDownloading(false);
    })

    const columns = <div className="flex flex-row flex-grow space-x-1">{
        columnKeys.map((columnName, columnIndex) => (
            <div className="flex-grow" key={columnIndex}>
                <h1 
                    key={columnIndex}
                    className="text-base font-medium text-on-surface"
                >
                    {columnName}
                </h1>
                {
                    data.map(row => Object.entries(row).filter(([key, _]) => key === columnName).map(([key, value]) => (
                        <div key={key}>
                            <Divider/>
                            <h1>{value}</h1>
                        </div>
                    )))
                }
            </div>
        ))
    }</div>

    return (
        <Card 
            variant="outlined" 
            className="py-1 px-1 space-x-1"
        >
            <div className="flex flex-row">
                {columns}
                {
                    !isDownloading ?
                    <IconButton onPress={downloadTableAsCsv}>
                        <Icon>download</Icon>
                    </IconButton> 
                    :
                    <h1>Eksportowanie tabeli</h1>
                }
            </div>
        </Card>
    )
}