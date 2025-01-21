import { useState } from "react";
import { CREATE_LEAGUE, CREATE_PLAYER, CREATE_TEAM, LoginRequired, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { TeamForm } from "../../components/forms/TeamForm";
import { useMutation } from "@apollo/client";
import { Button, Icon } from "actify";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";
import { PlayerForm } from "../../components/forms/PlayerForm";
import { useNavigate } from "react-router";

export function AddPlayerView() {
    const navigate = useNavigate()
    const [player, setPlayer] = useState(null);
    const [createPlayerMutation, {loading, error, data}] = useMutation(CREATE_PLAYER);

    const createPlayer = async () => {
        const response = await requestMutation(
            {
                name: player.name,
                countryId: Number.parseInt(player.country),
                surname: player.surname,
                nickname: player.nickname,
            },
            createPlayerMutation,
            "Dodano zawodnika",
            "Nie udało się dodać zawodnika!",
            "createPlayer"
        )
        if (!response || error || response?.createPlayer?.errors?.length > 0)
            return
        navigate("/list/players")
    }

    if (loading)
        return <LoadingView/>;

    return (
        <LoginRequired>
            <ContentView title={"Dodaj zawodnika"}>
                {
                    (error || data?.createPlayer?.errors?.length > 0)
                    &&
                    <Body 
                        text={
                            data?.createPlayer?.errors ? 
                            data?.createPlayer?.errors.map(err => err.messages.join("\n")) : 
                            error.cause.message
                        }
                        style={"text-error"}
                    />
                }
                <PlayerForm
                    player={player}
                    setPlayer={setPlayer}
                />
                {
                    player && Object.values({...player, nickname: "a"}).every(Boolean) &&
                    <Button 
                        variant="filled"
                        onPress={() => createPlayer()}
                    >
                        <Icon>check</Icon>
                        Dodaj ligę
                    </Button>
                }
            </ContentView>
        </LoginRequired>
    )
}