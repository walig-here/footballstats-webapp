import { TextField } from "actify";

export function RangeForm({from, to, setFilter}) {
    const setValue = (from, to) => {
        setFilter(prev => ({
            ...prev,
            parameters: [from, to]
        }));
    }

    return (<>
        <TextField 
            variant="outlined"
            type="number"
            label="Początek przedziału"
            value={from}
            onChange={(newFrom) => setValue(newFrom, to)}
        />
        <TextField 
            variant="outlined"
            type="number"
            label="Koniec przedziału"
            value={to}
            onChange={(newTo) => setValue(from, newTo)}
        />
    </>)
}