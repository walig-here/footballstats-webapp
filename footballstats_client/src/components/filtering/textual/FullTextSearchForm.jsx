import { TextField } from "actify"

export function FullTextSearchForm({searchText, setNewFilter}) {
    const setSearchText = (value) => [
        setNewFilter(prev => ({
            ...prev,
            parameters: [value]
        }))
    ];

    return <>
        <TextField
            variant="outlined" 
            label="Ciąg wyszukiwania"
            value={searchText}
            onChange={(value) => setSearchText(value)}
        />
    </>
}