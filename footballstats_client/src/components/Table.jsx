import { Button, Card, Divider, Icon, IconButton } from "actify";
import { useState } from "react";


const TableSortingDirection = {
    ASCENDING: 0,
    DESCENDING: 1
}


export function Table({data, columnKeys}) {
    const [sorting, setSorting] = useState({
        columnKey: columnKeys[0],
        direction: TableSortingDirection.ASCENDING
    });

    const downloadTableAsCsv = () => {
        const headers = columnKeys;
        const lines = [];
        lines.push(headers.join(','));
        data.forEach(element => lines.push(Object.values(element).join(",")));
        const csvData = lines.join('\n');
    
        const blob = new Blob([csvData], { type: 'text/csv' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'table.csv';
        a.click();
    }

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
                <IconButton onPress={() => downloadTableAsCsv()}>
                    <Icon>download</Icon>
                </IconButton>
            </div>
        </Card>
    )
}