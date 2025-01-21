import { TextField } from "actify";
import { useEffect, useState } from "react";
import { CountryForm } from "./CountryForm";
import Section from "../Section";
import { NewExistingSelection } from "../NewExistingSelection";
import { CountrySelector } from "../selections/CountrySelector";

export function LeagueForm({setLeague, league}) {
    const [localLeague, setLocalLeague] = useState({
        name: league ? league.name : "", 
        country: league ? league.country : ""
    });

    useEffect(() => {
        console.log(localLeague)
        if (!Object.values(localLeague).every(Boolean)){
            console.log(Object.values(localLeague).every(Boolean))
            setLeague(null);
            return;
        }
        setLeague(localLeague);
    }, [localLeague]);

    return (
        <>
            <TextField
                value={localLeague.name}
                onChange={newName => setLocalLeague(prev => ({...prev, name: newName}))}
                type="text" 
                variant="outlined"
                label="Nazwa ligi"
                key="name-input"
            />
            <CountrySelector
                label={"Wybierz kraj pochodzenia"}
                key={"country-form"}
                countryKey={localLeague.country}
                nameIsKey={false} 
                setCountryKey={
                    countryId => setLocalLeague(prev => ({...prev, country: countryId}))
                }
            />
        </>
    );
}