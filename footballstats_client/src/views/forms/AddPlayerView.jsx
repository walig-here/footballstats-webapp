import { useState } from "react";
import { CREATE_LEAGUE, CREATE_PLAYER, CREATE_TEAM, LoginRequired, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { TeamForm } from "../../components/forms/TeamForm";
import { useMutation } from "@apollo/client";
import { Button, Icon } from "actify";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";
import { PlayerForm } from "../../components/forms/PlayerForm";

export function AddPlayerView() {
    const [player, setPlayer] = useState(null);
    const [createPlayerMutation, {loading, error, data}] = useMutation(CREATE_PLAYER);

    const createPlayer = async () => {
        await requestMutation(
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
                            data.createPlayer.errors ? 
                            data.createPlayer.errors.map(err => err.messages.join("\n")) : 
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