import { TextField } from "actify";
import { useEffect, useState } from "react";
import { CountrySelector } from "../selections/CountrySelector";

export function TeamForm({setTeam, team}) {
    const [localTeam, setLocalTeam] = useState({
        name: team ? team.name : "", 
        country: team ? team.country : ""
    });

    useEffect(() => {
        console.log(localTeam)
        if (!Object.values(localTeam).every(Boolean)){
            setTeam(null);
            return;
        }
        setTeam(localTeam);
    }, [localTeam])

    return (
        <>
            <TextField
                value={localTeam.name}
                onChange={newName => setLocalTeam(prev => ({...prev, name: newName}))}
                type="text" 
                variant="outlined"
                label="Nazwa drużyny"
                key="name-input"
            />
            <CountrySelector
                countryKey={localTeam.country}
                label={"Kraj pochodzenia drużyny"}
                nameIsKey={false}
                setCountryKey={(newCountryId) => setLocalTeam(prev => ({...prev, country: newCountryId}))}
            />
        </>
    )
}