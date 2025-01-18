import { TextField } from "actify";

export default function EqualsForm({value, setFilter}) {
    const setValue = (newValue) => [
        setFilter(prev => ({
            ...prev,
            parameters: [newValue]
        }))
    ];

    return <>
        <TextField
            variant="outlined" 
            label="Wartość wzorcowa"
            type="number"
            value={value}
            onChange={(newValue) => setValue(newValue)}
        />
    </>
}