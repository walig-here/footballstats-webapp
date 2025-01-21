import { TextField } from "actify";
import { useEffect, useState } from "react";
import { CountrySelector } from "../selections/CountrySelector";

export function PlayerForm({setPlayer, player}) {
    const [localPlayer, setLocalPlayer] = useState({
        name: player ? player.name : "", 
        surname: player ? player.surname : "", 
        country: player ? player.country : ""
    });
    const [nickname, setNickname] = useState("");

    useEffect(() => {
        if (!Object.values(localPlayer).every(Boolean)){
            setPlayer(null);
            return;
        }
        setPlayer({
            ...localPlayer,
            nickname: nickname ? nickname : null
        });
    }, [localPlayer])

    return (
        <>
            <TextField
                value={localPlayer.name}
                onChange={newName => setLocalPlayer(prev => ({...prev, name: newName}))}
                type="text" 
                variant="outlined"
                label="Imie zawodnika"
                key="name-input"
            />
            <TextField
                value={localPlayer.surname}
                onChange={newSurname => setLocalPlayer(prev => ({...prev, surname: newSurname}))}
                type="text" 
                variant="outlined"
                label="Nazwisko zawodnika"
                key="surname-input"
            />
            <TextField
                value={localPlayer.nickname}
                onChange={newNickname => setNickname(newNickname)}
                type="text" 
                variant="outlined"
                label="Pseudonim zawodnika"
                key="nickname-input"
            />
            <CountrySelector
                countryKey={localPlayer.country}
                label={"Kraj pochodzenia zawodnika"}
                nameIsKey={false}
                setCountryKey={(newCountryId) => setLocalPlayer(prev => ({...prev, country: newCountryId}))}
            />
        </>
    )
}