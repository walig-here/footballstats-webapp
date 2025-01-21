import { TextField } from "actify";
import { useEffect, useState } from "react";
import { CountrySelector } from "../selections/CountrySelector";
import { PlayerSelector } from "../selections/PlayerSelector";
import { EventTypeSelector } from "../selections/EventTypeSelector";

export function EventForm({setEvent, event, matchId}) {
    const [localEvent, setLocalEvent] = useState({
        player: event ? event.player : "",
        type: event ? event.type : "", 
        occurrenceMinute: event ? event.occurrenceMinute : ""
    });

    useEffect(() => {
        console.log(localEvent)
        if (!Object.values(localEvent).every(Boolean)){
            setEvent(null);
            return;
        }
        setEvent(localEvent);
    }, [localEvent])

    return (
        <>
            <PlayerSelector
                match={matchId}
                playerKey={localEvent.player}
                setPlayerKey={(playerId) => setLocalEvent(prev => ({...prev, player: playerId}))}
            />
            <EventTypeSelector
                label={"Wybierz typ zdarzenia"}
                eventTypeKey={localEvent.type}
                setEventTypeKey={(eventId) => setLocalEvent(prev => ({...prev, type: eventId}))}
            />
            <TextField
                label={"Moment wystąpienia (minuta meczu)"}
                variant="outlined"
                type="number"
                value={localEvent.occurrenceMinute}
                onChange={(minute) => setLocalEvent(prev => ({...prev, occurrenceMinute: minute}))}
            />
        </>
    )
}