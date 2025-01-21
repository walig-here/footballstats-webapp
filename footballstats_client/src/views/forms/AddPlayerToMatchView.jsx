import { useState } from "react";
import { ADD_PLAYER_TO_MATCH, CREATE_LEAGUE, CREATE_TEAM, LoginRequired, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { TeamForm } from "../../components/forms/TeamForm";
import { useMutation } from "@apollo/client";
import { Button, Icon } from "actify";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";
import { useNavigate, useParams } from "react-router";
import { AddPlayerToMatchForm } from "../../components/forms/AddPlayerToMatchForm";

export function AddPlayerToMatchView() {
    const {teamId, matchId} = useParams();
    const navigate = useNavigate();
    const [player, setPlayer] = useState({
        minutesPlayed: "",
        playerId: ""
    });
    const [addPlayerToMatchMutation, {loading, error, data}] = useMutation(ADD_PLAYER_TO_MATCH);

    const createLeague = async () => {
        const response = await requestMutation(
            {
                teamId: Number.parseInt(teamId),
                matchId: Number.parseInt(matchId),
                playerId: Number.parseInt(player.playerId),
                minutes: Number.parseFloat(player.minutesPlayed),
            },
            addPlayerToMatchMutation,
            "Dodano zawodnika do meczu",
            "Nie udało się dodać zawodnika do meczu!",
            "addExistingPlayerToMatch"
        )
        if (!response || error || response?.addExistingPlayerToMatch?.errors?.length > 0)
            return;
        navigate(`/match/${matchId}/participants`);
    }

    if (loading)
        return <LoadingView/>;

    return (
        <LoginRequired>
            <ContentView title={"Dodaj zawodnika do meczu"}>
                {
                    (error || data?.addExistingPlayerToMatch?.errors?.length > 0)
                    &&
                    <Body 
                        text={
                            data?.addExistingPlayerToMatch?.errors ? 
                            data?.addExistingPlayerToMatch?.errors.map(err => err.messages.join("\n")) : 
                            error.cause.message
                        }
                        style={"text-error"}
                    />
                }
                <AddPlayerToMatchForm
                    minutesPlayed={player.minutesPlayed}
                    setMinutesPlayed={(minutesPlayed) => setPlayer(prev => ({...prev, minutesPlayed: minutesPlayed}))}
                    playerKey={player.playerId}
                    setPlayerKey={(id) => setPlayer(prev => ({...prev, playerId: id}))}
                />
                {
                    player && Object.values(player).every(Boolean) &&
                    <Button 
                        variant="filled"
                        onPress={() => createLeague()}
                    >
                        <Icon>check</Icon>
                        Dodaj zawodnika do meczu
                    </Button>
                }
            </ContentView>
        </LoginRequired>
    )
}