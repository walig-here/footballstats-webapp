import { TextField } from "actify";
import { useEffect, useState } from "react";
import { LeagueSelector } from "../selections/LeagueSelector";

export function SeasonForm({setSeasonData, seasonData}) {
    const [localSeasonData, setLocalSeasonData] = useState({
        name: seasonData ? seasonData.name : "", 
        league: seasonData ? seasonData.league : ""
    });

    useEffect(() => {
        if (!Object.values(localSeasonData).every(Boolean)){
            setSeasonData(null);
            return;
        }
        console.log("Season data provided!");
        setSeasonData(localSeasonData);
    }, [localSeasonData]);

    const content = [
        <>
            <TextField
                value={localSeasonData.name}
                onChange={newName => setLocalSeasonData(prev => ({...prev, name: newName}))}
                type="text"
                variant="outlined"
                label="Nazwa sezonu"
                key={"name-input"}
            />
            <LeagueSelector
                leagueKey={localSeasonData.league}
                nameIsKey={false}
                disableSeasonSelect={true}
                setLeagueKey={(newLeagueId) => setLocalSeasonData(prev => ({...prev, league: newLeagueId}))}
                key={"league-select"}
            />
        </>
    ];
    return content;
}