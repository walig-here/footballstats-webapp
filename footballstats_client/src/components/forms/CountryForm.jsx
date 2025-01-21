import { TextField } from "actify";
import { useEffect, useState } from "react";

export function CountryForm({setCountry, country}) {
    const [localCountry, setLocalCountry] = useState({
        name: country ? country.name : ""
    });

    useEffect(() => {
        if (!Object.values(localCountry).every(Boolean))
            return;
        console.log("Country data provided!");
        setCountry(localCountry);
    }, [localCountry])

    return (
        <>
            <TextField
                variant="outlined"
                value={localCountry.name}
                label="Nazwa kraju"
                onChange={(newName) => setLocalCountry(prev => ({...prev, name: newName}))}
            />
        </>
    )
}