import { TextField } from "actify";
import { useEffect, useState } from "react";

export function MatchOwnDataForm({setMatchOwnData, matchOwnData}) {
    const [localMatchOwnData, setLocalMatchOwnData] = useState({
        date: matchOwnData ? matchOwnData.date : ""
    });

    useEffect(() => {
        if (!Object.values(localMatchOwnData).every(Boolean)){
            setMatchOwnData(null);
            return;
        }
        console.log("Match own data provided!")
        setMatchOwnData(localMatchOwnData);
    }, [localMatchOwnData]);

    return (
        <>
            <TextField 
                type="date" 
                variant="outlined" 
                label={"Data rozegrania"}
                value={localMatchOwnData.date}
                onChange={(newDate) => setLocalMatchOwnData(prev => ({...prev, date: newDate}))}
            />
        </>
    );
}