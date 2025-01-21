import { TextField } from "actify";
import Section from "../Section";
import { PlayerSelector } from "../selections/PlayerSelector";

export function AddPlayerToMatchForm({setPlayerKey, playerKey, minutesPlayed, setMinutesPlayed}) {
    return (
        <>
            <PlayerSelector
                nameIsKey={false}
                setPlayerKey={setPlayerKey}
                playerKey={playerKey}
            />
            <TextField
                label="Czas gry (w minutach)"
                variant="outlined"
                type="number"
                value={minutesPlayed}
                onChange={(value) => setMinutesPlayed(value)}
            />
        </>
    );
}